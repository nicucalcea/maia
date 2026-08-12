import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPHICS = os.environ.get('SAMIZDATA_GRAPHICS_PACKAGE', 'github:samizdata-co/graphics#v0.0.1')
FULL_BUILD = os.environ.get('MAIA_TEST_FULL_BUILD') == '1'


class GenerationTests(unittest.TestCase):
    def generate(self, interactive: str) -> Path:
        temporary = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, temporary)
        slug = 'interactive-test' if interactive != 'None' else 'plain-test'
        subprocess.run(
            [
                'uvx', 'cookiecutter', str(ROOT), '--no-input',
                'project_name=Generated Test', f'project_slug={slug}',
                'notebook=None', 'language=None', 'virtual_env=None',
                f'interactive={interactive}',
                f'graphics_package={GRAPHICS}',
            ],
            cwd=temporary,
            check=True,
        )
        return temporary / slug

    def test_none_preserves_project_without_visuals(self):
        project = self.generate('None')
        self.assertFalse((project / 'visuals').exists())
        self.assertFalse((project / 'package.json').exists())

    def test_interactive_generates_allowlisted_workspace(self):
        project = self.generate('Svelte + Layer Cake')
        visuals = project / 'visuals'
        self.assertTrue((visuals / 'src/register.ts').is_file())
        self.assertTrue((project / 'data/processed/web').is_dir())

        if FULL_BUILD:
            subprocess.run(['pnpm', 'install'], cwd=visuals, check=True)
            subprocess.run(['pnpm', 'check'], cwd=visuals, check=True)
            subprocess.run(['pnpm', 'build'], cwd=visuals, check=True)
            self.assertTrue(
                (project / 'output/interactives/interactive-test/embed.html').is_file()
            )

        source = project / 'data/processed/web/chart.json'
        source.write_text('[{"period":1,"value":2}]\n')
        (visuals / 'data-manifest.json').write_text(json.dumps({'files': ['chart.json']}))
        subprocess.run(['node', 'scripts/prepare-data.mjs'], cwd=visuals, check=True)
        self.assertEqual((visuals / 'static/data/chart.json').read_text(), source.read_text())

        (visuals / 'data-manifest.json').write_text(json.dumps({'files': ['../secret.json']}))
        escaped = subprocess.run(
            ['node', 'scripts/prepare-data.mjs'], cwd=visuals, capture_output=True, text=True
        )
        self.assertNotEqual(escaped.returncode, 0)
        self.assertIn('escapes data/processed/web', escaped.stderr)


if __name__ == '__main__':
    unittest.main()

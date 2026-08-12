{% raw %}import { cp, mkdir, readFile, rm, stat } from 'node:fs/promises';
import { dirname, isAbsolute, relative, resolve, sep } from 'node:path';

const visualsRoot = resolve(import.meta.dirname, '..');
const projectRoot = resolve(visualsRoot, '..');
const sourceRoot = resolve(projectRoot, 'data/processed/web');
const destinationRoot = resolve(visualsRoot, 'static/data');
const manifestPath = resolve(visualsRoot, 'data-manifest.json');

function safeSourcePath(entry) {
  if (typeof entry !== 'string' || !entry || isAbsolute(entry) || entry.includes('\0')) {
    throw new Error('Manifest entries must be non-empty relative paths.');
  }

  const source = resolve(sourceRoot, entry);
  const inside = relative(sourceRoot, source);
  if (!inside || inside.startsWith(`..${sep}`) || inside === '..' || isAbsolute(inside)) {
    throw new Error(`Manifest path escapes data/processed/web: ${entry}`);
  }
  return source;
}

const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
if (!manifest || !Array.isArray(manifest.files) || manifest.files.some((entry) => typeof entry !== 'string')) {
  throw new Error('data-manifest.json must contain a string array named "files".');
}
if (new Set(manifest.files).size !== manifest.files.length) {
  throw new Error('data-manifest.json contains duplicate paths.');
}

const files = await Promise.all(manifest.files.map(async (entry) => {
  const source = safeSourcePath(entry);
  let metadata;
  try {
    metadata = await stat(source);
  } catch {
    throw new Error(`Manifest file is missing: ${entry}`);
  }
  if (!metadata.isFile()) throw new Error(`Manifest entry is not a file: ${entry}`);
  return { entry, source };
}));

await rm(destinationRoot, { recursive: true, force: true });
await mkdir(destinationRoot, { recursive: true });
for (const { entry, source } of files) {
  const destination = resolve(destinationRoot, entry);
  await mkdir(dirname(destination), { recursive: true });
  await cp(source, destination, { errorOnExist: true, force: false });
}

console.log(`Prepared ${files.length} allowlisted publication file(s).`);
{% endraw %}
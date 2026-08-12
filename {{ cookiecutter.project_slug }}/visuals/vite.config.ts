import { svelte } from '@sveltejs/vite-plugin-svelte';
import { resolve } from 'node:path';
import { defineConfig } from 'vite';

const tagPrefix = 'sz-{{ cookiecutter.project_slug }}-';

export default defineConfig({
  base: './',
  plugins: [
    svelte({
      dynamicCompileOptions: ({ filename }) => ({
        css: 'injected',
        customElement: filename.includes('/src/elements/')
      })
    })
  ],
  publicDir: 'static',
  build: {
    outDir: '../output/interactives/{{ cookiecutter.project_slug }}',
    emptyOutDir: true,
    lib: {
      entry: resolve(import.meta.dirname, 'src/register.ts'),
      formats: ['es'],
      fileName: () => 'story.js'
    }
  },
  define: {
    __SZ_TAG_PREFIX__: JSON.stringify(tagPrefix)
  }
});

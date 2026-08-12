export default {
  compilerOptions: {
    runes: ({ filename }) => filename.split(/[/\\]/).includes('node_modules') ? undefined : true,
    // Enables custom-element metadata during `svelte-check`; Vite limits emitted custom elements to src/elements/.
    customElement: true
  }
};

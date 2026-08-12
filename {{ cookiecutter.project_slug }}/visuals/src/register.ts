{% raw %}import ExampleChartElement from './elements/ExampleChartElement.svelte';

const exampleTag = `${__SZ_TAG_PREFIX__}example`;

if (!customElements.get(exampleTag)) {
  customElements.define(exampleTag, ExampleChartElement.element as CustomElementConstructor);
}
{% endraw %}
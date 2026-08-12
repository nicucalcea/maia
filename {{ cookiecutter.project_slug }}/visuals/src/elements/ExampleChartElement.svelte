{% raw %}<svelte:options
  customElement={{
    shadow: 'open',
    props: {
      dataUrl: { attribute: 'data-url', type: 'String' },
      locale: { type: 'String' },
      data: { type: 'Array' }
    }
  }}
/>

<script lang="ts">
  import ExampleChart, { type Datum } from '../graphics/ExampleChart.svelte';

  type Props = {
    dataUrl?: string;
    locale?: string;
    data?: Datum[];
  };

  const fallback: Datum[] = [
    { period: 1, value: 4 },
    { period: 2, value: 9 },
    { period: 3, value: 6 },
    { period: 4, value: 14 }
  ];

  let { dataUrl = '', locale = 'en', data = fallback }: Props = $props();
  let remoteData = $state.raw<Datum[]>();
  let error = $state('');
  let chartData = $derived(remoteData ?? data);

  function isData(value: unknown): value is Datum[] {
    return Array.isArray(value) && value.every((row) =>
      typeof row === 'object' && row !== null &&
      Number.isFinite((row as Datum).period) && Number.isFinite((row as Datum).value)
    );
  }

  $effect(() => {
    remoteData = undefined;
    error = '';
    if (!dataUrl) return;

    const controller = new AbortController();
    fetch(new URL(dataUrl, document.baseURI), { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      })
      .then((value: unknown) => {
        if (!isData(value)) throw new Error('Invalid chart data');
        remoteData = value;
      })
      .catch((reason: unknown) => {
        if (!controller.signal.aborted) {
          error = reason instanceof Error ? reason.message : 'Load failed';
        }
      });

    return () => controller.abort();
  });
</script>

<div class="element" part="figure">
  <ExampleChart data={chartData} {locale} />
  {#if error}<p role="alert">Could not load data: {error}</p>{/if}
</div>

<style>
  :host {
    display: block;
    color: var(--sz-foreground, #1b1c19);
    background: var(--sz-background, #fbf9f4);
  }

  .element {
    padding: var(--sz-spacing-3, 1rem);
  }

  p {
    color: var(--sz-accent, #9f1853);
    font-family: var(--sz-font-sans, 'Work Sans', system-ui, sans-serif);
  }
</style>
{% endraw %}
{% raw %}<script lang="ts">
  import { LayerCake, Svg } from 'layercake';
  import { AccessibleTable, Figure, Line, type TableColumn } from '@samizdata/graphics';

  export type Datum = { period: number; value: number };

  type Props = {
    data: Datum[];
    locale?: string;
  };

  const columns: TableColumn<Datum>[] = [
    { key: 'period', label: 'Period' },
    { key: 'value', label: 'Value' }
  ];

  let { data, locale = 'en' }: Props = $props();
  let formatter = $derived(new Intl.NumberFormat(locale));
</script>

<Figure
  title="Example chart"
  description="Replace this composition with the story's reporting and chart configuration."
  source="Example data."
>
  {#snippet children({ labelledBy, describedBy })}
    <div class="chart" part="chart">
      <LayerCake {data} x="period" y="value" padding={{ top: 12, right: 12, bottom: 12, left: 12 }}>
        <Svg {labelledBy} {describedBy}>
          <Line />
        </Svg>
      </LayerCake>
    </div>
  {/snippet}
  {#snippet alternative()}
    <AccessibleTable
      rows={data}
      columns={columns.map((column) => column.key === 'value'
        ? { ...column, format: (value) => formatter.format(Number(value)) }
        : column)}
      caption="Example chart data"
      rowKey={(datum) => datum.period}
    />
  {/snippet}
</Figure>

<style>
  .chart {
    height: 18rem;
    min-width: 0;
    background: var(--sz-surface, #fff);
  }
</style>
{% endraw %}
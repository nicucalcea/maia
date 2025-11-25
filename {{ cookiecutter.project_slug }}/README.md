# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Setup instructions

{% if cookiecutter.notebook == 'Quarto' %}To render the Quarto notebook, run `quarto render` on your `.qmd` file in `notebooks`.
{% elif cookiecutter.notebook == 'Jupyter' %}To render the Jupyter Notebooks using Quarto, run `quarto render` on your `.ipynb` file in `notebooks`.
{% elif cookiecutter.notebook == 'Observable' %}To build the Observable Notebook run `npm run dev` to preview or `npm run build` to build it to the `output` directory.
{% endif %}

## Tracking time

This project uses [klog](https://klog.jotaen.net/) to track time spent on it.

You can start tracking time by running:

```bash
klog start hours.klg
```

To stop tracking time, run:

```bash
klog stop hours.klg
```

Or to take a break:

```bash
klog pause --summary 'Lunch break' hours.klg
```
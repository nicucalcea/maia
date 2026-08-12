A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for data journalism projects. Named after the Romanian word for sourdough starter.

## Creating a project

Navigate to the directory where you want to create a new project and run the following command.

``` bash
uvx cookiecutter gh:nicucalcea/maia
```

## Optional interactive graphics

Choose `Svelte + Layer Cake` at the `interactive` prompt to generate a `visuals/` workspace. It pins an exact `@samizdata/graphics` version or Git tag, builds story-specific Svelte custom elements into one portable relative ES-module bundle, and copies only data explicitly allowlisted from `data/processed/web/`.

The default `None` choice preserves the existing generated project. The graphics package currently defaults to the anticipated first tag, `github:samizdata-co/graphics#v0.0.1`; create and push that tag before using the default in production, or enter another explicitly reviewed tag.

Template checks can be run with `uv run -m unittest discover -s tests -v`. To also install, type-check and build the generated interactive workspace against a local graphics checkout, run:

```bash
SAMIZDATA_GRAPHICS_PACKAGE=file:/path/to/graphics MAIA_TEST_FULL_BUILD=1 \
  uv run -m unittest discover -s tests -v
```

## Quarto branding

Generated projects now include a SAMIZDATA `brand.yml` and matching PDF style files (`samizdata-pdf.tex`, `samizdata-before-body.tex`).

Generated projects also include `logo.png` in the project root, picked up automatically by the PDF template.

## Structure

Here's the current folder structure.

```         
.
├── data
│   ├── handmade                        # data created by hand
│   ├── interim                         # various bits and pieces, i.e. for transfer between tools
│   ├── processed                       # final datasets
│   └── raw                             # raw, immutable data
├── etl                                 # scripts to clean and process data
├── notebooks                           # analysis of already cleaned data
│   └── analysis.ext                    # Quarto, Jupyter or Observable notebook
├── output                              # publishable notebooks, dashboards, charts, stories, etc.
├── visuals                             # optional Svelte + Layer Cake custom-element workspace
├── _quarto.yml                         # Quarto config
├── .gitignore                          # files to be ignored by version control
├── .Rprofile                           # (R) environment variables
├── {{cookiecutter.project_slug}}.Rproj # (R) RStudio project
├── package.json                        # (Observable) run scripts
├── README.md                           # boilerplate with instructions, sources, etc
└── story.md                            # article
```

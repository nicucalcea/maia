A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for data journalism projects. Named after the Romanian word for sourdough starter.

## Creating a project

Navigate to the directory where you want to create a new project and run the following command.

``` bash
uvx cookiecutter gh:nicucalcea/maia
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
├── _quarto.yml                         # Quarto config
├── .gitignore                          # files to be ignored by version control
├── .Rprofile                           # (R) environment variables
├── {{cookiecutter.project_slug}}.Rproj # (R) RStudio project
├── package.json                        # (Observable) run scripts
├── README.md                           # boilerplate with instructions, sources, etc
└── story.md                            # article
```

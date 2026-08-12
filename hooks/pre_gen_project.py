import re
import sys

SLUG_REGEX = r'^[a-zA-Z0-9][-_a-zA-Z0-9]+$'
slug = '{{ cookiecutter.project_slug }}'
graphics_package = '{{ cookiecutter.graphics_package }}'

if not re.match(SLUG_REGEX, slug):
    print(f'ERROR: {slug} is not a valid project slug!')
    sys.exit(1)

if '{{ cookiecutter.interactive }}' == 'Svelte + Layer Cake':
    unpinned = {
        '@samizdata/graphics',
        'latest',
        'github:samizdata-co/graphics',
        'git+https://github.com/samizdata-co/graphics.git',
    }
    if (
        graphics_package in unpinned
        or graphics_package.endswith('#main')
        or graphics_package.endswith('#master')
        or graphics_package.startswith('^')
        or graphics_package.startswith('~')
        or graphics_package.startswith('>')
        or '*' in graphics_package
    ):
        print('ERROR: graphics_package must pin an exact version or Git tag!')
        sys.exit(1)
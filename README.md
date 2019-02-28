# dash-bootstrap-css

This repo contains [Bootstrap v4][bsv4] compatible stylesheets for use with
[Plotly Dash][pd]. Specifically it extends Bootstrap and Bootswatch to add
consistent styling to [*dash-core-components*][dcc] when using
[*dash-bootstrap-components*][dbc].

**Note:** This project is still in its infancy, and so far only styles for
`dcc.Dropdown` have been added, and not extensively tested. Use with caution.

## Getting started

Simply download the stylesheet of interest from `dist/` and link it in your
Dash app. See the [Dash documentation][dash-docs] for instructions on how to do
this.

## Building

The stylesheets are compiled from the SASS source files available in `scss/`.
The simplest way to build the CSS yourself is to first install dependencies
with `npm`:

```
npm install
```

The build task is managed by Grunt. You can either run

```
npm run grunt -- build
```

to build all themes or

```
npm run grunt -- build:<theme>
```

to build a specific theme. If you have `grunt-cli` installed globally, you could
alternatively use a command like

```
grunt build:<theme>
```

[bsv4]: https://getbootstrap.com
[pd]: https://plot.ly/dash
[dash-docs]: https://dash.plot.ly/external-resources
[dcc]: https://github.com/plotly/dash-core-components
[dbc]: https://github.com/facultyai/dash-bootstrap-components

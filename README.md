# dash-bootstrap-css

This repo contains [Bootstrap v4][bsv4] compatible stylesheets for use with
[Plotly Dash][pd]. Specifically it extends Bootstrap and Bootswatch to add
consistent styling to [*dash-core-components*][dcc] when using
[*dash-bootstrap-components*][dbc].

**Note:** This repository is experimental, and I might break things, or fail to
keep up with new releases of Dash. Please use with caution, and open an issue if
you discover something that doesn't work as you would expect.

## Getting started

Simply download the stylesheet of interest from `dist/` and link it in your
Dash app. See the [Dash documentation][dash-docs] for instructions on how to do
this. Each Dash Bootstrap CSS stylesheet extends either Bootstrap or the
Bootswatch theme of the same name and can be used as a drop in replacement. The
additional styling for Dash components only applies to children of a component
with the class `dash-bootstrap` applied. This allows you to ensure that Dash
Bootstrap CSS will not interfere with existing styles outside of the children
of that component.

For example, to style a `dcc.Dropdown` with Dash Bootstrap CSS, you would
simply do something like

```python
app.layout = html.Div(dcc.Dropdown(options=[...]), className="dash-bootstrap")
```

Each sheet currently supports `dcc.DatePickerSingle`, `dcc.DatePickerRange`,
`dcc.Dropdown`, `dcc.Slider`, and `dcc.RangeSlider`.

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

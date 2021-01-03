from datetime import date

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

EXPLAINER = """This is a simple demo of the custom stylesheets. The default
styles in `dash-core-components` are overridden by adding one of the custom
stylesheets to the `assets` folder, and adding the class `dash-bootstrap` to
any parent element of the components you want to restyle. You can see the
effect of applying the custom styles using the below toggle.
"""


# note we do not add dbc.themes.BOOTSTRAP under external_stylesheets
# the bootstrap styles are loaded from our custom stylesheet in assets
app = dash.Dash()

app.layout = dbc.Container(
    [
        html.H1("dash-bootstrap-css example"),
        dcc.Markdown(EXPLAINER),
        dbc.Checklist(
            options=[{"label": "Activate custom styles", "value": 1}],
            value=[1],
            id="toggle",
            switch=True,
        ),
        html.Hr(),
        dbc.Card(
            [
                html.H4("Dropdown", className="card-title"),
                dcc.Dropdown(
                    options=[
                        {"label": f"Option {i}", "value": i} for i in range(10)
                    ]
                ),
            ],
            body=True,
            className="mb-3",
        ),
        dbc.Card(
            [
                html.H4("Dropdown - multi", className="card-title"),
                dcc.Dropdown(
                    options=[
                        {"label": f"Option {i}", "value": i} for i in range(10)
                    ],
                    multi=True,
                ),
            ],
            body=True,
            className="mb-3",
        ),
        dbc.Card(
            [
                html.H4("Slider", className="card-title"),
                dcc.Slider(
                    min=0,
                    max=20,
                    step=0.5,
                    value=10,
                    marks={i: {"label": str(i)} for i in range(0, 21, 4)},
                ),
            ],
            body=True,
            className="mb-3",
        ),
        dbc.Card(
            [
                html.H4("RangeSlider", className="card-title"),
                dcc.RangeSlider(
                    min=0,
                    max=20,
                    step=0.5,
                    value=[5, 15],
                    marks={i: {"label": str(i)} for i in range(0, 21, 4)},
                ),
            ],
            body=True,
            className="mb-3",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("DatePickerSingle", className="card-title"),
                    dcc.DatePickerSingle(
                        min_date_allowed=date(1995, 8, 5),
                        max_date_allowed=date(2017, 9, 19),
                        initial_visible_month=date(2017, 8, 5),
                    ),
                ],
            ),
            className="mb-3",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H4("DatePickerRange", className="card-title"),
                    dcc.DatePickerRange(
                        min_date_allowed=date(1995, 8, 5),
                        max_date_allowed=date(2017, 9, 19),
                        initial_visible_month=date(2017, 8, 5),
                    ),
                ]
            ),
            className="mb-3",
        ),
    ],
    id="container",
    style={"marginBottom": "300px", "marginTop": "20px"},
    # in most apps you won't want to toggle the className with a callback
    # simply set the className manually here
    # className="dash-bootstrap",
)


# this callback is use to toggle the "dash-bootstrap" class so you can see
# the effect of the custom stylesheets when running the example app.
@app.callback(Output("container", "className"), Input("toggle", "value"))
def toggle_classname(value):
    if 1 in value:
        return "dash-bootstrap"
    return ""


if __name__ == "__main__":
    app.run_server(debug=True)

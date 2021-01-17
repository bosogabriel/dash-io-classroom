import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import Input, Output, State

#LOGO = "./assets/LogoIO.JPG"
LOGO = "./assets/combine_images.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Inicio", href="/home"))

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Temas", header=True),
        dbc.DropdownMenuItem("Apps 1", href="/apps/app1"),
        dbc.DropdownMenuItem("Probabilidad y Estadistica", href="/apps/A_probStat"),
        dbc.DropdownMenuItem("Simulacion", href="/apps/B_simulation"),
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    label="More pages",
)
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
#                        dbc.Col(html.Img(src=LOGO, height="50px")),
                        dbc.Col(dbc.NavbarBrand("IO", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="primary",
    dark=True,
)
#Top Navbar - Subject Selector
# navbar = dbc.NavbarSimple(
#     children=[
#         html.A(
#         # Use row and col to control vertical alignment of logo / brand
#         dbc.Row(
#             [
#                 dbc.Col(html.Img(src=LOGO, height="40px")),
#                 dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
#             ],
#             align="left",
#             no_gutters=True,
#         ),
#         href="/home",
#         ),
#         dbc.NavItem(dbc.NavLink("Inicio", href="/home")),
#         dbc.DropdownMenu(
#             children=[
#                 dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Apps 1", href="/apps/app1"),
#                 dbc.DropdownMenuItem("Probabilidad y Estadistica", href="/apps/A_probStat"),
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
#     ],
#     color="primary",
#     dark=True,
# )

# Left Nav Bar - Topic Selector
nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Active", active=True, href="#")),
        dbc.NavItem(dbc.NavLink("A link", href="#")),
        dbc.NavItem(dbc.NavLink("Another link", href="#")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
    ],
    vertical="md",
    navbar = True
    )

# Topic XXXX
Topic_X = "Este es el topico 1"

# Page Layout
layout = html.Div(
    [
        dbc.Row(dbc.Col(html.Div(navbar))),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(nav),
                    width=2,
                    className="navbar navbar-expand-md navbar-light navbar-dark bg-secondary",
                    style={"height":"100vh","align-items":"start"}
),
                dbc.Col(html.Div(Topic_X)),
            ]
        ),
    ]
)

#html.Div([html.Div([navbar]),
#     dcc.Link('Go to App 1', href='/apps/app1'),
#     dcc.Link('Go to App 2', href='/apps/app2'),
#     html.Label('Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Multi-Select Dropdown'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value=['MTL', 'SF'],
#         multi=True
#     ),

#     html.Label('Radio Items'),
#     dcc.RadioItems(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value='MTL'
#     ),

#     html.Label('Checkboxes'),
#     dcc.Checklist(
#         options=[
#             {'label': 'New York City', 'value': 'NYC'},
#             {'label': u'Montréal', 'value': 'MTL'},
#             {'label': 'San Francisco', 'value': 'SF'}
#         ],
#         value=['MTL', 'SF']
#     ),

#     html.Label('Text Input'),
#     dcc.Input(value='MTL', type='text'),

#     html.Label('Slider'),
#     dcc.Slider(
#         min=0,
#         max=9,
#         marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
#         value=5,
#     ),
# ], style={'columnCount': 2})


import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from typing import List

# Left Nav Bar - Topic Selector
def sideNavBar(subject: str,topics: List[str],selected: str):
    navItems=[dbc.NavItem(dbc.NavLink(topic, active=True, href=subject+'/'+topic)) if topic==selected else dbc.NavItem(dbc.NavLink(topic, active=False, href=subject+'/'+topic)) for topic in topics]
    nav = dbc.Nav(navItems,vertical="md",navbar = True)
    return nav

# Main Nav Bar + Layout
def pageNavBar(page_content,side_nav=False,side_nav_content=None):
    """"""
    # Home link
    nav_item = dbc.NavItem(dbc.NavLink("Inicio", href="/home"))

    # Dropdown for subjects
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Temas", header=True),
            dbc.DropdownMenuItem("Apps 1", href="/apps/app1"),
            dbc.DropdownMenuItem("Probabilidad y Estadistica", href="/apps/A_probStat"),
            dbc.DropdownMenuItem("Entry 1"),
            dbc.DropdownMenuItem("Entry 2"),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Entry 3"),
        ],
        nav=True,
        in_navbar=True,
        label="More pages",
    )
    # Navbar core design
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
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
    # Structure page with/without side navbar
    if side_nav:
        structure = html.Div(
        [
            dbc.Row(dbc.Col(html.Div(navbar))),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(side_nav_content),
                        width=2,
                        className="navbar navbar-expand-md navbar-light navbar-dark bg-secondary",
                        style={"height":"100vh","align-items":"start"}
                    ),
                    dbc.Col(html.Div(page_content)),
                ]
            ),
        ]
        )
    else:
        structure = html.Div(
        [
            dbc.Row(dbc.Col(html.Div(navbar))),
            dbc.Row(
                [
                    dbc.Col(html.Div(page_content)),
                ]
            ),
        ]
        )
    return structure

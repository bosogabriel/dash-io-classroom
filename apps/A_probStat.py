import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components.BaseLayout import pageNavBar,sideNavBar
from app import app

topics=['Probabilidades']
base_selection='Probabilidades'
layout = pageNavBar(base_selection,side_nav_content=sideNavBar('B_simulation',topics=topics,selected=base_selection))
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components.BaseLayout import pageNavBar,sideNavBar
from app import app

topics=['Montecarlo']
base_selection='Montecarlo'
layout = pageNavBar(base_selection)


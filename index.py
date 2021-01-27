import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import home, app1, app2, A_probStat, B_simulation, C_markov, D_queues, \
    E_critPath, F_linProg, G_inventory, H_transport


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home.layout
    elif pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/A_probStat':
        return A_probStat.layout
    elif pathname == '/apps/B_simulation':
        return B_simulation.layout
    elif pathname == '/apps/C_markov':
        return C_markov.layout
    elif pathname == '/apps/D_queues':
        return D_queues.layout
    elif pathname == '/apps/E_critPath':
        return E_critPath.layout
    elif pathname == '/apps/F_linProg':
        return C_markov.layout
    elif pathname == '/apps/G_inventory':
        return C_markov.layout
    elif pathname == '/apps/H_transport':
        return C_markov.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
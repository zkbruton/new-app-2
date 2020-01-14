import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from dash.dependencies import Input, Output

zika = pd.read_excel('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx')


app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
        html.H2('Zika Explorer'),
        dcc.Dropdown(
                    id = 'countryPicker',
                    options = [{'label': i, 'value': i} for i in zika['integer'].unique()],
                    multi = True,
                    value = zika['integer'].unique())
])

if __name__ == '__main__':
    app.run_server(debug=True)

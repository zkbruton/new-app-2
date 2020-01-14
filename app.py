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

zika = pd.read_csv('https://raw.githubusercontent.com/charleyferrari/bnext-crossfilter/master/zika.csv').drop('X', axis = 1)

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
        html.H2('Zika Explorer')
])

if __name__ == '__main__':
    app.run_server(debug=True)


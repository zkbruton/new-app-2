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

df_spt=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/df_spt.csv',index_col=0)
repair_data=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/repair_data.csv',index_col=0)
repair_data_copy=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/repair_data_copy.csv',index_col=0)
nb_data=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/nb_data.csv',index_col=0)
nb_data_copy=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/nb_data_copy.csv',index_col=0)
con_data=pd.read_csv('https://raw.githubusercontent.com/zkbruton/csv-files/master/con_data.csv',index_col=0)
df_spt['Date']=pd.to_datetime(df_spt['Date'])
repair_data['Date']=pd.to_datetime(repair_data['Date'])
repair_data_copy['Date']=pd.to_datetime(repair_data_copy['Date'])
nb_data['Date']=pd.to_datetime(nb_data['Date'])
nb_data_copy['Date']=pd.to_datetime(nb_data_copy['Date'])

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
        html.H2('Testing Grounds')
])

if __name__ == '__main__':
    app.run_server(debug=True)


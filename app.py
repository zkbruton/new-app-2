import plotly.plotly as plotly
#import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
#import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
#import os
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
        html.H2('Testing Grounds'),
        dt.DataTable(id='table',
                   style_table={'overflowX':'scroll'},
                   style_cell={'minWidth':'45px'},
                   style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
                   style_data_conditional=[{'if':{'row_index':'odd'},
                                            'backgroundColor':'#f8f8f8'}],
                   columns=[{"name": i, "id": i} for i in df_spt.columns],
                   style_as_list_view=True,
                   data=df_spt.head(10).to_dict('records'))
])

if __name__ == '__main__':
    app.run_server(debug=True)


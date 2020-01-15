#import plotly.plotly as plotly
#import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import time
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

#Unique Customer Names
cust_names=pd.concat([con_data['Customer'],repair_data['Customer'],nb_data['Customer']]).unique()
cust_names=list(cust_names)
ll=[None]*len(cust_names)
for i in range(len(cust_names)):
    ll[i]={'label':cust_names[i],'value':cust_names[i]}

#Dash App creation
    
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets1 = ['https://codepen.io/zkbruton/pen/JjovEXN.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets1)

#app = dash.Dash(__name__)
server = app.server
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

colors = {
    'background': '#f1f1f1',
    'text': '#7FDBFF'
}

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'backgroundColor': '#f8f8f8'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'backgroundColor': '#f8f8f8',
    'fontWeight': 'bold'
}


    
#daterange = pd.date_range(start='2016',end='2020',freq='W')

def unixTimeMillis(dt):
    ''' Convert datetime to unix timestamp '''
    return int(time.mktime(dt.timetuple()))

def unixToDatetime(unix):
    ''' Convert unix timestamp to datetime. '''
    return pd.to_datetime(unix,unit='s')

def getMarks(begin, ending, Nth=40):
    ''' Returns the marks for labeling. 
        Every Nth value will be used.
    '''
    daterange = pd.date_range(start=begin,end=ending, freq='W')
    result = {}
    for i, date in enumerate(daterange):
        if(i%Nth == 1):
            # Append value to dict
            result[unixTimeMillis(date)] = str(date.strftime('%Y-%m-%d'))

    return result
#app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

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


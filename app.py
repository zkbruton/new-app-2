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

app.layout = html.Div(style={'backgroundColor': colors['background'],'width':'100%','height':'100%','top':'0px','left':'0px','z-index':'1000','position':'sticky'}, children=[
    html.H4(children='Commercial Dashboard',style={'textAlign':'center'}),

    html.H5(children='''
        Dashboard for Pricing and Order Information from the UK
    ''',style={'textAlign':'center'}),
   
#    html.Br(),         
    
    html.Div([
        html.Div([
                html.Div([
                         html.H6('Filter by Part Number'),
                         dcc.Input(id='my-id', value='Type PN here', type='text'),
                         html.Div(id='my-div')
                         ],
                className='four columns',
                style={'textAlign':'center'}),                
#                style={'width': '48%', 'display': 'inline-block'}),
                
                html.Div([
                        html.H6('Filter by Customer'),
                        dcc.RadioItems(id='radio_1',
                                options=[
                                        {'label':'All','value':'All'},
                                        {'label':'Big 5','value':'Big 5'},
                                        {'label':'Customize','value':'Customize'}
                                        ],
                                value='All',
                                labelStyle={'display': 'inline-block', 'margin-right': 10}),
                        dcc.Dropdown(id='customer', 
                                     options=ll,
                                     multi=True,
                                     placeholder='Select Customers',
                                     style={'textAlign':'center'}),
#                        html.Div(id='customer-name')
                        ],
                className='eight columns',
                style={'textAlign':'center'})                
#                style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
                ],className='row'),
        
        
        
        html.Br(),
        html.Div(id='output-container-range-slider',style={'text-align':'center'}),
        html.Div([
                dcc.RangeSlider(
                    id='year_slider',
                    min = unixTimeMillis(df_spt['Date'].min()),
                    max = unixTimeMillis(df_spt['Date'].max()),
                    value = [unixTimeMillis(df_spt['Date'].min()),
                             unixTimeMillis(df_spt['Date'].max())],
                    marks=getMarks(df_spt['Date'].min(),
                                df_spt['Date'].max()))
                    ],
                    style={'margin-left':'auto','margin-right':'auto','width':'70%'}),
        html.Br(),
                ],
#                    style={'backgroundColor':'#f8f8f8','border-style':'solid','border-color':'rgb(211,211,211)','border-width':'2px','border-radius':'5px','padding':'5px'}),
                    style={'margin-left':'auto','margin-right':'auto','width':'80%','backgroundColor':'#f8f8f8','box-shadow':'2px 2px #c9c9c9','padding':'5px','border-radius':'5px'}),

    html.Br(),
    dcc.Tabs([
            dcc.Tab(label='Sell Price Tracker',value='tab1',children=[
                html.Div([
                    html.Div([html.H4('Table'),dt.DataTable(id='table',
#                                                   style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0,},
                                                   style_table={'overflowX':'scroll'},
                                                   style_cell={'minWidth':'45px'},
                                                   style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
                                                   style_data_conditional=[{'if':{'row_index':'odd'},
                                                                            'backgroundColor':'#f8f8f8'}],
                                                   columns=[{"name": i, "id": i} for i in df_spt.columns],
#                                                   columns=['Part Number','Quote','Unit Cost Price','Unit Sell Price','CM','Date','Qty'],
                                                   style_as_list_view=True,
                                                   data=df_spt.head(10).to_dict('records'))
                            ], style={'text-align':'center'}, className='six columns'),
                    html.Div([html.H4('Graph'),dcc.Graph(id='g1', figure={})], className='six columns'),
                        ],style={'text-align':'center','padding': '8px'},className="row"),
                    ],style=tab_style,selected_style=tab_selected_style),
            dcc.Tab(label='Cost Model Data',value='tab2',children=[
                    dcc.Tabs(id='subtabsCM',value='subtabsSM',children=[  
                        dcc.Tab(label='Repair Work',
                                children=[html.Div([
                                            html.Div([html.H4('Table'),
                                                      dt.DataTable(id='table_repair',
                #                                                   style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0,},
                                                                   style_table={'overflowX':'scroll'},
                                                                   row_selectable="single",
                                                                   selected_rows=[],
                                                                   style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
                                                                   style_data_conditional=[{'if':{'row_index':'odd'},
                                                                                            'backgroundColor':'#f8f8f8'}],
                                                                   style_cell={'minWidth':'45px'},
                                                                   columns=[{"name": i, "id": i} for i in repair_data.columns],
#                                                                   style_as_list_view=True,
                                                                   data=repair_data.head(10).to_dict('records'))
                                                    ])],style={'padding':'8px'}),
                                          html.Div([
                                            html.Div([html.H4('Graph'),dcc.Graph(id='g_repair', figure={})], className='six columns'),
                                            html.Div([html.H4('Donut Chart'),dcc.Graph(id='g_donut_repair', figure={})], className='six columns'),
                                                ],style={'padding':'8px'},className="row"),
                                            ],style=tab_style,selected_style=tab_selected_style
                                ),
                        dcc.Tab(label='New Build',
                                children=[html.Div([
                                            html.Div([html.H4('Table'),
                                                      dt.DataTable(id='table_nb',
                #                                                   style_cell={'overflow': 'hidden','textOverflow': 'ellipsis','maxWidth': 0,},
                                                                   style_table={'overflowX':'scroll'},
                                                                   row_selectable="single",
                                                                   selected_rows=[],
                                                                   style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
                                                                   style_data_conditional=[{'if':{'row_index':'odd'},
                                                                                            'backgroundColor':'#f8f8f8'}],
                                                                   style_cell={'minWidth':'45px'},
                                                                   columns=[{"name": i, "id": i} for i in nb_data.columns],
                                                                   data=nb_data.head(10).to_dict('records'))
                                                    ])],style={'padding':'8px'}),
                                          html.Div([
                                            html.Div([html.H4('Graph'),dcc.Graph(id='g_nb', figure={})], className='six columns'),
                                            html.Div([html.H4('Donut Chart'),dcc.Graph(id='g_donut_nb', figure={})], className='six columns'),
                                                ],style={'padding':'8px'},className="row"),
                                            ],style=tab_style,selected_style=tab_selected_style
                                ),
                        ]),
                ],style=tab_style,selected_style=tab_selected_style),
            dcc.Tab(label='Contract Information',value='tab3',children=[
                    html.Div([html.H4('Table'),
                              dt.DataTable(id='table_contract',
                                           style_table={'overflowX':'scroll'},
                                           row_selectable="single",
                                           selected_rows=[],
                                           style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
                                           style_data_conditional=[{'if':{'row_index':'odd'},
                                                                    'backgroundColor':'#f8f8f8'}],
                                           style_cell={'minWidth':'45px'},
                                           columns=[{"name": i, "id": i} for i in con_data.columns],
                                           data=con_data.head(10).to_dict('records'))
                            ],style={'padding':'8px'})
                    ],
                    style=tab_style,selected_style=tab_selected_style),
            ]),

    html.Div(id='tabs-content')
])

if __name__ == '__main__':
    app.run_server(debug=True)


#PREVIOUSLY: HOW USERS CAN INTERACT
# YOU NEED PANDAS DATAREADER FOR THIS (WHICH I DIDNT HAVE PREVIOUSLY SO I HAD TO GET IT) THIS IS FOR GETTING LIVE DATA FROM THE INTERNET

#HOWEVER FOR MY PURPOSE SINCE I HAVE TO WORK WITH THE COVID DATA SET, I AM JUST WORKING WITH PANDAS AND STUFF I HAVE ALREADY WORKED ON

#pip install pandas-datareader

#Pythonprogramming.net has the code for finance data... I am going to try it with covid data


#Important Bit of Knowledge required is how to work with wrapper and then making use of dash core components for displaying graph

import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Death/Positive/Cured/Active:
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    #start = datetime.datetime(2015, 1, 1)
    #end = datetime.datetime.now()
    india_data_url = "https://www.mohfw.gov.in/data/datanew.json"
    df = pd.read_json(india_data_url)
    #df.reset_index(inplace=True)
    df.set_index('state_name', inplace=True)
    df.drop(columns='sno', axis=1, inplace=True)

    if input_data == 'Death':
        val = 'new_death'
    elif input_data == 'Active':
        val = 'new_active'
    elif input_data == 'Positive':
        val = 'new_positive'
    elif input_data == 'Cured':
        val = 'new_cured'

    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df[val], 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
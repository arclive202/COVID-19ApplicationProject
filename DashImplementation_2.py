#HOW USERS CAN INTERACT
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', value='Enter something here!', type='text'),
    html.Div(id='output')
])

#DECORATOR EXPLAINER URL: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')] #SIMULTANEOUSLY UPDATING INPUT AND OUTPUT
)
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)


if __name__ == '__main__':
    app.run_server(debug=True)
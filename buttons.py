# -*- coding: utf-8 -*-
"""
Created: March 2021

@author: Ryan Clement
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Button Examples'),
    html.Br(),
    html.H2('Example #1'),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-text', n_clicks=0),
    html.Div(id='result-text'),
    html.Br(),
    html.H2('Example #2'),
    html.Div([
        html.Button(
            'Button 1', 
            id='btn-1', 
            n_clicks=0,
            style={'background-color':'red',
                   'color':'white'}
            ),
        html.Button(
            'Button 2', 
            id='btn-2', 
            n_clicks=0,
            style={'background-color':'white'}
            ),
        html.Button(
            'Button 3', 
            id='btn-3', 
            n_clicks=0,
            style={'background-color':'blue',
                   'color':'white'}
            ),
        html.Div(id='container-button-timestamp')
        ])
    ])


@app.callback(
    Output('result-text', 'children'),
    [Input('submit-text', 'n_clicks')],
    [State('input-on-submit', 'value')]
    )
def update_output(n_clicks, value):
    if n_clicks == 0:
        return 'Enter text and click submit button.'
    else:
        return 'The input value was "{}". The button has been clicked {} time(s).'.format(
            value,
            n_clicks
        )

@app.callback(Output('container-button-timestamp', 'children'),
              Input('btn-1', 'n_clicks'),
              Input('btn-2', 'n_clicks'),
              Input('btn-3', 'n_clicks'))
def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-1' in changed_id:
        msg = 'Button 1 clicked'
    elif 'btn-2' in changed_id:
        msg = 'Button 2 clicked'
    elif 'btn-3' in changed_id:
        msg = 'Button 3 clicked'
    else:
        msg = 'Please click one of the buttons.'
    return html.Div(msg)


if __name__ == '__main__':
    app.run_server(debug=True)
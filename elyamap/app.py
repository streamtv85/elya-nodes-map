import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json

from datetime import datetime as dt

import pandas as pd

from elyamap import geoip

# http://139.59.149.46:57778/peers
# http://139.59.149.46:57778/getinfo


from cachetools import cached, TTLCache

refresh_interval = 10  # in seconds
cache = TTLCache(50, 600)  # TTL is 10 minutes

app = dash.Dash(__name__)


def serve_layout():
    return html.Div(children=[

        html.Div(id='temp-value'
                 , style={'display': 'none'}
                 ),
        dcc.Interval(
            id='timer',
            interval=refresh_interval * 1000,  # in milliseconds
            n_intervals=0
        )
    ],
        className='container')


# put layout to a separate function so that it is refreshed on page reload
app.layout = serve_layout
app.title = "Elya Coin World Map"


@app.callback(Output('books', 'value'), [Input('books', 'options')])
def update_markets_value(available_options):
    return available_options[0]['value']


if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='0.0.0.0')

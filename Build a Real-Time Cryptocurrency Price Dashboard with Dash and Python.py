import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import requests

app = dash.Dash(__name__)

# Store data globally
data_store = {
    'Time': [],
    'BTC': [],
    'ETH': [],
    'LTC': []
}

app.layout = html.Div(children=[
    html.H1(children='Real-Time Cryptocurrency Price Dashboard'),

    dcc.Dropdown(
        id='crypto-dropdown',
        options=[
            {'label': 'Bitcoin', 'value': 'BTC'},
            {'label': 'Ethereum', 'value': 'ETH'},
            {'label': 'Litecoin', 'value': 'LTC'}
        ],
        value='BTC',  # Default value
        clearable=False,
        style={'width': '50%'}
    ),

    dcc.Graph(
        id='price-graph'
    ),

    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # in milliseconds (1 minute)
        n_intervals=0
    )
])

@app.callback(
    Output('price-graph', 'figure'),
    [Input('interval-component', 'n_intervals'), Input('crypto-dropdown', 'value')]
)
def update_graph(n, selected_crypto):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # Print the API response for debugging
    print("API response:", data)

    if 'error_code' in data and data['error_code'] == 429:
        print("Rate limit exceeded. Waiting for a while before retrying...")
        return dash.no_update

    try:
        btc_price = data['bitcoin']['usd']
        eth_price = data['ethereum']['usd']
        ltc_price = data['litecoin']['usd']
        current_time = pd.Timestamp.now()

        # Append new data
        data_store['Time'].append(current_time)
        data_store['BTC'].append(btc_price)
        data_store['ETH'].append(eth_price)
        data_store['LTC'].append(ltc_price)

        # Limit data to the last 100 points
        if len(data_store['Time']) > 100:
            data_store['Time'] = data_store['Time'][-100:]
            data_store['BTC'] = data_store['BTC'][-100:]
            data_store['ETH'] = data_store['ETH'][-100:]
            data_store['LTC'] = data_store['LTC'][-100:]

    except KeyError as e:
        print(f"KeyError: {e}")
        return dash.no_update

    df = pd.DataFrame(data_store)

    fig = go.Figure()

    if selected_crypto == 'BTC':
        fig.add_trace(go.Scatter(x=df['Time'], y=df['BTC'], mode='lines+markers', name='Bitcoin'))
    elif selected_crypto == 'ETH':
        fig.add_trace(go.Scatter(x=df['Time'], y=df['ETH'], mode='lines+markers', name='Ethereum'))
    elif selected_crypto == 'LTC':
        fig.add_trace(go.Scatter(x=df['Time'], y=df['LTC'], mode='lines+markers', name='Litecoin'))

    fig.update_layout(title=f'Price of {selected_crypto} over Time',
                      xaxis_title='Time',
                      yaxis_title='Price (USD)')

    return fig

if __name__ == '__main__':
    app.run(debug=True)

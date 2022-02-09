import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import pandas as pd
# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '1d')
print(timestamp)
btc_price = {'error':False}
bars = client.get_historical_klines('BTCUSDT', '1d', timestamp, limit=1000)

for line in bars:
    del line[5:]

btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)
print(btc_df.head())
btc_df.to_csv('btc_bars3.csv')

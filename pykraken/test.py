
from rest_api_client import client
from rest_api_client.api.market_data import get_ohlc_data, get_order_book

myclient = client.Client(base_url='https://api.kraken.com/0')


data1 = get_ohlc_data.sync(client=myclient, pair='XBTUSD')
data2 = get_order_book.sync_detailed(client=myclient, pair='XBTUSD', count=100)

print(myclient)
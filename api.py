import json
import urllib.parse
import requests
from config import TOKEN

url = 'https://api.stockdata.org/v1/data/eod'
symbol = 'ABT'

params = urllib.parse.urlencode(
    {'api_token': TOKEN, 'symbols': symbol, 'date_from': '2021-01-01'})

req = requests.get(url=url, params=params).content
data = json.loads(req)

with open('json_data_{}.json'.format(symbol), 'w') as outfile:
    json.dump(data, outfile)

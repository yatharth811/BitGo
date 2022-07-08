import requests, json

base_url = 'https://api.coingecko.com/api/v3'

response = requests.get(f'{base_url}/derivatives')
for x in response.json():
        if x['contract_type'] != 'perpetual':
            print(x)
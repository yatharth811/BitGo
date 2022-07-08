import csv
import requests, json

API_KEY = '2854a5c3399c288c9183d204216c9c5d706e7d55bb64cd5a67eda10db684a574'

## this data is available for BTC only
## available historically as well but didnt make sense to do so.

response = requests.get(f'https://min-api.cryptocompare.com/data/blockchain/balancedistribution/latest?fsym=BTC&api_key={API_KEY}')
outData = []
csvheader = ['range', 'volume', 'addressCount']

for x in response.json()['Data']['balance_distribution']:
    fromBalance = x['from']
    toBalance = x['to']
    res = [f'{fromBalance}-{toBalance}', x['totalVolume'], x['addressesCount']]
    outData.append(res)

with open(f'balanceDistributionLatest.csv', "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(outData)
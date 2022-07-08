import time
import requests, json, csv
API_KEY = 'LRSGYQNJREBKNBBDIALT'
market = 'binance'
limit = 30
for cur in ['btc', 'eth']:
    response = requests.get(f'https://api.cryptowat.ch/markets/{market}/{cur}usdt/orderbook?limit={limit}&apikey={API_KEY}')
    outData = []
    csvheader = ['bid', 'bid-size', 'ask', 'ask-size']
    
    for i in range(limit):
        bid = response.json()['result']['bids'][i][0]
        bidSize = response.json()['result']['bids'][i][1]
        ask = response.json()['result']['asks'][i][0]
        askSize = response.json()['result']['asks'][i][1]
        res = [bid, bidSize, ask, askSize]
        outData.append(res)

    with open(f'orderBook-{cur}usdt-binance.csv', "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(outData)
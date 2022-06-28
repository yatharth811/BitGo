import pandas as pd
import requests, csv

data = pd.read_csv('coinissue.csv')
# res = 

csvheader = ['Coin', 'Price (if available)']
outData = []

for x in data.COIN:
    response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={x}&tsyms=USD').json()
    if ('USD' not in response):
        outData.append([x, 'N/A'])
    else:
        outData.append([x, response['USD']])

with open("cryptocompare-coinissue.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(outData)
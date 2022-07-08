import csv
import requests, json

API_KEY = '2854a5c3399c288c9183d204216c9c5d706e7d55bb64cd5a67eda10db684a574'
day_limit = 60

for cur in ['BTC', 'ETH']:
    response = requests.get(f'https://min-api.cryptocompare.com/data/blockchain/histo/day?fsym={cur}&api_key={API_KEY}&limit={day_limit}')
    outData = []
    csvheader = []

    for x in response.json()['Data']['Data'][0]:
        if x not in ['id', 'symbol']:
            csvheader.append(x)

    # print(csvheader)


    for x in response.json()['Data']['Data']:
        res = []
        for y in csvheader:
            res.append(x[y])

        outData.append(res)

    # print(outData)

    with open(f'blockchain-historical-{cur}.csv', "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(outData)
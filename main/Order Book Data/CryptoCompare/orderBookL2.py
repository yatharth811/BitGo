import requests, json, csv

API_KEY = '10a54ff876c174db2fe90a61907bf7eb979b48a7ec315fd6935ad77782d3ca2a'
noOfTopBids = 30
e = 'Binance'
for cur in ['ETH', 'BTC']:
    response = requests.get(f'https://min-api.cryptocompare.com/data/v2/ob/l2/snapshot?fsym={cur}&tsym=USDC&api_key={API_KEY}&limit={noOfTopBids}&e={e}')
    outData = []
    csvheader = ['bid', 'bid-size', 'ask', 'ask-size']
    # print(response.json())
    for i in range(noOfTopBids):
        bid = response.json()['Data']['BID'][i]['P']
        bidSize = response.json()['Data']['BID'][i]['Q']
        ask = response.json()['Data']['ASK'][i]['P']
        askSize = response.json()['Data']['ASK'][i]['Q']
        res = [bid, bidSize, ask, askSize]
        outData.append(res)

    # print(outData)

    with open(f'orderBook{e}-{cur}-USDC.csv', "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csvheader)
        writer.writerows(outData)
import re
from matplotlib.pyplot import hist
import requests, json, csv

## marketCap.csv 

myjson = {
  "USD" :   requests.get(f'https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD').json(),
  "INR" :   requests.get(f'https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=INR').json(),
  "EUR" :   requests.get(f'https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=EUR').json()
}
csvheader = ['Coin']
outData = []
historicalCoins = []

for currency in myjson:
    for x in myjson[currency]['Data'][0]['RAW'][currency]:
        csvheader.append(f'{currency}_{x}')


for x in myjson['USD']['Data']:
    listing = [x['CoinInfo']['Name']]
    historicalCoins.append(x['CoinInfo']['Name'])
    if (x['CoinInfo']['Name'] not in {'BIT', 'CUSDC'}):
        for y in x['RAW']['USD']:
            listing.append(x['RAW']['USD'][y])

    outData.append(listing)

cnt = 0
for x in myjson['INR']['Data']:
    listing = outData[cnt]
    if (x['CoinInfo']['Name'] not in {'BIT', 'CUSDC', 'SAITAMA', 'VELO', 'XEC', 'LDO'}):
        for y in x['RAW']['INR']:
            listing.append(x['RAW']['INR'][y])
    cnt+=1


cnt = 0
for x in myjson['EUR']['Data']:
    listing = outData[cnt]
    if (x['CoinInfo']['Name'] not in {'BIT', 'CUSDC', 'VELO', 'XEC'}):
        for y in x['RAW']['EUR']:
            listing.append(x['RAW']['EUR'][y])
    cnt+=1



## historicalPrices.csv

coins = ['BTC', 'ETH', 'USDT', 'USDC', 'BNB', 'SAITAMA', 'XRP', 'SOL', 'BUSD', 'ADA', 'DOGE']
csvheader2 = ['Time', 'BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'BNB-USD', 'SAITAMA-USD', 'XRP-USD', 'SOL-USD', 'BUSD-USD', 'ADA-USD', 'DOGE-USD']

for cur in ['INR', 'EUR']:
    for coin in coins:
        csvheader2.append(f'{coin}-{cur}')


outData2 = []
cnt = 0
limit = 671
for cur in ['USD', 'INR', 'EUR']:
    for currency in coins:
        res  = requests.get(f'https://min-api.cryptocompare.com/data/v2/histohour?fsym={currency}&tsym={cur}&limit={limit}').json()
        
        if (cur == 'INR' and currency == 'SAITAMA'):
            for x in range (limit+1):
                listing = outData2[x]
                listing.append(-1)

        else:
            for x in res['Data']['Data']:
                if currency=='BTC' and cur=='USD':
                    outData2.append([x['time']])


                listing = outData2[cnt]
                listing.append(x['high'])
                cnt+=1
        cnt = 0



## Hourly Total Trading Volume
csvheader3 = ['Time', 'Volume (in USD)', 'Volume (in INR)', 'Volume (in EUR)']
outData3 = []
for cur in ['USD', 'INR', 'EUR']:
    res =  requests.get(f'https://min-api.cryptocompare.com/data/exchange/histohour?tsym={cur}&limit={limit}').json()


    if cur == 'USD':
        for x in res['Data']:
                outData3.append([x['time'], x['volume']])

    else:
        for x in res['Data']:
            listing = outData3[cnt]
            listing.append(x['volume'])
            cnt+=1

        cnt = 0

## Top exchanges volume by data pair BTC-USD

csvheader4 = ['Exchange', 'Volume (in BTC)', 'Volume (in USD)', 'Price']
outData4 = []
res4 = requests.get(f'https://min-api.cryptocompare.com/data/top/exchanges?fsym=BTC&tsym=USD&limit=10').json()
for x in res4['Data']:
    outData4.append([x['exchange'], x['volume24h'], x['volume24hTo'], x['price']])


## Top exchanges volume by data pair ETH-USD
csvheader5 = ['Exchange', 'Volume (in ETH)', 'Volume (in USD)', 'Price']
outData5 = []
res5 = requests.get(f'https://min-api.cryptocompare.com/data/top/exchanges?fsym=ETH&tsym=USD&limit=10').json()
for x in res5['Data']:
    outData5.append([x['exchange'], x['volume24h'], x['volume24hTo'], x['price']])







## Daily Symbol Volume

csvheader6 = ['Time']
outData6 = []
for cur in ['USD','INR', 'EUR']:
    for coin in coins:
        csvheader6.append(f'{coin}-{cur}')

for cur in ['USD', 'INR', 'EUR']:
    for currency in coins:
        res  = requests.get(f'https://min-api.cryptocompare.com/data/symbol/histoday?fsym={currency}&tsym={cur}&limit={limit}').json()
        
        if (cur == 'INR' and currency == 'SAITAMA'):
            for x in range (limit+1):
                listing = outData6[x]
                listing.append(0)

        else:
            for x in res['Data']:
                if currency=='BTC' and cur=='USD':
                    outData6.append([x['time']])


                listing = outData6[cnt]
                listing.append(x['total_volume_total'])
                cnt+=1
            cnt = 0



with open("marketcap.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(outData)


with open("historicalPrices.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader2)
    writer.writerows(outData2)


with open("hourlyExchangeVolume.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader3)
    writer.writerows(outData3)

with open("topExchangeBTCUSD.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader4)
    writer.writerows(outData4)

with open("topExchangeETHUSD.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader5)
    writer.writerows(outData5)


with open("Exchange.csv", "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader6)
    writer.writerows(outData6)
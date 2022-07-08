import requests, json, csv

API_KEY = '10a54ff876c174db2fe90a61907bf7eb979b48a7ec315fd6935ad77782d3ca2a'

response = requests.get(f'https://min-api.cryptocompare.com/data/all/coinlist?apikey={API_KEY}')
lister = []
# print(response.json())
for x in response.json()['Data']:
    lister.append(x)

csvheader = ['Coin',  'Price', '24H Volume', 'Market Cap', 'Circulating Supply'] 
outData = []
nodata = []

# lister = lister[:20]
print(len(lister))

for x in lister:
    res = requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={x}&tsyms=USD&apikey={API_KEY}').json()
    try:
        tempRes = res['RAW'][x]['USD']
        bro = [tempRes['FROMSYMBOL'], tempRes['PRICE'], tempRes['TOTALVOLUME24HTO'], tempRes['MKTCAP'], tempRes['CIRCULATINGSUPPLY']]
        outData.append(bro)
    except:
        nodata.append(x)
        outData.append([x])

    

print(len(nodata))
print(nodata)

with open(f'coin-list.csv', "w", encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(outData)



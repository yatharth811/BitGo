import importlib, requests, json
API_KEY = '407e6a79-911a-440b-85bf-e331ccecfb5a'

url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY={API_KEY}'

response = requests.get(url)
print(response)
  
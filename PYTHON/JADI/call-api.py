import requests
responce = requests.get("https://api.coinbase.com/v2/prices/buy?currency=usd")
print(responce.text)
import requests
proxies = {
    'https':''
}
#https://api.coinbase.com/v2/prices/buy?currency=usd
responce = requests.get("https://randomfox.ca/floof/")

if responce.price <1000:
    print("find it is your work")
print(responce.text)
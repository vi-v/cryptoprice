import urllib
import sys
import json

args = sys.argv[1:]
response = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/')
cryptoData = json.loads(response.read().decode())
crpytoDataMap = {} # Dictionary for faster access

for data in cryptoData:
    crpytoDataMap[data['symbol']] = data

print args
print crpytoDataMap['LTC']['price_usd']



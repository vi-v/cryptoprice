import urllib
import sys
import json

args = sys.argv[1:]
response = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/')
cryptoData = json.loads(response.read().decode())
crpytoDataMap = {} # Dictionary for faster access

for data in cryptoData:
    crpytoDataMap[data['symbol']] = data

#print args
# print crpytoDataMap['LTC']['price_usd']

for arg in args:
    arg = arg.strip().replace('-', '')
    priceUSD = crpytoDataMap[arg]['price_usd']
    coinName = crpytoDataMap[arg]['name']
    percentChange24 = crpytoDataMap[arg]['percent_change_24h']

    print "%s (%s) \t| USD: %s \t| %% Change 24H: %s" % (coinName, arg, priceUSD, percentChange24)



import urllib
import sys
import json

args = sys.argv[1:]
response = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/')
cryptoData = json.loads(response.read().decode())
crpytoDataMap = {} # Dictionary for faster access

# Terminal colors
OKGREEN = '\033[92m'
FAIL = '\033[91m'
RESET = '\033[0;0m'

for data in cryptoData:
    crpytoDataMap[data['symbol']] = data

for arg in args:
    arg = arg.strip().replace('-', '')
    priceUSD = crpytoDataMap[arg]['price_usd']
    coinName = crpytoDataMap[arg]['name']
    percentChange24 = crpytoDataMap[arg]['percent_change_24h']

    if(float(percentChange24) < 0):
        changeColor = FAIL
    else:
        changeColor = OKGREEN

    print "%s%s (%s) \t| USD: %s \t| %% Change 24H: %s%s%s" % (RESET, coinName, arg, priceUSD, changeColor, percentChange24, RESET)
    
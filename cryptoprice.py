import urllib
import sys
import json

args = sys.argv[1:]
response = urllib.urlopen('https://api.coinmarketcap.com/v1/ticker/')
cryptoData = json.loads(response.read().decode())
crpytoDataMap = {} # Dictionary for faster access
findall = False
allCoins = []

# Terminal colors
OKGREEN = '\033[92m'
FAIL = '\033[91m'
RESET = '\033[0;0m'

if args[0] == '-a':
    findall = True

for data in cryptoData:
    crpytoDataMap[data['symbol']] = data

    if findall:
        allCoins.append(data['symbol'])

if findall:
    args = allCoins

for arg in args:
    arg = arg.strip().replace('-', '')
    priceUSD = crpytoDataMap[arg]['price_usd']
    coinName = crpytoDataMap[arg]['name']
    percentChange24 = crpytoDataMap[arg]['percent_change_24h']

    if(float(percentChange24) < 0):
        changeColor = FAIL
    else:
        changeColor = OKGREEN

    col1 = coinName + ' (' + arg + ')'
    col2 = 'USD: ' + priceUSD
    col3 = '% Change 24H: ' + changeColor + percentChange24

    print "%s%-30s | %-20s| %s %s" % (RESET, col1, col2, col3, RESET)
    
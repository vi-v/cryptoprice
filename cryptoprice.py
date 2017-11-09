import urllib2
import sys

args = sys.argv[1:]
cryptoData = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/').read()
crpytoDataMap = {} # Dictionary for faster access


print args



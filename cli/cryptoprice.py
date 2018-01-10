import click
import requests

@click.group()
def cli():
    pass


@click.command()
# @click.argument('coin', default='all', nargs=-1, help='Get price in USD for specified cryptos. Use --all to list price for all coins.')
@click.option('--nousd', is_flag=True, default=False)
@click.option('--btc', is_flag=True, default=False)
@click.option('--rank', is_flag=True, default=False)
@click.option('--volume', is_flag=True, default=False)
@click.option('--marketcap', is_flag=True, default=False)
@click.option('--change1h', is_flag=True, default=False)
@click.option('--change24h', is_flag=True, default=False)
@click.option('--change7d', is_flag=True, default=False)
@click.argument('coins', nargs=-1)
def price(coins, nousd, btc, rank, volume, marketcap, change1h, change24h, change7d):
    response =  requests.get('https://api.coinmarketcap.com/v1/ticker/')
    cryptoData = response.json()
    crpytoDataMap = {}  # Dictionary for faster access

    for crypto in cryptoData:
        crpytoDataMap[crypto['symbol']] = crypto

    # click.echo(crpytoDataMap)

    for coin in coins:
        coinData = crpytoDataMap[coin.upper()]
        
        coinInfo = coinData['name'] + " (" + coinData['symbol'] + ")"
        
        if(not nousd):
            coinInfo += " | USD: " + coinData['price_usd']
        
        if(btc):
            coinInfo += " | BTC: " + coinData['price_btc']

        if(rank):
            coinInfo += " | Rank: " + coinData['rank']

        if(volume):
            coinInfo += " | Volume: " + coinData['24h_volume_usd']

        if(marketcap):
            coinInfo += " | Market Cap: " + coinData['market_cap_usd']

        if(change1h):
            coinInfo += " | % Change 1H: " + coinData['percent_change_1h']

        if(change24h):
            coinInfo += " | % Change 24H: " + coinData['percent_change_24h']

        if(change7d):
            coinInfo += " | % Change 7D: " + coinData['percent_change_7d']

        click.echo(coinInfo)

cli.add_command(price)

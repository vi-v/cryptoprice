import click
import requests
from terminaltables import SingleTable


@click.group()
def cli():
    pass


@click.command()
# @click.argument('coin', default='all', nargs=-1, help='Get price in USD for specified cryptos. Use --all to list price for all coins.')
@click.option('--nocolor', is_flag=True, default=False)
@click.option('--table', is_flag=True, default=False)
@click.option('--nousd', is_flag=True, default=False)
@click.option('--btc', is_flag=True, default=False)
@click.option('--rank', is_flag=True, default=False)
@click.option('--all', is_flag=True, default=False)
@click.option('--volume', is_flag=True, default=False)
@click.option('--marketcap', is_flag=True, default=False)
@click.option('--change1h', is_flag=True, default=False)
@click.option('--change24h', is_flag=True, default=False)
@click.option('--change7d', is_flag=True, default=False)
@click.argument('coins', nargs=-1)
def price(nocolor, table, coins, nousd, btc, rank, all, volume, marketcap, change1h, change24h, change7d):
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
    crypto_data = response.json()
    crypto_data_map = {}  # Dictionary for faster access
    all_coins = [] # List of all coin names

    for crypto in crypto_data:
        all_coins.append(crypto['symbol'])
        crypto_data_map[crypto['symbol']] = crypto

    # Print table if specified
    table_data = []
    table_headers = ['Name']
    if(not nousd):
        table_headers.append('USD')
    if(btc):
        table_headers.append('BTC')
    if(rank):
        table_headers.append('Rank')
    if(volume):
        table_headers.append('Volume')
    if(marketcap):
        table_headers.append('Market Cap')
    if(change1h):
        table_headers.append('% Change 1H')
    if(change24h):
        table_headers.append('% Change 24H')
    if(change7d):
        table_headers.append('% Change 7D')
    table_data.append(table_headers)

    # if --all or no coin is specified, list all
    if all or not coins:
        coins = all_coins

    for coin in coins:
        if not coin.upper() in crypto_data_map:
            continue

        coin_data = crypto_data_map[coin.upper()]

        table_row = []

        coin_info = coin_data['name'] + " (" + coin_data['symbol'] + ")"
        table_row.append(coin_info)

        if(not nousd):
            coin_info += " | USD: " + coin_data['price_usd']
            table_row.append(coin_data['price_usd'])

        if(btc):
            coin_info += " | BTC: " + coin_data['price_btc']
            table_row.append(coin_data['price_btc'])

        if(rank):
            coin_info += " | Rank: " + coin_data['rank']
            table_row.append(coin_data['rank'])

        if(volume):
            coin_info += " | Volume: " + coin_data['24h_volume_usd']
            table_row.append(coin_data['24h_volume_usd'])

        if(marketcap):
            coin_info += " | Market Cap: " + coin_data['market_cap_usd']
            table_row.append(coin_data['market_cap_usd'])

        if(change1h):
            perc_change = coin_data['percent_change_1h']
            if not nocolor:
                if float(perc_change) > 0:
                    perc_change = click.style(perc_change, fg='green')
                else:
                    perc_change = click.style(perc_change, fg='red')
                
            coin_info += " | % Change 1H: " + perc_change
            table_row.append(perc_change)

        if(change24h):
            perc_change = coin_data['percent_change_24h']
            if not nocolor:
                if float(perc_change) > 0:
                    perc_change = click.style(perc_change, fg='green')
                else:
                    perc_change = click.style(perc_change, fg='red')
                
            coin_info += " | % Change 24H: " + perc_change
            table_row.append(perc_change)

        if(change7d):
            perc_change = coin_data['percent_change_7d']
            if not nocolor:
                if float(perc_change) > 0:
                    perc_change = click.style(perc_change, fg='green')
                else:
                    perc_change = click.style(perc_change, fg='red')
                
            coin_info += " | % Change 7D: " + perc_change
            table_row.append(perc_change)

        table_data.append(table_row)

        if(not table):
            click.echo(coin_info)

    if(table):
        term_table = SingleTable(table_data)
        click.echo(term_table.table)

cli.add_command(price)


import click
import json
import requests


@click.group(name="stock")
def stock_cmd():
    pass


@stock_cmd.command(name="list")
@click.option('--page', required=False, default=1)
@click.option('--limit', required=False, default=10)
@click.option('--filter-ticker', required=False)
def show_stocks(page, limit, filter_ticker):
    print(page)
    print(limit)
    print(filter_ticker)

# todo add calc cmd
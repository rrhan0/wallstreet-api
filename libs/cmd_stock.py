
import click
import json


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


@stock_cmd.command(name="calc")
@click.option('--ticker', required=True)
@click.option('--roi', required=True)
@click.option('--expected-growth-rate', required=True)
@click.option('--pe', required=True)
def calc_stocks(ticker, roi, expected_growth_rate, pe):
    print(ticker)
    print(roi)
    print(expected_growth_rate)
    print(pe)
    #EPS * (1 + expected_growth_rate) * pe
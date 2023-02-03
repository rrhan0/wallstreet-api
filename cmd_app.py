#!/usr/bin/env python
import click
from libs.cmd_stock import stock_cmd


@click.group()
def cli():
    pass


cli.add_command(stock_cmd)


if __name__ == "__main__":
    cli()

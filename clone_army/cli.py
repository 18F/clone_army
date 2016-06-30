# -*- coding: utf-8 -*-

from . import clone_army
import click

@click.command()
@click.option('-o', '--org', 'type', flag_value='org', default=True)
@click.option('-u', '--user', 'type', flag_value='user')
@click.argument('account')
def main(account, type):
    """Console script for clone_army"""
    result = clone_army.repositories(account, type)
    return 'Placeholder for results'



if __name__ == "__main__":
    main()

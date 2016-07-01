# -*- coding: utf-8 -*-

from . import clone_army
import click

@click.command(context_settings=dict(ignore_unknown_options=True,))
@click.option('-o', '--org', 'type', flag_value='org', default=True, help='Clone GitHub account of an org')
@click.option('-u', '--user', 'type', flag_value='user', help='Clone GitHub account of a single user')
@click.option('-f', '--filter', help='Filter repositories (regex syntax)')
@click.argument('account')
@click.argument('git_options', nargs=-1, type=click.UNPROCESSED)
def main(account, type, filter, git_options):
    """Console script for clone_army"""
    if account.startswith('-'):
        raise click.BadArgumentUsage("Options for Git should come at end.")
    clone_army.Repository.synch_all(account, type, filter, *git_options)



if __name__ == "__main__":
    main()

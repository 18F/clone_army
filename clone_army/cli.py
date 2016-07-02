# -*- coding: utf-8 -*-

from . import clone_army
import click
import logging


@click.command(context_settings=dict(ignore_unknown_options=True, ))
@click.option('-o',
              '--org',
              'type',
              flag_value='org',
              default=True,
              help='Clone GitHub account of an org')
@click.option('-u',
              '--user',
              'type',
              flag_value='user',
              help='Clone GitHub account of a single user')
@click.option('-f', '--filter', help='Filter repositories (regex syntax)')
@click.option('-v', '--verbose', is_flag=True, help='See logging info')
@click.option('-x', '--existing-only', is_flag=True, help='Only update directories already present, no new clones')
@click.argument('account')
@click.argument('git_options', nargs=-1, type=click.UNPROCESSED)
def main(account, type, filter, verbose, git_options, existing_only):
    """Console script for clone_army"""
    if account.startswith('-'):
        raise click.BadArgumentUsage("Options for Git should come at end.")
    if verbose:
        logging.getLogger(__name__).setLevel(logging.INFO)
    clone_army.Repository.synch_all(account, type, filter, *git_options)


if __name__ == "__main__":
    main()

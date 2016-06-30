# -*- coding: utf-8 -*-
import itertools

import click
import requests

_REPO_LIST_URL = 'https://api.github.com/{type}s/{account}/repos?page={page_no}'


def repositories(account, type='org'):
    for page_no in itertools.count(1):
        click.echo('Page {page_no}'.format(page_no=page_no))
        url = _REPO_LIST_URL.format(type=type,
                                    account=account,
                                    page_no=page_no)
        resp = requests.get(url)
        if not resp.json():
            raise StopIteration
        for repo in resp.json():
            yield repo

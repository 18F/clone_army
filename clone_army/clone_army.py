# -*- coding: utf-8 -*-
import itertools
import os.path
import subprocess
import logging
import re

import click
import requests

_REPO_LIST_URL = 'https://api.github.com/{type}s/{account}/repos?page={page_no}'
_SEARCH_URL = 'https://api.github.com/search/repositories?q={filter}+{type}:{account}&page={page_no}'


def repositories(account, type='org', filter=None):
    for page_no in itertools.count(1):
        click.echo('Page {page_no}'.format(page_no=page_no))
        url = _SEARCH_URL if filter else _REPO_LIST_URL
        url = url.format(type=type,
                         account=account,
                         page_no=page_no,
                         filter=filter)
        resp = requests.get(url)
        if not resp.json():
            raise StopIteration
        for repo in resp.json():
            if (not filter) or re.search(filter, repo['name']):
                yield repo


class Repository(object):
    def __init__(self, data):
        self.__dict__.update(data)

    @classmethod
    def synch_all(cls, account, type, filter=None, *args):
        for repo_data in repositories(account, type, filter):
            repo = cls(repo_data)
            repo.synch(*args)

    def synch(self, *args):
        if os.path.exists(self.name):
            logging.info('{} exists; pulling changes'.format(self.name))
            subprocess.run(['git', 'pull'], cwd=self.name)
        else:
            logging.info('Cloning '.format(self.name))
            subprocess.run(['git', 'clone', *args, self.clone_url])

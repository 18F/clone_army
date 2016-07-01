#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_clone_army
----------------------------------

Tests for `clone_army` module.
"""

from . import mock_data

import os.path
from unittest import mock
import pytest

from click.testing import CliRunner

from clone_army import clone_army
from clone_army import cli


class TestCli(object):
    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    @pytest.mark.skip(reason="need to mock out despite runner.invoke")
    def test_cli_accepts_account_name(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, ['18F'])
        assert not result.exception

    def test_cli_demands_account_name(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, [])
        assert result.exception
        assert 'Usage:' in result.output

    @pytest.mark.skip(reason="need to mock out despite runner.invoke")
    def test_cli_accepts_type(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, ['catherinedevlin', '--user'])
        assert not result.exception

    def test_cli_gives_help_message(self):
        runner = CliRunner()
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass


@mock.patch('requests.get', side_effect=mock_data.Response)
class TestRepoList(object):
    def test_lists_org_repos(self, mocked_get):
        repos = clone_army.repositories('18F')
        repos.__next__()
        assert 'https://api.github.com/orgs' in mocked_get.call_args[0][0]

    def test_lists_user_repos(self, mocked_get):
        repos = clone_army.repositories('catherinedevlin', type='user')
        repos.__next__()
        assert 'https://api.github.com/users' in mocked_get.call_args[0][0]

    def test_filtered_repo_list(self, mocked_get):
        for repo in clone_army.repositories('18F', filter=r'18f'):
            assert '18f' in repo['name']


@mock.patch('subprocess.run')
@mock.patch('requests.get', side_effect=mock_data.Response)
class TestCloning(object):
    @mock.patch('os.path.exists', return_value=False)
    def test_creates_directory(self, mocked_exists, mocked_get, mocked_run):
        repos = clone_army.repositories('18F')
        repo1 = clone_army.Repository(repos.__next__())
        repo1.synch()
        mocked_run.assert_called_with(['git', 'clone', repo1.clone_url])

    def test_args_passed_when_cloning(self, mocked_get, mocked_run):
        repos = clone_army.repositories('18F')
        repo1 = clone_army.Repository(repos.__next__())
        assert not os.path.exists(repo1.name)
        repo1.synch('--depth', '1')
        mocked_run.assert_called_with(
            ['git', 'clone', '--depth', '1',
             'https://github.com/18F/14c-prototype.git'])

    @mock.patch('os.path.exists', return_value=True)
    def test_pulls_when_dir_exists(self, mocked_exists, mocked_get,
                                   mocked_run):
        repos = clone_army.repositories('18F')
        repo1 = clone_army.Repository(repos.__next__())
        repo1.synch()
        mocked_run.assert_called_with(['git', 'pull'], cwd=repo1.name)

    @mock.patch('os.path.exists', return_value=False)
    def test_clone_each_repo(self, mocked_exists, mocked_get, mocked_run):
        clone_army.Repository.synch_all('18F', 'org')
        assert len(mocked_run.mock_calls) == len(mock_data.DATA)

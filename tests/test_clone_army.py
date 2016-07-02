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

import requests
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

    def test_no_account_name_ok_when_existing_only(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            result = runner.invoke(cli.main, ['--existing-only', ])
            assert not result.exception

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


@mock.patch('requests.get', side_effect=mock_data.GoodResponse)
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
        for repo in clone_army.repositories('18F', filter=r'gsa'):
            assert 'gsa' in repo['name']

@mock.patch('requests.get', side_effect=mock_data.BadResponse)
class TestNonexistentRepoList(object):
    def test_no_such_repo(self, mocked_get):
        with pytest.raises(requests.exceptions.HTTPError):
            result = clone_army.repositories('there is no such repo')
            result.__next__()


@mock.patch('subprocess.run')
@mock.patch('requests.get', side_effect=mock_data.GoodResponse)
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

    @mock.patch('os.listdir', return_value=['dir1', 'dir2', 'dir3'])
    @mock.patch('os.path.isdir', return_value=True)
    def test_only_updating_present_repos(self, mocked_isdir, mocked_listdir,
                                         mocked_get, mocked_run):
        expected_calls = [
            mock.call(['git', 'pull'], cwd='dir1'), mock.call(
                ['git', 'pull'], cwd='dir2'), mock.call(
                    ['git', 'pull'], cwd='dir3')
        ]
        clone_army.Repository.synch_present('18F', 'org')
        mocked_run.assert_has_calls(expected_calls)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_clone_army
----------------------------------

Tests for `clone_army` module.
"""

from . import mock_data

from unittest import mock
import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from clone_army import clone_army
from clone_army import cli


class TestCli(object):
    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    def test_cli_accepts_account_name(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, ['18F'])
        assert not result.exception

    def test_cli_demands_account_name(self):
        runner = CliRunner()
        result = runner.invoke(cli.main, [])
        assert result.exception
        assert 'Usage:' in result.output

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


class TestRepoList(object):
    @classmethod
    def setup_class(cls):
        pass

    @mock.patch('requests.get', side_effect=mock_data.Response)
    def test_lists_org_repos(self, mocked_get):
        repos = clone_army.repositories('18F')
        repos.__next__()
        assert 'https://api.github.com/orgs' in mocked_get.call_args[0][0]

    @mock.patch('requests.get', side_effect=mock_data.Response)
    def test_lists_user_repos(self, mocked_get):
        repos = clone_army.repositories('catherinedevlin', type='user')
        repos.__next__()
        assert 'https://api.github.com/users' in mocked_get.call_args[0][0]

    @classmethod
    def teardown_class(cls):
        pass

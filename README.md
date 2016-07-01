# clone_army

[![PyPI Status](https://img.shields.io/pypi/v/clone_army.svg)](https://pypi.python.org/pypi/clone_army)
[![Build Status](https://img.shields.io/travis/18F/clone_army.svg?branch=master)](https://travis-ci.org/18F/clone_army)
[![Coverage Status](https://coveralls.io/repos/github/18F/clone_army.svg?branch=master)](https://coveralls.io/github/18F/clone_army?branch=master)
[![Code Climate](https://codeclimate.com/github/18F/clone_army.svg)](https://codeclimate.com/github/18F/clone_army)

Locally clone or synch all a GitHub account's public repos.


## Using

To clone or synch an organization's repos, `cd` to the directory you want
to serve as the parent directory of all the repos, and

    clone-army <org_name>

Each repo will be cloned, if there is no child directory by its name; or,
if there is, `git pull` will be run in it.

Any extra options after the organization name are passed on to `git clone`.
`--depth 1`, for example, makes
[shallow clones](https://www.perforce.com/blog/141218/git-beyond-basics-using-shallow-clones)
that can save considerable disk space.

To clone the repos of a user (not an org), add `-u` or `--user`:

    clone-army --user <user_name>

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [18F/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

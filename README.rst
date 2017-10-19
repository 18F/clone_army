clone_army
==========

.. image:: https://img.shields.io/pypi/v/clone_army.svg
   :target: https://pypi.python.org/pypi/clone_army
   :alt: PyPI status

.. image:: https://circleci.com/gh/18F/clone_army.svg?style=svg
   :target: https://circleci.com/gh/18F/clone_army
   :alt: CircleCI status

.. image:: https://codeclimate.com/github/18F/clone_army/badges/gpa.svg
   :target: https://codeclimate.com/github/18F/clone_army
   :alt: Code Climate

.. image:: https://codeclimate.com/github/18F/clone_army/badges/coverage.svg
   :target: https://codeclimate.com/github/18F/clone_army/coverage
   :alt: Test Coverage

.. image:: https://gemnasium.com/badges/github.com/18F/clone_army.svg
   :target: https://gemnasium.com/github.com/18F/clone_army
   :alt: Gemnasium

Locally clone or synch all a GitHub account's public repos.


Installing
----------

*Requires Python 3.5*

::

    pip install -e git+https://github.com/18F/clone_army.git#egg=clone_army

Using
-----

To clone or synch an organization's repos, `cd` to the directory you want
to serve as the parent directory of all the repos, and

::

    clone-army <org_name>

Each repo will be cloned, if there is no child directory by its name; or,
if there is, `git pull` will be run in it.

Any extra options *after* the organization name are passed on to `git clone`.
`--depth 1`, for example, makes `shallow clones`_
that can save considerable disk space.

.. _`shallow clones`: https://www.perforce.com/blog/141218/git-beyond-basics-using-shallow-clones

To clone the repos of a user (not an org), add `-u` or `--user`::

    clone-army --user <user_name>

To refresh (pull) only the repositories currently present as subdirectories::

    clone-army -x

The only differences between this and simply re-running `clone-army <org_name>`
are

- Any repositories that have appeared in the account in the meantime will
  not be cloned
- If you had run `clone-army` with a filter, you won't need to re-use that
  filter to avoid cloning the rest of the repositories

Comparable projects
-------------------

- clone_github_

.. _clone_github: https://github.com/khilnani/clone-github

Credits
-------

This package was created with Cookiecutter_
and the `18F/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

.. _`18F/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Public domain
-------------

This project is in the worldwide `public domain`_. As stated in CONTRIBUTING_:

  This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the `CC0 1.0 Universal public domain dedication`_.

  All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.

.. _`public domain`: LICENSE.md
.. _CONTRIBUTING: CONTRIBUTING.md
.. _`CC0 1.0 Universal public domain dedication`: https://creativecommons.org/publicdomain/zero/1.0/

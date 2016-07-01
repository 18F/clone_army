class Response(object):

    _PAGE_LENGTH = 3

    def __init__(self, url):
        pieces = url.split('=')
        if len(pieces) > 1:
            self.page = int(pieces[1])
        else:
            self.page = 1

    def json(self):
        begin_at = self._PAGE_LENGTH * (self.page - 1)
        return DATA[begin_at:begin_at + self._PAGE_LENGTH]


DATA = [
    {'archive_url':
     'https://api.github.com/repos/18F/14c-prototype/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/14c-prototype/assignees{/user}',
     'blobs_url':
     'https://api.github.com/repos/18F/14c-prototype/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/14c-prototype/branches{/branch}',
     'clone_url': 'https://github.com/18F/14c-prototype.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/14c-prototype/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/14c-prototype/comments{/number}',
     'commits_url':
     'https://api.github.com/repos/18F/14c-prototype/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/14c-prototype/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/14c-prototype/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/14c-prototype/contributors',
     'created_at': '2016-04-01T20:48:55Z',
     'default_branch': 'master',
     'deployments_url':
     'https://api.github.com/repos/18F/14c-prototype/deployments',
     'description': '',
     'downloads_url':
     'https://api.github.com/repos/18F/14c-prototype/downloads',
     'events_url': 'https://api.github.com/repos/18F/14c-prototype/events',
     'fork': False,
     'forks': 1,
     'forks_count': 1,
     'forks_url': 'https://api.github.com/repos/18F/14c-prototype/forks',
     'full_name': '18F/14c-prototype',
     'git_commits_url':
     'https://api.github.com/repos/18F/14c-prototype/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/14c-prototype/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/14c-prototype/git/tags{/sha}',
     'git_url': 'git://github.com/18F/14c-prototype.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': True,
     'homepage': None,
     'hooks_url': 'https://api.github.com/repos/18F/14c-prototype/hooks',
     'html_url': 'https://github.com/18F/14c-prototype',
     'id': 55261451,
     'issue_comment_url':
     'https://api.github.com/repos/18F/14c-prototype/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/14c-prototype/issues/events{/number}',
     'issues_url':
     'https://api.github.com/repos/18F/14c-prototype/issues{/number}',
     'keys_url':
     'https://api.github.com/repos/18F/14c-prototype/keys{/key_id}',
     'labels_url':
     'https://api.github.com/repos/18F/14c-prototype/labels{/name}',
     'language': None,
     'languages_url':
     'https://api.github.com/repos/18F/14c-prototype/languages',
     'merges_url': 'https://api.github.com/repos/18F/14c-prototype/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/14c-prototype/milestones{/number}',
     'mirror_url': None,
     'name': '14c-prototype',
     'notifications_url':
     'https://api.github.com/repos/18F/14c-prototype/notifications{?since,all,participating}',
     'open_issues': 1,
     'open_issues_count': 1,
     'owner': {'avatar_url':
               'https://avatars.githubusercontent.com/u/6233994?v=3',
               'events_url':
               'https://api.github.com/users/18F/events{/privacy}',
               'followers_url': 'https://api.github.com/users/18F/followers',
               'following_url':
               'https://api.github.com/users/18F/following{/other_user}',
               'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
               'gravatar_id': '',
               'html_url': 'https://github.com/18F',
               'id': 6233994,
               'login': '18F',
               'organizations_url': 'https://api.github.com/users/18F/orgs',
               'received_events_url':
               'https://api.github.com/users/18F/received_events',
               'repos_url': 'https://api.github.com/users/18F/repos',
               'site_admin': False,
               'starred_url':
               'https://api.github.com/users/18F/starred{/owner}{/repo}',
               'subscriptions_url':
               'https://api.github.com/users/18F/subscriptions',
               'type': 'Organization',
               'url': 'https://api.github.com/users/18F'},
     'private': False,
     'pulls_url':
     'https://api.github.com/repos/18F/14c-prototype/pulls{/number}',
     'pushed_at': '2016-04-15T07:29:49Z',
     'releases_url':
     'https://api.github.com/repos/18F/14c-prototype/releases{/id}',
     'size': 12177,
     'ssh_url': 'git@github.com:18F/14c-prototype.git',
     'stargazers_count': 0,
     'stargazers_url':
     'https://api.github.com/repos/18F/14c-prototype/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/14c-prototype/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/14c-prototype/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/14c-prototype/subscription',
     'svn_url': 'https://github.com/18F/14c-prototype',
     'tags_url': 'https://api.github.com/repos/18F/14c-prototype/tags',
     'teams_url': 'https://api.github.com/repos/18F/14c-prototype/teams',
     'trees_url':
     'https://api.github.com/repos/18F/14c-prototype/git/trees{/sha}',
     'updated_at': '2016-04-01T20:48:55Z',
     'url': 'https://api.github.com/repos/18F/14c-prototype',
     'watchers': 0,
     'watchers_count': 0},
    {'archive_url':
     'https://api.github.com/repos/18F/18f-bot/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18f-bot/assignees{/user}',
     'blobs_url': 'https://api.github.com/repos/18F/18f-bot/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18f-bot/branches{/branch}',
     'clone_url': 'https://github.com/18F/18f-bot.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18f-bot/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18f-bot/comments{/number}',
     'commits_url': 'https://api.github.com/repos/18F/18f-bot/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18f-bot/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18f-bot/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18f-bot/contributors',
     'created_at': '2014-09-18T12:23:35Z',
     'default_branch': 'master',
     'deployments_url': 'https://api.github.com/repos/18F/18f-bot/deployments',
     'description': "18F's Slack bot, Charlie. Based on Hubot.",
     'downloads_url': 'https://api.github.com/repos/18F/18f-bot/downloads',
     'events_url': 'https://api.github.com/repos/18F/18f-bot/events',
     'fork': True,
     'forks': 6,
     'forks_count': 6,
     'forks_url': 'https://api.github.com/repos/18F/18f-bot/forks',
     'full_name': '18F/18f-bot',
     'git_commits_url':
     'https://api.github.com/repos/18F/18f-bot/git/commits{/sha}',
     'git_refs_url': 'https://api.github.com/repos/18F/18f-bot/git/refs{/sha}',
     'git_tags_url': 'https://api.github.com/repos/18F/18f-bot/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18f-bot.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': False,
     'homepage': '',
     'hooks_url': 'https://api.github.com/repos/18F/18f-bot/hooks',
     'html_url': 'https://github.com/18F/18f-bot',
     'id': 24187077,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18f-bot/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18f-bot/issues/events{/number}',
     'issues_url': 'https://api.github.com/repos/18F/18f-bot/issues{/number}',
     'keys_url': 'https://api.github.com/repos/18F/18f-bot/keys{/key_id}',
     'labels_url': 'https://api.github.com/repos/18F/18f-bot/labels{/name}',
     'language': 'CoffeeScript',
     'languages_url': 'https://api.github.com/repos/18F/18f-bot/languages',
     'merges_url': 'https://api.github.com/repos/18F/18f-bot/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18f-bot/milestones{/number}',
     'mirror_url': None,
     'name': '18f-bot',
     'notifications_url':
     'https://api.github.com/repos/18F/18f-bot/notifications{?since,all,participating}',
     'open_issues': 21,
     'open_issues_count': 21,
     'owner': {'avatar_url':
               'https://avatars.githubusercontent.com/u/6233994?v=3',
               'events_url':
               'https://api.github.com/users/18F/events{/privacy}',
               'followers_url': 'https://api.github.com/users/18F/followers',
               'following_url':
               'https://api.github.com/users/18F/following{/other_user}',
               'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
               'gravatar_id': '',
               'html_url': 'https://github.com/18F',
               'id': 6233994,
               'login': '18F',
               'organizations_url': 'https://api.github.com/users/18F/orgs',
               'received_events_url':
               'https://api.github.com/users/18F/received_events',
               'repos_url': 'https://api.github.com/users/18F/repos',
               'site_admin': False,
               'starred_url':
               'https://api.github.com/users/18F/starred{/owner}{/repo}',
               'subscriptions_url':
               'https://api.github.com/users/18F/subscriptions',
               'type': 'Organization',
               'url': 'https://api.github.com/users/18F'},
     'private': False,
     'pulls_url': 'https://api.github.com/repos/18F/18f-bot/pulls{/number}',
     'pushed_at': '2016-06-02T23:43:12Z',
     'releases_url': 'https://api.github.com/repos/18F/18f-bot/releases{/id}',
     'size': 75,
     'ssh_url': 'git@github.com:18F/18f-bot.git',
     'stargazers_count': 7,
     'stargazers_url': 'https://api.github.com/repos/18F/18f-bot/stargazers',
     'statuses_url': 'https://api.github.com/repos/18F/18f-bot/statuses/{sha}',
     'subscribers_url': 'https://api.github.com/repos/18F/18f-bot/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18f-bot/subscription',
     'svn_url': 'https://github.com/18F/18f-bot',
     'tags_url': 'https://api.github.com/repos/18F/18f-bot/tags',
     'teams_url': 'https://api.github.com/repos/18F/18f-bot/teams',
     'trees_url': 'https://api.github.com/repos/18F/18f-bot/git/trees{/sha}',
     'updated_at': '2016-06-02T23:32:31Z',
     'url': 'https://api.github.com/repos/18F/18f-bot',
     'watchers': 7,
     'watchers_count': 7},
    {'archive_url':
     'https://api.github.com/repos/18F/18f-cli/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18f-cli/assignees{/user}',
     'blobs_url': 'https://api.github.com/repos/18F/18f-cli/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18f-cli/branches{/branch}',
     'clone_url': 'https://github.com/18F/18f-cli.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18f-cli/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18f-cli/comments{/number}',
     'commits_url': 'https://api.github.com/repos/18F/18f-cli/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18f-cli/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18f-cli/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18f-cli/contributors',
     'created_at': '2016-01-25T18:25:47Z',
     'default_branch': 'develop',
     'deployments_url': 'https://api.github.com/repos/18F/18f-cli/deployments',
     'description': 'A command line utility to standardize common 18F actions',
     'downloads_url': 'https://api.github.com/repos/18F/18f-cli/downloads',
     'events_url': 'https://api.github.com/repos/18F/18f-cli/events',
     'fork': False,
     'forks': 3,
     'forks_count': 3,
     'forks_url': 'https://api.github.com/repos/18F/18f-cli/forks',
     'full_name': '18F/18f-cli',
     'git_commits_url':
     'https://api.github.com/repos/18F/18f-cli/git/commits{/sha}',
     'git_refs_url': 'https://api.github.com/repos/18F/18f-cli/git/refs{/sha}',
     'git_tags_url': 'https://api.github.com/repos/18F/18f-cli/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18f-cli.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': True,
     'homepage': None,
     'hooks_url': 'https://api.github.com/repos/18F/18f-cli/hooks',
     'html_url': 'https://github.com/18F/18f-cli',
     'id': 50371314,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18f-cli/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18f-cli/issues/events{/number}',
     'issues_url': 'https://api.github.com/repos/18F/18f-cli/issues{/number}',
     'keys_url': 'https://api.github.com/repos/18F/18f-cli/keys{/key_id}',
     'labels_url': 'https://api.github.com/repos/18F/18f-cli/labels{/name}',
     'language': 'Shell',
     'languages_url': 'https://api.github.com/repos/18F/18f-cli/languages',
     'merges_url': 'https://api.github.com/repos/18F/18f-cli/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18f-cli/milestones{/number}',
     'mirror_url': None,
     'name': '18f-cli',
     'notifications_url':
     'https://api.github.com/repos/18F/18f-cli/notifications{?since,all,participating}',
     'open_issues': 12,
     'open_issues_count': 12,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url': 'https://api.github.com/repos/18F/18f-cli/pulls{/number}',
     'pushed_at': '2016-06-20T19:11:11Z',
     'releases_url': 'https://api.github.com/repos/18F/18f-cli/releases{/id}',
     'size': 76,
     'ssh_url': 'git@github.com:18F/18f-cli.git',
     'stargazers_count': 13,
     'stargazers_url': 'https://api.github.com/repos/18F/18f-cli/stargazers',
     'statuses_url': 'https://api.github.com/repos/18F/18f-cli/statuses/{sha}',
     'subscribers_url': 'https://api.github.com/repos/18F/18f-cli/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18f-cli/subscription',
     'svn_url': 'https://github.com/18F/18f-cli',
     'tags_url': 'https://api.github.com/repos/18F/18f-cli/tags',
     'teams_url': 'https://api.github.com/repos/18F/18f-cli/teams',
     'trees_url': 'https://api.github.com/repos/18F/18f-cli/git/trees{/sha}',
     'updated_at': '2016-06-17T00:10:51Z',
     'url': 'https://api.github.com/repos/18F/18f-cli',
     'watchers': 13,
     'watchers_count': 13},
    {'archive_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/assignees{/user}',
     'blobs_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/branches{/branch}',
     'clone_url': 'https://github.com/18F/18f-reveal.js-theme.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/comments{/number}',
     'commits_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/contributors',
     'created_at': '2016-05-23T21:12:27Z',
     'default_branch': '18f-pages',
     'deployments_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/deployments',
     'description': 'A reveal.js theme with 18F branding.',
     'downloads_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/downloads',
     'events_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/events',
     'fork': False,
     'forks': 0,
     'forks_count': 0,
     'forks_url': 'https://api.github.com/repos/18F/18f-reveal.js-theme/forks',
     'full_name': '18F/18f-reveal.js-theme',
     'git_commits_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18f-reveal.js-theme.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': True,
     'homepage': 'https://pages.18f.gov/18f-reveal.js-theme/',
     'hooks_url': 'https://api.github.com/repos/18F/18f-reveal.js-theme/hooks',
     'html_url': 'https://github.com/18F/18f-reveal.js-theme',
     'id': 59518694,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/issues/events{/number}',
     'issues_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/issues{/number}',
     'keys_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/keys{/key_id}',
     'labels_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/labels{/name}',
     'language': 'JavaScript',
     'languages_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/languages',
     'merges_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/milestones{/number}',
     'mirror_url': None,
     'name': '18f-reveal.js-theme',
     'notifications_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/notifications{?since,all,participating}',
     'open_issues': 4,
     'open_issues_count': 4,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/pulls{/number}',
     'pushed_at': '2016-05-24T21:33:49Z',
     'releases_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/releases{/id}',
     'size': 309,
     'ssh_url': 'git@github.com:18F/18f-reveal.js-theme.git',
     'stargazers_count': 1,
     'stargazers_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/subscription',
     'svn_url': 'https://github.com/18F/18f-reveal.js-theme',
     'tags_url': 'https://api.github.com/repos/18F/18f-reveal.js-theme/tags',
     'teams_url': 'https://api.github.com/repos/18F/18f-reveal.js-theme/teams',
     'trees_url':
     'https://api.github.com/repos/18F/18f-reveal.js-theme/git/trees{/sha}',
     'updated_at': '2016-05-24T14:00:48Z',
     'url': 'https://api.github.com/repos/18F/18f-reveal.js-theme',
     'watchers': 1,
     'watchers_count': 1},
    {'archive_url':
     'https://api.github.com/repos/18F/18f.github.io/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18f.github.io/assignees{/user}',
     'blobs_url':
     'https://api.github.com/repos/18F/18f.github.io/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18f.github.io/branches{/branch}',
     'clone_url': 'https://github.com/18F/18f.github.io.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18f.github.io/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18f.github.io/comments{/number}',
     'commits_url':
     'https://api.github.com/repos/18F/18f.github.io/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18f.github.io/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18f.github.io/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18f.github.io/contributors',
     'created_at': '2014-03-01T22:18:53Z',
     'default_branch': 'master',
     'deployments_url':
     'https://api.github.com/repos/18F/18f.github.io/deployments',
     'description': "DEPRECATED: List of 18F's open source projects",
     'downloads_url':
     'https://api.github.com/repos/18F/18f.github.io/downloads',
     'events_url': 'https://api.github.com/repos/18F/18f.github.io/events',
     'fork': False,
     'forks': 21,
     'forks_count': 21,
     'forks_url': 'https://api.github.com/repos/18F/18f.github.io/forks',
     'full_name': '18F/18f.github.io',
     'git_commits_url':
     'https://api.github.com/repos/18F/18f.github.io/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/18f.github.io/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/18f.github.io/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18f.github.io.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': True,
     'has_wiki': True,
     'homepage': 'https://18f.gsa.gov/dashboard',
     'hooks_url': 'https://api.github.com/repos/18F/18f.github.io/hooks',
     'html_url': 'https://github.com/18F/18f.github.io',
     'id': 17325636,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18f.github.io/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18f.github.io/issues/events{/number}',
     'issues_url':
     'https://api.github.com/repos/18F/18f.github.io/issues{/number}',
     'keys_url':
     'https://api.github.com/repos/18F/18f.github.io/keys{/key_id}',
     'labels_url':
     'https://api.github.com/repos/18F/18f.github.io/labels{/name}',
     'language': 'HTML',
     'languages_url':
     'https://api.github.com/repos/18F/18f.github.io/languages',
     'merges_url': 'https://api.github.com/repos/18F/18f.github.io/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18f.github.io/milestones{/number}',
     'mirror_url': None,
     'name': '18f.github.io',
     'notifications_url':
     'https://api.github.com/repos/18F/18f.github.io/notifications{?since,all,participating}',
     'open_issues': 1,
     'open_issues_count': 1,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url':
     'https://api.github.com/repos/18F/18f.github.io/pulls{/number}',
     'pushed_at': '2016-04-20T14:31:19Z',
     'releases_url':
     'https://api.github.com/repos/18F/18f.github.io/releases{/id}',
     'size': 626,
     'ssh_url': 'git@github.com:18F/18f.github.io.git',
     'stargazers_count': 5,
     'stargazers_url':
     'https://api.github.com/repos/18F/18f.github.io/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/18f.github.io/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/18f.github.io/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18f.github.io/subscription',
     'svn_url': 'https://github.com/18F/18f.github.io',
     'tags_url': 'https://api.github.com/repos/18F/18f.github.io/tags',
     'teams_url': 'https://api.github.com/repos/18F/18f.github.io/teams',
     'trees_url':
     'https://api.github.com/repos/18F/18f.github.io/git/trees{/sha}',
     'updated_at': '2015-07-20T21:28:55Z',
     'url': 'https://api.github.com/repos/18F/18f.github.io',
     'watchers': 5,
     'watchers_count': 5},
    {'archive_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/assignees{/user}',
     'blobs_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/branches{/branch}',
     'clone_url': 'https://github.com/18F/18f.gsa.gov.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/comments{/number}',
     'commits_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/contributors',
     'created_at': '2014-03-01T20:57:14Z',
     'default_branch': 'staging',
     'deployments_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/deployments',
     'description': "This repository contains 18F's website.",
     'downloads_url': 'https://api.github.com/repos/18F/18f.gsa.gov/downloads',
     'events_url': 'https://api.github.com/repos/18F/18f.gsa.gov/events',
     'fork': False,
     'forks': 195,
     'forks_count': 195,
     'forks_url': 'https://api.github.com/repos/18F/18f.gsa.gov/forks',
     'full_name': '18F/18f.gsa.gov',
     'git_commits_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18f.gsa.gov.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': True,
     'homepage': 'https://18f.gsa.gov',
     'hooks_url': 'https://api.github.com/repos/18F/18f.gsa.gov/hooks',
     'html_url': 'https://github.com/18F/18f.gsa.gov',
     'id': 17324120,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/issues/events{/number}',
     'issues_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/issues{/number}',
     'keys_url': 'https://api.github.com/repos/18F/18f.gsa.gov/keys{/key_id}',
     'labels_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/labels{/name}',
     'language': 'CSS',
     'languages_url': 'https://api.github.com/repos/18F/18f.gsa.gov/languages',
     'merges_url': 'https://api.github.com/repos/18F/18f.gsa.gov/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/milestones{/number}',
     'mirror_url': None,
     'name': '18f.gsa.gov',
     'notifications_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/notifications{?since,all,participating}',
     'open_issues': 73,
     'open_issues_count': 73,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/pulls{/number}',
     'pushed_at': '2016-06-30T03:24:30Z',
     'releases_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/releases{/id}',
     'size': 218297,
     'ssh_url': 'git@github.com:18F/18f.gsa.gov.git',
     'stargazers_count': 148,
     'stargazers_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/subscription',
     'svn_url': 'https://github.com/18F/18f.gsa.gov',
     'tags_url': 'https://api.github.com/repos/18F/18f.gsa.gov/tags',
     'teams_url': 'https://api.github.com/repos/18F/18f.gsa.gov/teams',
     'trees_url':
     'https://api.github.com/repos/18F/18f.gsa.gov/git/trees{/sha}',
     'updated_at': '2016-06-17T15:41:12Z',
     'url': 'https://api.github.com/repos/18F/18f.gsa.gov',
     'watchers': 148,
     'watchers_count': 148},
    {'archive_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/assignees{/user}',
     'blobs_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/branches{/branch}',
     'clone_url': 'https://github.com/18F/18fconsulting-proto-3.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/comments{/number}',
     'commits_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/contributors',
     'created_at': '2014-11-18T16:51:35Z',
     'default_branch': 'gh-pages',
     'deployments_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/deployments',
     'description': 'An 18F Consulting Protosketch',
     'downloads_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/downloads',
     'events_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/events',
     'fork': False,
     'forks': 0,
     'forks_count': 0,
     'forks_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/forks',
     'full_name': '18F/18fconsulting-proto-3',
     'git_commits_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/git/tags{/sha}',
     'git_url': 'git://github.com/18F/18fconsulting-proto-3.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': True,
     'has_wiki': True,
     'homepage': None,
     'hooks_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/hooks',
     'html_url': 'https://github.com/18F/18fconsulting-proto-3',
     'id': 26819560,
     'issue_comment_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/issues/events{/number}',
     'issues_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/issues{/number}',
     'keys_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/keys{/key_id}',
     'labels_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/labels{/name}',
     'language': None,
     'languages_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/languages',
     'merges_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/milestones{/number}',
     'mirror_url': None,
     'name': '18fconsulting-proto-3',
     'notifications_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/notifications{?since,all,participating}',
     'open_issues': 0,
     'open_issues_count': 0,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/pulls{/number}',
     'pushed_at': '2014-11-18T21:38:46Z',
     'releases_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/releases{/id}',
     'size': 1756,
     'ssh_url': 'git@github.com:18F/18fconsulting-proto-3.git',
     'stargazers_count': 0,
     'stargazers_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/subscription',
     'svn_url': 'https://github.com/18F/18fconsulting-proto-3',
     'tags_url': 'https://api.github.com/repos/18F/18fconsulting-proto-3/tags',
     'teams_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/teams',
     'trees_url':
     'https://api.github.com/repos/18F/18fconsulting-proto-3/git/trees{/sha}',
     'updated_at': '2014-11-18T17:06:24Z',
     'url': 'https://api.github.com/repos/18F/18fconsulting-proto-3',
     'watchers': 0,
     'watchers_count': 0},
    {'archive_url':
     'https://api.github.com/repos/18F/3d-files/{archive_format}{/ref}',
     'assignees_url':
     'https://api.github.com/repos/18F/3d-files/assignees{/user}',
     'blobs_url': 'https://api.github.com/repos/18F/3d-files/git/blobs{/sha}',
     'branches_url':
     'https://api.github.com/repos/18F/3d-files/branches{/branch}',
     'clone_url': 'https://github.com/18F/3d-files.git',
     'collaborators_url':
     'https://api.github.com/repos/18F/3d-files/collaborators{/collaborator}',
     'comments_url':
     'https://api.github.com/repos/18F/3d-files/comments{/number}',
     'commits_url': 'https://api.github.com/repos/18F/3d-files/commits{/sha}',
     'compare_url':
     'https://api.github.com/repos/18F/3d-files/compare/{base}...{head}',
     'contents_url':
     'https://api.github.com/repos/18F/3d-files/contents/{+path}',
     'contributors_url':
     'https://api.github.com/repos/18F/3d-files/contributors',
     'created_at': '2015-09-30T18:37:27Z',
     'default_branch': 'master',
     'deployments_url':
     'https://api.github.com/repos/18F/3d-files/deployments',
     'description': 'A sandbox for experimenting with 3D files',
     'downloads_url': 'https://api.github.com/repos/18F/3d-files/downloads',
     'events_url': 'https://api.github.com/repos/18F/3d-files/events',
     'fork': False,
     'forks': 1,
     'forks_count': 1,
     'forks_url': 'https://api.github.com/repos/18F/3d-files/forks',
     'full_name': '18F/3d-files',
     'git_commits_url':
     'https://api.github.com/repos/18F/3d-files/git/commits{/sha}',
     'git_refs_url':
     'https://api.github.com/repos/18F/3d-files/git/refs{/sha}',
     'git_tags_url':
     'https://api.github.com/repos/18F/3d-files/git/tags{/sha}',
     'git_url': 'git://github.com/18F/3d-files.git',
     'has_downloads': True,
     'has_issues': True,
     'has_pages': False,
     'has_wiki': False,
     'homepage': None,
     'hooks_url': 'https://api.github.com/repos/18F/3d-files/hooks',
     'html_url': 'https://github.com/18F/3d-files',
     'id': 43451578,
     'issue_comment_url':
     'https://api.github.com/repos/18F/3d-files/issues/comments{/number}',
     'issue_events_url':
     'https://api.github.com/repos/18F/3d-files/issues/events{/number}',
     'issues_url': 'https://api.github.com/repos/18F/3d-files/issues{/number}',
     'keys_url': 'https://api.github.com/repos/18F/3d-files/keys{/key_id}',
     'labels_url': 'https://api.github.com/repos/18F/3d-files/labels{/name}',
     'language': 'OpenSCAD',
     'languages_url': 'https://api.github.com/repos/18F/3d-files/languages',
     'merges_url': 'https://api.github.com/repos/18F/3d-files/merges',
     'milestones_url':
     'https://api.github.com/repos/18F/3d-files/milestones{/number}',
     'mirror_url': None,
     'name': '3d-files',
     'notifications_url':
     'https://api.github.com/repos/18F/3d-files/notifications{?since,all,participating}',
     'open_issues': 0,
     'open_issues_count': 0,
     'owner': {
         'avatar_url': 'https://avatars.githubusercontent.com/u/6233994?v=3',
         'events_url': 'https://api.github.com/users/18F/events{/privacy}',
         'followers_url': 'https://api.github.com/users/18F/followers',
         'following_url':
         'https://api.github.com/users/18F/following{/other_user}',
         'gists_url': 'https://api.github.com/users/18F/gists{/gist_id}',
         'gravatar_id': '',
         'html_url': 'https://github.com/18F',
         'id': 6233994,
         'login': '18F',
         'organizations_url': 'https://api.github.com/users/18F/orgs',
         'received_events_url':
         'https://api.github.com/users/18F/received_events',
         'repos_url': 'https://api.github.com/users/18F/repos',
         'site_admin': False,
         'starred_url':
         'https://api.github.com/users/18F/starred{/owner}{/repo}',
         'subscriptions_url': 'https://api.github.com/users/18F/subscriptions',
         'type': 'Organization',
         'url': 'https://api.github.com/users/18F'
     },
     'private': False,
     'pulls_url': 'https://api.github.com/repos/18F/3d-files/pulls{/number}',
     'pushed_at': '2016-06-20T19:34:49Z',
     'releases_url': 'https://api.github.com/repos/18F/3d-files/releases{/id}',
     'size': 22,
     'ssh_url': 'git@github.com:18F/3d-files.git',
     'stargazers_count': 1,
     'stargazers_url': 'https://api.github.com/repos/18F/3d-files/stargazers',
     'statuses_url':
     'https://api.github.com/repos/18F/3d-files/statuses/{sha}',
     'subscribers_url':
     'https://api.github.com/repos/18F/3d-files/subscribers',
     'subscription_url':
     'https://api.github.com/repos/18F/3d-files/subscription',
     'svn_url': 'https://github.com/18F/3d-files',
     'tags_url': 'https://api.github.com/repos/18F/3d-files/tags',
     'teams_url': 'https://api.github.com/repos/18F/3d-files/teams',
     'trees_url': 'https://api.github.com/repos/18F/3d-files/git/trees{/sha}',
     'updated_at': '2016-06-20T19:34:48Z',
     'url': 'https://api.github.com/repos/18F/3d-files',
     'watchers': 1,
     'watchers_count': 1}
]

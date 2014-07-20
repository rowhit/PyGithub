# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime

import PyGithub.Blocking
import PyGithub.Blocking.Dir
import PyGithub.Blocking.File
import PyGithub.Blocking.User

import PyGithub.Blocking.tests.Framework as Framework
from PyGithub.Blocking.tests.Framework import *


class RepositoryTestCase(Framework.SimpleLoginTestCase):
    def testAttributesOfOwnedRepository(self):
        r = self.g.get_repo("jacquev6/PyGithub")
        self.assertEqual(r.archive_url, "https://api.github.com/repos/jacquev6/PyGithub/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "https://api.github.com/repos/jacquev6/PyGithub/assignees{/user}")
        self.assertEqual(r.blobs_url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "https://api.github.com/repos/jacquev6/PyGithub/branches{/branch}")
        self.assertEqual(r.clone_url, "https://github.com/jacquev6/PyGithub.git")
        self.assertEqual(r.collaborators_url, "https://api.github.com/repos/jacquev6/PyGithub/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "https://api.github.com/repos/jacquev6/PyGithub/comments{/number}")
        self.assertEqual(r.commits_url, "https://api.github.com/repos/jacquev6/PyGithub/commits{/sha}")
        self.assertEqual(r.compare_url, "https://api.github.com/repos/jacquev6/PyGithub/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "https://api.github.com/repos/jacquev6/PyGithub/contents/{+path}")
        self.assertEqual(r.contributors_url, "https://api.github.com/repos/jacquev6/PyGithub/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2012, 2, 25, 12, 53, 47))
        self.assertEqual(r.default_branch, "master")
        self.assertEqual(r.description, "Python library implementing the full Github API v3")
        self.assertEqual(r.downloads_url, "https://api.github.com/repos/jacquev6/PyGithub/downloads")
        self.assertEqual(r.events_url, "https://api.github.com/repos/jacquev6/PyGithub/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks_count, 89)
        self.assertEqual(r.forks_url, "https://api.github.com/repos/jacquev6/PyGithub/forks")
        self.assertEqual(r.full_name, "jacquev6/PyGithub")
        self.assertEqual(r.git_commits_url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "https://api.github.com/repos/jacquev6/PyGithub/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.com/jacquev6/PyGithub.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, "http://jacquev6.github.com/PyGithub")
        self.assertEqual(r.hooks_url, "https://api.github.com/repos/jacquev6/PyGithub/hooks")
        self.assertEqual(r.html_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(r.id, 3544490)
        self.assertEqual(r.issue_comment_url, "https://api.github.com/repos/jacquev6/PyGithub/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "https://api.github.com/repos/jacquev6/PyGithub/issues/events{/number}")
        self.assertEqual(r.issues_url, "https://api.github.com/repos/jacquev6/PyGithub/issues{/number}")
        self.assertEqual(r.keys_url, "https://api.github.com/repos/jacquev6/PyGithub/keys{/key_id}")
        self.assertEqual(r.labels_url, "https://api.github.com/repos/jacquev6/PyGithub/labels{/name}")
        self.assertEqual(r.language, "Python")
        self.assertEqual(r.languages_url, "https://api.github.com/repos/jacquev6/PyGithub/languages")
        self.assertEqual(r.merges_url, "https://api.github.com/repos/jacquev6/PyGithub/merges")
        self.assertEqual(r.milestones_url, "https://api.github.com/repos/jacquev6/PyGithub/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "PyGithub")
        self.assertEqual(r.network_count, 89)
        self.assertEqual(r.notifications_url, "https://api.github.com/repos/jacquev6/PyGithub/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues_count, 26)
        self.assertEqual(r.owner.login, "jacquev6")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.permissions.admin, True)
        self.assertEqual(r.permissions.push, True)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "https://api.github.com/repos/jacquev6/PyGithub/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2013, 12, 16, 2, 11, 29))
        self.assertEqual(r.releases_url, "https://api.github.com/repos/jacquev6/PyGithub/releases{/id}")
        self.assertEqual(r.size, 8785)
        self.assertEqual(r.ssh_url, "git@github.com:jacquev6/PyGithub.git")
        self.assertEqual(r.stargazers_count, 315)
        self.assertEqual(r.stargazers_url, "https://api.github.com/repos/jacquev6/PyGithub/stargazers")
        self.assertEqual(r.statuses_url, "https://api.github.com/repos/jacquev6/PyGithub/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 32)
        self.assertEqual(r.subscribers_url, "https://api.github.com/repos/jacquev6/PyGithub/subscribers")
        self.assertEqual(r.subscription_url, "https://api.github.com/repos/jacquev6/PyGithub/subscription")
        self.assertEqual(r.svn_url, "https://github.com/jacquev6/PyGithub")
        self.assertEqual(r.tags_url, "https://api.github.com/repos/jacquev6/PyGithub/tags")
        self.assertEqual(r.teams_url, "https://api.github.com/repos/jacquev6/PyGithub/teams")
        self.assertEqual(r.trees_url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2013, 12, 19, 9, 39, 44))
        self.assertEqual(r.url, "https://api.github.com/repos/jacquev6/PyGithub")
        self.assertEqual(r.watchers_count, 315)

    def testAttributesOfOtherRepository(self):
        r = self.g.get_repo("nvie/gitflow")
        self.assertEqual(r.archive_url, "https://api.github.com/repos/nvie/gitflow/{archive_format}{/ref}")
        self.assertEqual(r.assignees_url, "https://api.github.com/repos/nvie/gitflow/assignees{/user}")
        self.assertEqual(r.blobs_url, "https://api.github.com/repos/nvie/gitflow/git/blobs{/sha}")
        self.assertEqual(r.branches_url, "https://api.github.com/repos/nvie/gitflow/branches{/branch}")
        self.assertEqual(r.clone_url, "https://github.com/nvie/gitflow.git")
        self.assertEqual(r.collaborators_url, "https://api.github.com/repos/nvie/gitflow/collaborators{/collaborator}")
        self.assertEqual(r.comments_url, "https://api.github.com/repos/nvie/gitflow/comments{/number}")
        self.assertEqual(r.commits_url, "https://api.github.com/repos/nvie/gitflow/commits{/sha}")
        self.assertEqual(r.compare_url, "https://api.github.com/repos/nvie/gitflow/compare/{base}...{head}")
        self.assertEqual(r.contents_url, "https://api.github.com/repos/nvie/gitflow/contents/{+path}")
        self.assertEqual(r.contributors_url, "https://api.github.com/repos/nvie/gitflow/contributors")
        self.assertEqual(r.created_at, datetime.datetime(2010, 1, 20, 23, 14, 12))
        self.assertEqual(r.default_branch, "develop")
        self.assertEqual(r.description, "Git extensions to provide high-level repository operations for Vincent Driessen's branching model.")
        self.assertEqual(r.downloads_url, "https://api.github.com/repos/nvie/gitflow/downloads")
        self.assertEqual(r.events_url, "https://api.github.com/repos/nvie/gitflow/events")
        self.assertEqual(r.fork, False)
        self.assertEqual(r.forks_count, 897)
        self.assertEqual(r.forks_url, "https://api.github.com/repos/nvie/gitflow/forks")
        self.assertEqual(r.full_name, "nvie/gitflow")
        self.assertEqual(r.git_commits_url, "https://api.github.com/repos/nvie/gitflow/git/commits{/sha}")
        self.assertEqual(r.git_refs_url, "https://api.github.com/repos/nvie/gitflow/git/refs{/sha}")
        self.assertEqual(r.git_tags_url, "https://api.github.com/repos/nvie/gitflow/git/tags{/sha}")
        self.assertEqual(r.git_url, "git://github.com/nvie/gitflow.git")
        self.assertEqual(r.has_issues, True)
        self.assertEqual(r.has_wiki, True)
        self.assertEqual(r.homepage, "http://nvie.com/posts/a-successful-git-branching-model/")
        self.assertEqual(r.hooks_url, "https://api.github.com/repos/nvie/gitflow/hooks")
        self.assertEqual(r.html_url, "https://github.com/nvie/gitflow")
        self.assertEqual(r.id, 481366)
        self.assertEqual(r.issue_comment_url, "https://api.github.com/repos/nvie/gitflow/issues/comments/{number}")
        self.assertEqual(r.issue_events_url, "https://api.github.com/repos/nvie/gitflow/issues/events{/number}")
        self.assertEqual(r.issues_url, "https://api.github.com/repos/nvie/gitflow/issues{/number}")
        self.assertEqual(r.keys_url, "https://api.github.com/repos/nvie/gitflow/keys{/key_id}")
        self.assertEqual(r.labels_url, "https://api.github.com/repos/nvie/gitflow/labels{/name}")
        self.assertEqual(r.language, "Shell")
        self.assertEqual(r.languages_url, "https://api.github.com/repos/nvie/gitflow/languages")
        self.assertEqual(r.merges_url, "https://api.github.com/repos/nvie/gitflow/merges")
        self.assertEqual(r.milestones_url, "https://api.github.com/repos/nvie/gitflow/milestones{/number}")
        self.assertEqual(r.mirror_url, None)
        self.assertEqual(r.name, "gitflow")
        self.assertEqual(r.network_count, 897)
        self.assertEqual(r.notifications_url, "https://api.github.com/repos/nvie/gitflow/notifications{?since,all,participating}")
        self.assertEqual(r.open_issues_count, 176)
        self.assertEqual(r.owner.login, "nvie")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.permissions.admin, False)
        self.assertEqual(r.permissions.push, False)
        self.assertEqual(r.permissions.pull, True)
        self.assertEqual(r.private, False)
        self.assertEqual(r.pulls_url, "https://api.github.com/repos/nvie/gitflow/pulls{/number}")
        self.assertEqual(r.pushed_at, datetime.datetime(2012, 9, 26, 10, 25, 25))
        self.assertEqual(r.releases_url, "https://api.github.com/repos/nvie/gitflow/releases{/id}")
        self.assertEqual(r.size, 5662)
        self.assertEqual(r.ssh_url, "git@github.com:nvie/gitflow.git")
        self.assertEqual(r.stargazers_count, 7973)
        self.assertEqual(r.stargazers_url, "https://api.github.com/repos/nvie/gitflow/stargazers")
        self.assertEqual(r.statuses_url, "https://api.github.com/repos/nvie/gitflow/statuses/{sha}")
        self.assertEqual(r.subscribers_count, 369)
        self.assertEqual(r.subscribers_url, "https://api.github.com/repos/nvie/gitflow/subscribers")
        self.assertEqual(r.subscription_url, "https://api.github.com/repos/nvie/gitflow/subscription")
        self.assertEqual(r.svn_url, "https://github.com/nvie/gitflow")
        self.assertEqual(r.tags_url, "https://api.github.com/repos/nvie/gitflow/tags")
        self.assertEqual(r.teams_url, "https://api.github.com/repos/nvie/gitflow/teams")
        self.assertEqual(r.trees_url, "https://api.github.com/repos/nvie/gitflow/git/trees{/sha}")
        self.assertEqual(r.updated_at, datetime.datetime(2013, 12, 20, 5, 57, 21))
        self.assertEqual(r.url, "https://api.github.com/repos/nvie/gitflow")
        self.assertEqual(r.watchers_count, 7973)

    def testAttributesOfFork(self):
        r = self.g.get_repo("lentty/PyGithub")
        self.assertEqual(r.fork, True)
        self.assertEqual(r.parent.owner.login, "akfish")
        self.assertEqual(r.source.owner.login, "jacquev6")

    def testAttributesOfOrganizationRepository(self):
        # @todoSomeday Open an issue because repo.owner contains silly attributes when owner is an org (following_url, etc. See deprecated_attributes in Organization.yml)
        # @todoSomeday Open an issue because repo contains a "organization" attribute when owner is an org
        r = self.g.get_repo("graphite-project/whisper")
        self.assertEqual(r.owner.login, "graphite-project")
        self.assertEqual(r.owner.type, "Organization")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.Organization.Organization))

    def testAttributesOfForkOfOrganizationRepository(self):
        r = self.g.get_repo("ryansndrs/whisper")
        self.assertEqual(r.owner.login, "ryansndrs")
        self.assertEqual(r.owner.type, "User")
        self.assertTrue(isinstance(r.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.parent.owner.login, "richg")
        self.assertEqual(r.parent.owner.type, "User")
        self.assertTrue(isinstance(r.parent.owner, PyGithub.Blocking.User.User))
        self.assertEqual(r.source.owner.login, "graphite-project")
        self.assertEqual(r.source.owner.type, "Organization")
        self.assertTrue(isinstance(r.source.owner, PyGithub.Blocking.Organization.Organization))

    def testGetStargazers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_stargazers(per_page=3)
        self.assertEqual(users[0].login, "ybakos")
        self.assertEqual(users[1].login, "huxley")

    def testGetAssignees(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_assignees()
        self.assertEqual(users[0].login, "jacquev6")

    def testGetAssignees_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_assignees(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")

    def testHasInAssignees(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        self.assertTrue(repo.has_in_assignees("jacquev6"))
        self.assertFalse(repo.has_in_assignees("nvie"))

    def testGetCollaborators(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_collaborators()
        self.assertEqual(users[0].login, "jacquev6")

    def testGetCollaborators_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_collaborators(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")

    def testAddRemoveCollaborators(self):
        repo = self.g.get_repo("jacquev6/PyGithub")
        self.assertFalse(repo.has_in_collaborators("Lyloa"))
        repo.add_to_collaborators("Lyloa")
        self.assertTrue(repo.has_in_collaborators("Lyloa"))
        repo.remove_from_collaborators("Lyloa")
        self.assertFalse(repo.has_in_collaborators("Lyloa"))

    def testGetContributors(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors()
        self.assertEqual(len(list(users)), 25)
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[0].contributions, 1041)
        self.assertTrue(isinstance(users[0], PyGithub.Blocking.User.User))
        self.assertEqual(users[1].login, "akfish")
        self.assertEqual(users[1].type, "User")

    def testGetContributors_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors(anon=True, per_page=3)
        self.assertEqual(len(list(users)), 26)
        self.assertEqual(users[17].type, "Anonymous")
        self.assertEqual(users[17].name, "Petteri Muilu")
        self.assertEqual(users[17].contributions, 1)
        self.assertTrue(isinstance(users[17], PyGithub.Blocking.Repository.Repository.AnonymousContributor))

    def testGetContributorsWithAnonExplicitelyFalse(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_contributors(anon=False)
        self.assertEqual(len(list(users)), 25)

    def testUpdatingContributorKeepsContributions(self):
        user = self.g.get_repo("jacquev6/JellyNoSolver").get_contributors(per_page=3)[0]
        self.assertEqual(user.contributions, 117)
        user.update()
        self.assertEqual(user.contributions, 117)

    @Framework.SharesDataWith(testUpdatingContributorKeepsContributions)
    def testLazyCompletionOfContributorKeepsContributions(self):
        user = self.g.get_repo("jacquev6/JellyNoSolver").get_contributors(per_page=3)[0]
        self.assertEqual(user.contributions, 117)
        self.assertEqual(user.name, "Vincent Jacques")
        self.assertEqual(user.contributions, 117)

    def testGetSubscribers(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers()
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testGetSubscribers_allParameters(self):
        users = self.g.get_repo("jacquev6/PyGithub").get_subscribers(per_page=3)
        self.assertEqual(users[0].login, "jacquev6")
        self.assertEqual(users[1].login, "equus12")

    def testEditNothing(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        repo.edit()

    def testEditName(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.name, "JellyNoSolver")
        repo.edit(name="JellyNoSolver2")
        self.assertEqual(repo.name, "JellyNoSolver2")
        repo.edit(name="JellyNoSolver")
        self.assertEqual(repo.name, "JellyNoSolver")
        with self.assertRaises(TypeError):
            repo.edit(name=PyGithub.Blocking.Reset)

    def testEditDescription(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")
        repo.edit(description=PyGithub.Blocking.Reset)
        self.assertEqual(repo.description, None)
        repo.edit(description="Solver for Jelly no Puzzle")
        self.assertEqual(repo.description, "Solver for Jelly no Puzzle")

    def testEditHomepage(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.homepage, None)
        repo.edit(homepage="http://foo.bar")
        self.assertEqual(repo.homepage, "http://foo.bar")
        repo.edit(homepage=PyGithub.Blocking.Reset)
        self.assertEqual(repo.homepage, None)

    def testEditPrivate(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.private, False)
        repo.edit(private=True)
        self.assertEqual(repo.private, True)
        repo.edit(private=False)
        self.assertEqual(repo.private, False)
        with self.assertRaises(TypeError):
            repo.edit(private=PyGithub.Blocking.Reset)

    def testEditHasIssues(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.has_issues, False)
        repo.edit(has_issues=True)
        self.assertEqual(repo.has_issues, True)
        repo.edit(has_issues=False)
        self.assertEqual(repo.has_issues, False)
        with self.assertRaises(TypeError):
            repo.edit(has_issues=PyGithub.Blocking.Reset)

    def testEditHasWiki(self):
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.has_wiki, False)
        repo.edit(has_wiki=True)
        self.assertEqual(repo.has_wiki, True)
        repo.edit(has_wiki=False)
        self.assertEqual(repo.has_wiki, False)
        with self.assertRaises(TypeError):
            repo.edit(has_wiki=PyGithub.Blocking.Reset)

    def testEditDefaultBranch(self):
        # @todoBeta test with a Branch instance
        repo = self.g.get_repo("jacquev6/JellyNoSolver")
        self.assertEqual(repo.default_branch, "master")
        repo.edit(default_branch="develop")
        self.assertEqual(repo.default_branch, "develop")
        repo.edit(default_branch="master")
        self.assertEqual(repo.default_branch, "master")
        with self.assertRaises(TypeError):
            repo.edit(default_branch=PyGithub.Blocking.Reset)

    def testGetForks(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks()
        self.assertEqual(repos[0].owner.login, "Web5design")
        self.assertEqual(repos[1].owner.login, "pelson")

    def testGetForks_allParameters(self):
        repos = self.g.get_repo("jacquev6/PyGithub").get_forks(sort="stargazers", per_page=3)
        self.assertEqual(repos[0].owner.login, "roverdotcom")
        self.assertEqual(repos[0].stargazers_count, 1)
        self.assertEqual(repos[1].owner.login, "pmuilu")
        self.assertEqual(repos[1].stargazers_count, 1)

    def testGetTeamsOfPersonalRepo(self):
        teams = self.g.get_repo("jacquev6/PyGithub").get_teams()
        self.assertEqual(len(list(teams)), 0)

    def testGetTeamsOfOrgRepo(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams()
        self.assertEqual(teams[0].name, "Members")

    def testGetTeams_allParameters(self):
        teams = self.g.get_repo("BeaverSoftware/FatherBeaver").get_teams(per_page=1)
        self.assertEqual(teams[0].name, "Members")

    def testGetKeys(self):
        keys = self.g.get_repo("jacquev6/CodingDojos").get_keys()
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys[0].id, 6941367)

    def testGetKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").get_key(6941367)
        self.assertEqual(key.title, "dojo@dojo")

    def testCreateKey(self):
        key = self.g.get_repo("jacquev6/CodingDojos").create_key("vincent@test", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkQih2DtSwBzLUtSNYEKULlI5M1qa6vnq42xt9qZpkLav3G9eD/GqJRST+zZMsyfpP62PtiYKXJdLJX2MQIzUgI2PzNy+iMy+ldiTEABYEOCa+BH9+x2R5xXGlmmCPblpamx3kstGtCTa3LSkyIvxbt5vjbXCyThhJaSKyh+42Uedcz7l0y/TODhnkpid/5eiBz6k0VEbFfhM6h71eBdCFpeMJIhGaPTjbKsEjXIK0SRe0v0UQnpXJQkhAINbm+q/2yjt7zwBF74u6tQjRqJK7vQO2k47ZmFMAGeIxS6GheI+JPmwtHkxvfaJjy2lIGX+rt3lkW8xEUxiMTlxeh+0R")
        self.assertEqual(key.id, 7229238)

    def testGetReadme(self):
        readme = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_readme()
        self.assertEqual(readme.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testGetReadme_allParameters(self):
        # @todoAlpha ref can also be a GitObject
        readme = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_readme(ref="develop")
        self.assertEqual(readme.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=develop")

    def testGetFileContents(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("README.md")
        self.assertIsInstance(f, PyGithub.Blocking.File.File)
        self.assertEqual(f.type, "file")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/README.md?ref=master")

    def testGetSymlinkContents(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("SymLink.rst")
        self.assertIsInstance(f, PyGithub.Blocking.SymLink.SymLink)
        self.assertEqual(f.type, "symlink")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/SymLink.rst?ref=master")

    def testGetSubmoduleContents(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("PyGithub")
        self.assertIsInstance(f, PyGithub.Blocking.Submodule.Submodule)
        self.assertEqual(f.type, "submodule")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/PyGithub?ref=master")

    def testGetFileContentsWithinDirectory(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("a/foo.md")
        self.assertIsInstance(f, PyGithub.Blocking.File.File)
        self.assertEqual(f.type, "file")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/a/foo.md?ref=master")

    def testGetFileContents_allParameters(self):
        f = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("toto.md", ref="develop")
        self.assertIsInstance(f, PyGithub.Blocking.File.File)
        self.assertEqual(f.type, "file")
        self.assertEqual(f.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/toto.md?ref=develop")

    def testGetRootDirContents(self):
        contents = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_contents("")
        self.assertIsInstance(contents, list)
        self.assertEqual(len(contents), 5)
        self.assertIsInstance(contents[0], PyGithub.Blocking.File.File)
        self.assertIsInstance(contents[1], PyGithub.Blocking.Submodule.Submodule)
        self.assertIsInstance(contents[2], PyGithub.Blocking.File.File)
        self.assertIsInstance(contents[3], PyGithub.Blocking.SymLink.SymLink)
        self.assertIsInstance(contents[4], PyGithub.Blocking.Dir.Dir)
        self.assertEqual(contents[0].type, "file")
        self.assertEqual(contents[1].type, "file")  # https://github.com/github/developer.github.com/commit/1b329b04cece9f3087faa7b1e0382317a9b93490
        self.assertEqual(contents[2].type, "file")
        self.assertEqual(contents[3].type, "symlink")
        self.assertEqual(contents[4].type, "dir")

    def testCreateFile(self):
        cc = self.g.get_repo("jacquev6/PyGithubIntegrationTests").create_file("hello.md", "Add hello.md", "SGVsbG8sIFdvcmxkIQ==")
        self.assertEqual(cc.content.size, 13)
        self.assertEqual(cc.content.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/hello.md?ref=master")
        self.assertEqual(cc.commit.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/git/commits/4289f250d2144c637b255e5765ef0fac00f4d8d4")

    def testCreateFile_allParameters(self):
        cc = self.g.get_repo("jacquev6/PyGithubIntegrationTests").create_file(
            "hello.md",
            "Add hello.md",
            "SGVsbG8sIFdvcmxkIQ==",
            branch="develop",
            committer={"name": "John Doe", "email": "john@doe.com"},
            author={"name": "Jane Doe", "email": "jane@doe.com"},  # @todoAlpha Use a GitCommit.Author? Does the api accept an undocumented date?
        )
        self.assertEqual(cc.content.size, 13)
        self.assertEqual(cc.content.url, "https://api.github.com/repos/jacquev6/PyGithubIntegrationTests/contents/hello.md?ref=develop")
        self.assertEqual(cc.commit.author.name, "Jane Doe")
        self.assertEqual(cc.commit.committer.email, "john@doe.com")

    def testCreateGitBlob(self):
        blob = self.g.get_repo("jacquev6/PyGithubIntegrationTests").create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    def testGetGitBlob(self):
        blob = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_blob("3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(blob.content, "VGhpcyBpcyBzb21lIGNvbnRlbnQ=\n")

    def testGetGitTree(self):
        tree = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_git_tree("83e7163e208723d366a758b7cbef1042e77b9e8b")
        self.assertEqual(tree.sha, "83e7163e208723d366a758b7cbef1042e77b9e8b")

    def testGetIssue(self):
        issue = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_issue(1)
        self.assertEqual(issue.title, "First issue")

    def testGetLabel(self):
        label = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_label("bug")
        self.assertEqual(label.color, "fc2929")

    # @todoAlpha follow-up with issue opened to github for labels with % sign
    # def testGetLabel_weirdName(self):
    #     label = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_label("space é % space")
    #     self.assertEqual(label.name, "space é % space".decode("utf-8"))

    def testGetMilestone(self):
        milestone = self.g.get_repo("jacquev6/PyGithubIntegrationTests").get_milestone(1)
        self.assertEqual(milestone.title, "First milestone")


class RepositoryGitStuff(TestCase):
    @Enterprise.User(1)
    def testGetBranches(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        branches = r.get_branches()
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise.User(1)
    def testGetBranches_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        branches = r.get_branches(per_page=1)
        self.assertEqual([b.name for b in branches], ["develop", "master"])

    @Enterprise.User(1)
    def testGetBranch(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        b = r.get_branch("develop")
        self.assertEqual(b.commit.author.login, "ghe-user-1")

    # @todoSomeday Consider opening an issue to GitHub to fix inconsistency with Branch:
    # Branch.update can be tested like this if Branch is modified to take its url attribute from _links["self"]
    # but _links is returned only by Repository.get_branch, not by Repository.get_branches
    # so we have no way to make Branch generaly updatable
    # @Enterprise.User(1)
    # def testUpdateBranch(self):
    #     r = self.g.get_repo("ghe-user-1/repo-user-1-1")
    #     b = r.get_branch("test_update")
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     self.assertFalse(b.update())
    #     self.assertEqual(b.commit.sha, "e078f69fb050b75fe5f3c7aa70adc24d692e75b8")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="7820fadc2429652016611e98fdc21766ba075161")
    #     self.assertTrue(b.update())
    #     self.assertEqual(b.commit.sha, "7820fadc2429652016611e98fdc21766ba075161")
    #     r.get_git_ref("refs/heads/test_update").edit(sha="e078f69fb050b75fe5f3c7aa70adc24d692e75b8", force=True)

    @Enterprise.User(1)
    def testGetCommits(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        commits = r.get_commits()
        self.assertEqual([c.sha for c in commits], ["e078f69fb050b75fe5f3c7aa70adc24d692e75b8"])

    @Enterprise.User(1)
    def testGetCommits_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        commits = r.get_commits(sha="7820fad", path="README.md", author="ghe-user-1", since=datetime.datetime(2014, 1, 1, 0, 0, 0), until=datetime.datetime(2014, 12, 31, 23, 59, 59), per_page=1)
        self.assertEqual([c.sha for c in commits], ["7820fadc2429652016611e98fdc21766ba075161", "e078f69fb050b75fe5f3c7aa70adc24d692e75b8"])

    @Enterprise.User(1)
    def testGetCommit(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        c = r.get_commit("7820fad")
        self.assertEqual(c.author.login, "ghe-user-1")
        self.assertEqual(c.commit.comment_count, 0)  # @todoAlpha Understand why this attribute is returned here, but not in r.get_git_commit

    @Enterprise.User(1)
    def testGetTags(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tags = r.get_tags()
        self.assertEqual([t.name for t in tags], ["v0.1-beta.2", "v0.1-beta.1"])

    @Enterprise.User(1)
    def testGetTags_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tags = r.get_tags(per_page=1)
        self.assertEqual([t.name for t in tags], ["v0.1-beta.2", "v0.1-beta.1"])

    @Enterprise.User(1)
    def testGetGitTag(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        t = r.get_git_tag("43bafe50b11378c5546dbef02032941bb8a46099")
        self.assertEqual(t.sha, "43bafe50b11378c5546dbef02032941bb8a46099")

    @Enterprise.User(1)
    def testGetGitRefs(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        refs = r.get_git_refs()
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/v0.1-beta.1", "refs/tags/v0.1-beta.2"])

    @Enterprise.User(1)
    def testGetGitRefs_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        refs = r.get_git_refs(per_page=2)
        self.assertEqual([r.ref for r in refs], ["refs/heads/develop", "refs/heads/master", "refs/tags/v0.1-beta.1", "refs/tags/v0.1-beta.2"])

    @Enterprise.User(1)
    def testGetGitRef(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.get_git_ref("refs/heads/develop")
        # @todoAlpha Test get_git_ref with a string not starting with "refs/"
        self.assertEqual(ref.ref, "refs/heads/develop")

    @Enterprise.User(1)
    def testCreateGitBlob(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        blob = r.create_git_blob("This is some content", "utf8")
        self.assertEqual(blob.sha, "3daf0da6bca38181ab52610dd6af6e92f1a5469d")

    @Enterprise.User(1)
    def testCreateGitTree(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tree = r.create_git_tree(tree=[{"path": "test.txt", "mode": "100644", "type": "blob", "sha": "3daf0da6bca38181ab52610dd6af6e92f1a5469d"}])
        self.assertEqual(tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")

    @Enterprise.User(1)
    def testCreateInitialGitCommit(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[])
        self.assertEqual(commit.message, "first commit")
        self.assertEqual(commit.tree.sha, "65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(len(commit.parents), 0)

    @Enterprise.User(1)
    def testCreateInitialGitCommit_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="first commit", parents=[], author={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"}, committer={"name": "Jane Doe", "email": "jane@doe.com", "date": "2000-01-01T00:00:00Z"})
        self.assertEqual(commit.author.name, "John Doe")
        self.assertEqual(commit.author.email, "john@doe.com")
        self.assertEqual(commit.author.date, datetime.datetime(1999, 12, 31, 23, 59, 59))
        self.assertEqual(commit.committer.name, "Jane Doe")
        self.assertEqual(commit.committer.email, "jane@doe.com")
        self.assertEqual(commit.committer.date, datetime.datetime(2000, 1, 1, 0, 0, 0))

    @Enterprise.User(1)
    def testCreateSubsequentGitCommit(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        commit = r.create_git_commit(tree="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", message="second commit", parents=["7b96628d495239a926958bb5b8b935245668cc6a"])
        self.assertEqual(commit.parents[0].sha, "7b96628d495239a926958bb5b8b935245668cc6a")

    @Enterprise.User(1)
    def testCreateCommitGitRef(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        self.assertEqual(ref.ref, "refs/tests/commit_ref")
        self.assertEqual(ref.object.type, "commit")
        self.assertIsInstance(ref.object, PyGithub.Blocking.GitCommit.GitCommit)
        ref.delete()

    @Enterprise.User(1)
    def testCreateTreeGitRef(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.create_git_ref(ref="refs/tests/tree_ref", sha="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad")
        self.assertEqual(ref.ref, "refs/tests/tree_ref")
        self.assertEqual(ref.object.type, "tree")
        # @todoAlpha self.assertIsInstance(ref.object, PyGithub.Blocking.Gittree.Gittree)
        ref.delete()

    @Enterprise.User(1)
    def testCreateBlobGitRef(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.create_git_ref(ref="refs/tests/blob_ref", sha="3daf0da6bca38181ab52610dd6af6e92f1a5469d")
        self.assertEqual(ref.ref, "refs/tests/blob_ref")
        self.assertEqual(ref.object.type, "blob")
        # @todoAlpha self.assertIsInstance(ref.object, PyGithub.Blocking.Gitblob.Gitblob)
        ref.delete()

    @Enterprise.User(1)
    def testCreateExistingGitRef(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        ref = r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_ref(ref="refs/tests/commit_ref", sha="7b96628d495239a926958bb5b8b935245668cc6a")
        ref.delete()

    @Enterprise.User(1)
    def testCreateCommitGitTag(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="commit")
        self.assertEqual(tag.object.type, "commit")
        self.assertIsInstance(tag.object, PyGithub.Blocking.GitCommit.GitCommit)

    @Enterprise.User(1)
    def testCreateGitTagWithBadType(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        with self.assertRaises(PyGithub.Blocking.UnprocessableEntityException):
            r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="blob")

    @Enterprise.User(1)
    def testCreateGitTag_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tag = r.create_git_tag(tag="commit_tag", message="This is a commit tag", object="7b96628d495239a926958bb5b8b935245668cc6a", type="commit", tagger={"name": "John Doe", "email": "john@doe.com", "date": "1999-12-31T23:59:59Z"})
        self.assertEqual(tag.tagger.name, "John Doe")
        self.assertEqual(tag.tagger.email, "john@doe.com")
        self.assertEqual(tag.tagger.date, datetime.datetime(1999, 12, 31, 23, 59, 59))

    @Enterprise.User(1)
    def testCreateTreeGitTag(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tag = r.create_git_tag(tag="tree_tag", message="This is a tree tag", object="65208a85edf4a0d2c2f757ab655fb3ba2cd63bad", type="tree")
        self.assertEqual(tag.object.type, "tree")
        # @todoAlpha self.assertIsInstance(tag.object, PyGithub.Blocking.GitTree.GitTree)

    @Enterprise.User(1)
    def testCreateBlobGitTag(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        tag = r.create_git_tag(tag="blob_tag", message="This is a blob tag", object="3daf0da6bca38181ab52610dd6af6e92f1a5469d", type="blob")
        self.assertEqual(tag.object.type, "blob")
        # @todoAlpha self.assertIsInstance(tag.object, PyGithub.Blocking.GitBlob.GitBlob)


class RepositoryIssues(TestCase):
    @Enterprise.User(2)
    def testCreateIssue(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.create_issue("Created by PyGithub")
        self.assertEqual(issue.title, "Created by PyGithub")
        self.assertIsNone(issue.body)
        self.assertIsNone(issue.assignee)
        self.assertIsNone(issue.milestone)
        self.assertEqual(len(issue.labels), 0)

    @Enterprise.User(1)
    def testCreateIssue_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issue = r.create_issue("Also created by PyGithub", body="Body", assignee="ghe-user-1", milestone=1, labels=["question"])
        self.assertEqual(issue.title, "Also created by PyGithub")
        self.assertEqual(issue.body, "Body")
        self.assertEqual(issue.assignee.login, "ghe-user-1")
        self.assertEqual(issue.milestone.number, 1)
        self.assertEqual(len(issue.labels), 1)

    @Enterprise.User(2)
    def testGetIssues(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issues = r.get_issues()
        self.assertEqual([i.title for i in issues], ["Also created by PyGithub", "Created by PyGithub", "First issue"])

    @Enterprise.User(2)
    def testGetIssues_allParameters(self):
        r = self.g.get_repo("ghe-user-1/repo-user-1-1")
        issues = r.get_issues(milestone=1, state="open", assignee="ghe-user-1", creator="ghe-user-1", mentioned="ghe-user-2", labels=["question"], sort="created", direction="asc", since=datetime.datetime(2014, 1, 1, 0, 0, 0), per_page=1)
        self.assertEqual([i.title for i in issues], ["Also created by PyGithub"])

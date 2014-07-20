# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

import datetime


class _Reset:
    pass
Reset = _Reset()


def dictionary(**args):
    d = dict()
    for k, v in args.iteritems():
        if v is Reset:
            d[k] = None
        elif v is not None:
            d[k] = v
    return d


def normalizeLabelName(label):
    import PyGithub.Blocking.Label
    if isinstance(label, PyGithub.Blocking.Label.Label):
        return label.name
    elif isinstance(label, basestring):
        return label
    else:
        raise TypeError()


def normalizeMilestoneNumber(milestone):
    import PyGithub.Blocking.Milestone
    if isinstance(milestone, PyGithub.Blocking.Milestone.Milestone):
        return milestone.number
    elif isinstance(milestone, int):
        return milestone
    else:
        raise TypeError()


def normalizeMilestoneNumberReset(milestone):
    if milestone is Reset:
        return milestone
    else:
        return normalizeMilestoneNumber(milestone)


def normalizeUserLogin(user):
    import PyGithub.Blocking.User
    if isinstance(user, PyGithub.Blocking.User.User):
        return user.login
    elif isinstance(user, basestring):
        return user
    else:
        raise TypeError()


def normalizeUserLoginReset(user):
    if user is Reset:
        return user
    else:
        return normalizeUserLogin(user)


def normalizeRepositoryFullName(repo):
    import PyGithub.Blocking.Repository
    if isinstance(repo, PyGithub.Blocking.Repository.Repository):
        return (repo.owner.login, repo.name)
    elif isinstance(repo, basestring):
        return repo.split("/")
    elif isinstance(repo, tuple):
        return repo
    else:
        raise TypeError()


def normalizeUserId(user):
    import PyGithub.Blocking.User
    if isinstance(user, PyGithub.Blocking.User.User):
        return user.id
    elif isinstance(user, int):
        return user
    else:
        raise TypeError()


def normalizeRepositoryId(repo):
    import PyGithub.Blocking.Repository
    if isinstance(repo, PyGithub.Blocking.Repository.Repository):
        return repo.id
    elif isinstance(repo, int):
        return repo
    else:
        raise TypeError()


def normalizeTeamId(team):
    import PyGithub.Blocking.Team
    if isinstance(team, PyGithub.Blocking.Team.Team):
        return team.id
    elif isinstance(team, int):
        return team
    else:
        raise TypeError()


def normalizeString(s):
    if isinstance(s, basestring):
        return s
    else:
        raise TypeError()


def normalizeBool(b):
    if isinstance(b, bool):
        return b
    else:
        raise TypeError()


def normalizeInt(b):
    if isinstance(b, int):
        return b
    else:
        raise TypeError()


def normalizeStringReset(s):
    if isinstance(s, basestring):
        return s
    elif s is Reset:
        return s
    else:
        raise TypeError()


def normalizeBoolReset(b):
    if isinstance(b, bool):
        return b
    elif b is Reset:
        return b
    else:
        raise TypeError()


def normalizeTwoStringsString(s):
    if isinstance(s, basestring):
        return s.split("/")
    elif isinstance(s, tuple):
        return s
    else:
        raise TypeError()


def normalizeEnum(s, *values):
    if s in values:
        return s
    else:
        raise TypeError()


def normalizeList(normalizeElement, l):
    if normalizeElement is normalizeRepositoryFullName:
        return ["/".join(normalizeElement(e)) for e in l]
    else:
        return [normalizeElement(e) for e in l]


def normalizeGitIgnoreTemplateName(tmpl):
    import PyGithub.Blocking.Github  # @todoAlpha Find a way to remove those local imports
    if isinstance(tmpl, PyGithub.Blocking.Github.Github.GitIgnoreTemplate):
        return tmpl.name
    elif isinstance(tmpl, basestring):
        return tmpl
    else:
        raise TypeError()


def normalizeGitAuthor(a):
    # @todoAlpha Devise a strategy for structured input data
    if isinstance(a, dict):
        return a
    else:
        raise TypeError()


def normalizeDatetime(d):
    # @todoAlpha Should we parse strings into datetime here?
    if isinstance(d, datetime.datetime):
        return d.isoformat() + "Z"  # @todoAlpha Use utcoffset? https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat
    else:
        raise TypeError()


def normalizeDict(d):
    return d


def normalizeGitTreeSha(tree):
    import PyGithub.Blocking.GitTree
    if isinstance(tree, PyGithub.Blocking.GitTree.GitTree):
        return tree.sha
    elif isinstance(tree, str):
        return tree
    else:
        raise TypeError()


def normalizeGitCommitSha(commit):  # @todoAlpha Rename normalizeGitCommitSha
    import PyGithub.Blocking.GitCommit
    if isinstance(commit, PyGithub.Blocking.GitCommit.GitCommit):
        return commit.sha
    elif isinstance(commit, str):
        return commit
    else:
        raise TypeError()

#!/usr/local/bin/python3

import click, os
from git import Repo, exc


@click.group()
def cli():
    """This application is for keeping my workspace up-to-date"""


@cli.command('update', short_help='Update repositories')
@click.option('--folder',       '-f', default=os.getcwd(), help='Update repositories under this folder (absolute paths only)')
@click.option('--svn',          '-s', default=None, help='Only update svn repositories')
@click.option('--git',          '-g', default=None, help='Only update git repositories')
def update(folder, svn, git):
    for repo in __git_folders_as_repos(__get_git_folders(folder)):
        __update(repo, __is_svn_or_git(repo))


@cli.command('status', short_help='Check status of repositories')
@click.option('--folder',       '-f', default=os.getcwd(), help='Check status of repositories under this folder')
@click.option('--svn',          '-s', default=None, help='Only check svn repositories')
@click.option('--git',          '-g', default=None, help='Only check git repositories')
def status(folder, svn, git):
    for repo in __git_folders_as_repos(__get_git_folders(folder)):
        __status(repo)


@cli.command('clone', short_help='Clone repositories')
@click.argument('team', metavar='<team>')
def clone(team):
    print("team: {team}".format(team=team))


def __get_git_folders(folder):
    git_folders = []
    for root, dirs, files in os.walk(folder):
        if dirs and '.git' in dirs:
            git_folders.append(root)
    return git_folders


def __git_folders_as_repos(git_folder_paths):
    repos = []
    for git_repo in git_folder_paths:
        repos.append(Repo(git_repo))
    return repos


def __is_svn_or_git(git_repo):
    url = ''
    for i in git_repo.git.config('--list').splitlines():
        if 'url' in i:
            url = i
    return 'git' if 'git' in url else 'svn'


def __update(git_repo, git_or_svn):
    try:
        result = git_repo.git.pull() if git_or_svn == 'git' else git_repo.git.svn('rebase')
    except exc.GitCommandError as error:
        result = "Error: %s" % error
    print("Result on updating %s: %s" % (git_repo.working_dir, result))


def __status(git_repo):
    try:
        result = git_repo.git.status()
    except exc.GitCommandError as error:
        result = "Error: %s" % error
    print("Result on status %s: %s" % (git_repo.working_dir, result))


if __name__ == '__main__':
    cli()

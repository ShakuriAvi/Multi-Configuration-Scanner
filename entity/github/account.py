from github import Auth, Github
from entity.github.repository import Repository
from typing import List


class Account:
    def __init__(self, **kwargs):
        # Initialize Account object with account name and access token
        self.account_name = kwargs.get('account_name')
        self.access_token = kwargs.get('access_token')

        # Initialize GitHub user object using access token
        self.user = self.__init_github()

        # Initialize list of repositories
        self.repositories = self.__init_repo(kwargs.get('repositories'))

    def __init_github(self):
        # Initialize authentication with access token
        auth = Auth.Token(self.access_token)
        # Create GitHub user object
        user = Github(auth=auth)
        return user

    def __init_repo(self, repositories_prop: List):
        repositories = []
        # Iterate through repository names
        for repo_name in repositories_prop:
            # Append repository name to the list
            repositories.append(repo_name)
        return repositories

from entity.github.github_file import GitHubFile
from entity.file import FileFactory
class Repository:

    def __init__(self, user, repo_name):
        self.user = user
        self.repo_name = repo_name
    

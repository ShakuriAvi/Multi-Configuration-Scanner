from cfg import ACCOUNTS_SETTINGS
from entity.github.account import Account
from entity.github.github_file import GitHubFile
from entity.file import FileFactory
class GithubAccessor:
    def __init__(self):
        self.accounts_config = ACCOUNTS_SETTINGS

    

    def stream_files(self):
        accounts_list = []

        for config in self.accounts_config:
            accounts_list.append(Account(**config))

        for account in accounts_list:
            for repo_name in account.repositories:
                repo = account.user.get_repo(f"{account.account_name}/{repo_name}")
                contents = repo.get_contents("")
                while contents:
                    file_content = contents.pop(0)
                    if file_content.type == "dir":
                        contents.extend(repo.get_contents(file_content.path))
                    else:
                        github_file = GitHubFile(repo, file_content)
                        new_file = FileFactory()
                        yield new_file.create(github_file)

        return True

import random
from typing import Any


class GitHubFile:
    def __init__(self, repository: Any, file):
        # Initialize GitHubFile object with repository, and file
        self.repository = repository
        self.file = file
        self.content = file.decoded_content.decode("utf-8")  # Decode file content
        self.file_name = file.name  # Get file name

    def get_content(self):
        # Method to get file content
        return self.content.decoded_content.decode("utf-8")

    def commit_content(self, notes: str, update_content=None):
        # Method to commit file content changes
        branch_name = self.__create_new_branch()  # Create a new branch
        if not update_content:
            # If no update content provided, create an empty commit
            branch = self.repository.get_branch(branch_name)
            commit = self.repository.create_empty_commit(
                message="Empty commit",
                parents=[branch.commit],
                committer={
                    "name": "Your Name",
                    "email": "your.email@example.com"
                }
            )
            branch.edit(commit.sha)
        else:
            # Update file content and commit changes
            self.repository.update_file(self.file.path, "more tests", update_content, self.file.sha, branch=branch_name)
        self.__pull_request(branch_name, notes)  # Create a pull request

    def __create_new_branch(self):
        # Method to create a new branch
        number = random.randint(1000, 9999)
        new_branch_name = f'{number}'
        base_branch = self.repository.default_branch
        sb = self.repository.get_branch(base_branch)
        self.repository.create_git_ref(ref='refs/heads/' + new_branch_name, sha=sb.commit.sha)
        return new_branch_name

    def __pull_request(self, branch_name, notes):
        # Method to create a pull request
        self.repository.create_pull(base="main", head=branch_name, title=f"{branch_name}", body=notes)

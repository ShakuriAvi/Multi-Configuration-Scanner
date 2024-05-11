import yaml
import json
from entity.github.github_file import GitHubFile

# Interface for file parsers
class IFile:
    # Method to get the content of the file
    def get_content(self):
        raise NotImplementedError()

    # Method to get the file type
    def get_file_type(self):
        raise NotImplementedError()

# Parser class for JSON files
class JsonParser(IFile):
    def __init__(self, file: GitHubFile):
        self.file = file
        self.file_type = 'json'

    # Method to parse and return the content of the JSON file
    def get_content(self):
        return json.loads(self.file.content)

    # Method to return the file type
    def get_file_type(self):
        return self.file_type

# Parser class for YAML files
class YamlParser(IFile):
    def __init__(self, file: GitHubFile):
        self.file = file
        self.file_type = 'yaml'

    # Method to parse and return the content of the YAML file
    def get_content(self):
        return yaml.safe_load(self.file.content)

    # Method to return the file type
    def get_file_type(self):
        return self.file_type

# Parser class for plain text files
class TextParser(IFile):
    def __init__(self, file: GitHubFile):
        self.file = file
        self.file_type = 'txt'

    # Method to return the content of the text file
    def get_content(self):
        return self.file.content

    # Method to return the file type
    def get_file_type(self):
        return self.file_type


# Factory class for creating parser objects
class FileFactory:
    def create(self, file: GitHubFile):
        # Determine the file type based on the file name extension
        file_type = file.file_name.split(".")[1]

        # Create and return an instance of the appropriate parser class
        if file_type == 'json':
            return JsonParser(file)
        elif file_type == 'yaml':
            return YamlParser(file)
        elif file_type == 'txt':
            return TextParser(file)
        else:
            # Return an instance of the interface if the file type is not recognized
            return IFile()

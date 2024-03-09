from entity.scanner.handler import Handler
from typing import Any
import subprocess

class RequirementsVulnerabilities(Handler):
    def __init__(self):
        # Define the supported file type
        self.files_type = ("txt")

    def scan_and_fix(self, config_file: Any):
        try:
            # Check if the file type is supported and if the file name contains "requirement"
            if config_file.file_type in self.files_type and "requirement" in config_file.file.file_name:
                file_name = config_file.file.file_name
                print(f"file: {file_name} {self.__class__.__name__}")

                # Run safety check on the content of the requirements file
                result = subprocess.run(["safety", "check", "-r", "-"], input=config_file.file.content, capture_output=True, text=True)

                # Split the output to extract vulnerabilities
                vulnerabilities = result.stdout.split("REPORT")[1]

                # If vulnerabilities are found, suggest updates and commit the changes
                if vulnerabilities:
                    # Add a newline character to the file content
                    config_file.file.content += "\n"
                    print(f"new suggestion for Requirements file:{vulnerabilities}")
                    config_file.file.commit_content(f"new suggestion for Requirements file:{vulnerabilities}", config_file.file.content)

        # Handle missing configuration data exception
        except KeyError as e:
            print(f"missing configuration data: {e}")

        # Handle missing Attribute data exception
        except AttributeError as e:
            print(f"missing Attribute data: {e}")

        # Handle other unexpected exceptions
        except Exception as e:
            print(f"unexpected error: {e}")

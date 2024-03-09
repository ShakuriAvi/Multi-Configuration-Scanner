from entity.scanner.handler import Handler
import re
from typing import Any

class ConfigurationAWSCredScanner(Handler):
    def __init__(self):
        # Define the supported file types
        self.files_type = ("txt", "json", "yaml")

    def scan_and_fix(self, config_file:Any):
        try:
            # Extract file name and check if file type is supported
            file_name = config_file.file.file_name
            if config_file.file_type in self.files_type:
                print(f"file: {file_name} {self.__class__.__name__}")

                # Define regex patterns for AWS access keys and secret keys
                aws_access_key_regex = re.compile(r'(?<![A-Z0-9])[A-Z0-9]{20}(?![A-Z0-9])')
                aws_secret_key_regex = re.compile(r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])')

                # Find access keys and secret keys in the file content
                access_keys = aws_access_key_regex.findall(config_file.file.content)
                secret_keys = aws_secret_key_regex.findall(config_file.file.content)

                # If no keys are found, configuration is correct
                if not access_keys and not secret_keys:
                    print("Configuration is correct.")
                    return

                # If secret keys are found, redact them from the content and commit changes
                if secret_keys:
                    updated_content = config_file.file.content
                    for secret_key in secret_keys:
                        updated_content = updated_content.replace(secret_key, "REDACTED")
                    print(f"The secret_keys: {secret_keys} shows")
                    config_file.file.commit_content(f"This is sensitive data, Please remove {secret_keys} and "
                                                    f"put this file .gitignore",
                                                    updated_content)

                # If access keys are found, redact them from the content and commit changes
                if access_keys:
                    print(f"The access_keys: {access_keys} shows")
                    updated_content = config_file.file.content
                    for access_key in access_keys:
                        updated_content = updated_content.replace(access_key, "REDACTED")
                    config_file.file.commit_content(f"This is sensitive data, Please remove {secret_keys} and "
                                                    f"put this file .gitignore", updated_content)

        # Handle missing configuration data exception
        except KeyError as e:
            print(f"missing configuration data: {e}")

        # Handle missing Attribute data exception
        except AttributeError as e:
            print(f"missing Attribute data: {e}")

        # Handle other unexpected exceptions
        except Exception as e:
            print(f"unexpected error: {e}")

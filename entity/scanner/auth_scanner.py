import json
from entity.scanner.handler import Handler
from typing import Any


class AuthControlScanner(Handler):
    def __init__(self):
        # Initialize the files_type attribute with file types to be scanned
        self.files_type = ("json")

    def scan_and_fix(self, config_file: Any):
        try:
            # Get the file name from the config_file
            file_name = config_file.file.file_name

            # Check if the file type is in the files_type attribute
            if config_file.file_type in self.files_type:
                # Get the content of the config_file
                data = config_file.get_content()
                authorized_users = set(data["authorized_users"])  # Extract authorized users
                denied_user = data["denied_user"]  # Extract denied user

                # Print file information and class name
                print(f"file: {file_name} {self.__class__.__name__}")

                # Initialize a list to store removed users
                removed_users = []

                # Loop through denied users
                for user in denied_user:
                    if user in authorized_users:
                        # If denied user is also authorized, remove from authorized users and add to removed_users list
                        authorized_users.remove(user)
                        removed_users.append(user)

                if len(removed_users) > 0:
                    # If any users were removed, update the content and commit changes
                    updated_content = {
                        "authorized_users": list(authorized_users),
                        "denied_user": denied_user
                    }
                    config_file.file.commit_content(
                        f"There are unauthorized users in the system: {','.join(removed_users)}. "
                        f"Recommended to remove them",
                        json.dumps(updated_content)
                    )
                else:
                    # If no users were removed, print that configuration is correct
                    print("Configuration is correct.")

        # Handle missing configuration data exception
        except KeyError as e:
            print(f"missing configuration data: {e}")

        # Handle missing Attribute data exception
        except AttributeError as e:
            print(f"missing Attribute data: {e}")

        # Handle other unexpected exceptions
        except Exception as e:
            print(f"unexpected error: {e}")

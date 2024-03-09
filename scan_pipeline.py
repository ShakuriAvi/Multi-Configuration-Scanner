from abc import abstractmethod
from entity.file import IFile  # Import the IFile interface
from entity.scanner.configuration_aws_cred import ConfigurationAWSCredScanner  # Import the ConfigurationAWSCredScanner class
from entity.scanner.auth_scanner import AuthControlScanner  # Import the AuthControlScanner class
from entity.scanner.requirements_vulnerabilities import RequirementsVulnerabilities  # Import the RequirementsVulnerabilities class

class Scanner:
    def __init__(self):
        pass

    @abstractmethod
    def scan(self, file: IFile):
        raise NotImplementedError()

# Concrete class implementing the scanning logic
class ScanPipeline(Scanner):

    def __init__(self):
        super().__init__()
        # Initialize a list of scanners
        self.scanners = [ConfigurationAWSCredScanner(), AuthControlScanner(), RequirementsVulnerabilities()]

    # Method to scan the file using multiple scanners
    def scan(self, file: IFile):
        # Iterate over each scanner in the list
        for scanner in self.scanners:
            # Call the scan_and_fix method of each scanner with the file as input
            scanner.scan_and_fix(file)

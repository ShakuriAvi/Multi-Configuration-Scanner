from github_accessor import GithubAccessor  # Import the GithubAccessor class
from scan_pipeline import ScanPipeline  # Import the ScanPipeline class
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor
from entity.file import IFile  # Import the IFile interface

class ScanManager:
    def __init__(self):
        self.github_accessor = GithubAccessor()  # Initialize GithubAccessor

    # Method to process a single file
    def process_file(self, file_path: IFile):
        pipeline = ScanPipeline()  # Create a ScanPipeline object
        pipeline.scan(file_path)  # Execute the scan pipeline for the file

    # Method to start the scanning process
    def run(self):
        # Use ThreadPoolExecutor to concurrently execute process_file for multiple files
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Use map to apply process_file to each file obtained from GithubAccessor
            executor.map(self.process_file, self.github_accessor.stream_files())

from abc import ABC, abstractmethod
from typing import Any

class Handler(ABC):
    @abstractmethod
    def scan_and_fix(self, config_file: Any):
        pass

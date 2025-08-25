from core.cliforge import CliForge
from abc import ABC, abstractmethod

class Command(ABC):
    @staticmethod
    def execarg(parsed_args: dict[str, str]) -> None:
        pass

    

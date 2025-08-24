import os
import sys
from utils.arg_parser import ArgParser

class CliForge:
    def __init__(self, config: dict[str, str], cmds) -> None:
        self.__cmds = cmds
        self.config = config

    def exec_cmd(prompt: str = "") -> None:
        args = ArgParser.split(prompt)

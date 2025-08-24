import os
from utils.command_parser import CommandParser as CmdParse

class CliForge:
    def __init__(self, config, cmds):
        self.__cmds = cmds
        self.config = config

    def exec_cmd(prompt = ""):
        args = CmdParse.split(prompt)
        #EXECUTE CMD

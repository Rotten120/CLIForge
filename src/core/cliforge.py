from utils.arg_parser import ArgParser

class CliForge:
    def __init__(self, config: dict[str, str], cmds) -> None:
        self.__cmds = cmds
        self.config = config

    def exec_cmd(self, argv: str | list[str]) -> None:
        argtype = type(argv)

        if argtype == type(""):
            argv = ArgParser.split(argv)

        print(argv)

from utils.arg_parser import ArgParser

class CliForge:
    def __init__(self, config: dict[str, str], cmds) -> None:
        self.__cmds = cmds
        self.config = config

    def exec_cmd(self, argv: str | list[str]) -> None:
        if type(argv) == str:
            argv = CliForge.format_strcmd(argv)

        cmd = argv[0]
        parsed_args = ArgParser.parse(argv[1:])
        
        self.__cmds[cmd](parsed_args)

    @staticmethod
    def format_strcmd(argv: str) -> list[str]:
        argv = ArgParser.split(argv)
        if argv[0] != "cli":
            raise Exception("cli input must start with 'cli'")
        return argv[1:]

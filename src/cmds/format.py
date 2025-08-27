from core.cliforge import CliForge

class Format:
    def __init__(self, parsed_args: dict[str, list[str]]):
        self.flags = {
            "UPPER": False,
            "LOWER": False,
            "ITALIC": False,
            "STRONG": False,
            "SOURCE": False
        }
        
        self.flagargs = {}
        self.execarg(parsed_args)
        
    def execarg(self, parsed_args: dict[str, list[str]]) -> None:
        optli = {
            "--upper": "UPPER",
            "--lower": "LOWER",
            "-i": "ITALIC",
            "-b": "STRONG",
            "--source": "SOURCE"
        }
        
        for opt in parsed_args:
            if opt in optli:
                flag = optli[opt]
                value = parsed_args[opt]
                self.set_flag(flag, value)
            elif opt != "cmd_arg":
                raise Exception("option not exist")

        self.run(parsed_args["cmd_arg"])        

    def set_flag(self, key: str, arg: list[str] = []) -> None:
        self.flags[key] = True
        if arg != []:
            self.flagargs[key] = arg

    def run(self, cmd_args: list[str]) -> None:
        string = cmd_args[0]
        flags = self.flags

        if flags["UPPER"]:
            string.upper()
        if flags["LOWER"]:
            string.lower()
        if flags["ITALIC"]:
            string = "<i>" + string
        if flags["STRONG"]:
            string = "<b>" + string
        if flags["SOURCE"]:
            string = self.flagargs["SOURCE"][0] + ": " + string

        print(string)
            
            

        

from cmds.flag import FlagToggle, FlagValue
from cmds.cmd import Command

class Format(Command):
    cli_name = "format"
    cmd_flag_default = FlagValue(["default"], 1)
    
    flag_default: dict[str, FlagToggle | FlagValue] = {
        "ITALIC": FlagToggle(False),
        "STRONG": FlagToggle(False),
        "UPPER": FlagToggle(False),
        "LOWER": FlagToggle(False),
        "SOURCE": FlagValue(["None"], -1)
    }

    flag_queue: dict[str, str] = {
        "--upper": "UPPER",
        "--lower": "LOWER",
        "-i": "ITALIC",
        "-b": "STRONG",
        "--source": "SOURCE"
    }

    def execute_command(self) -> None:        
        string = self.cmd_flag.value[0]

        if self.flags["UPPER"]:
            string = string.upper()
        if self.flags["LOWER"]:
            string = string.lower()
        if self.flags["ITALIC"]:
            string = "<i>" + string + "<i>"
        if self.flags["STRONG"]:
            string = "<b>" + string + "<b>"

        source_val = self.flags["SOURCE"].value
        if source_val != None:
            string = str(source_val) + ": " + string

        print(string)

    

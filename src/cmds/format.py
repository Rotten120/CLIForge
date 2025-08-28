from cmds.cmd import Command, FlagBool, FlagList

class Format(Command):
    flagbools: dict[str, FlagBool] = {
        "ITALIC": FlagBool(False),
        "STRONG": FlagBool(False),
        "UPPER": FlagBool(False),
        "LOWER": FlagBool(False)
    }

    flaglists: dict[str, FlagList] = {
        "SOURCE": FlagList(["None"], 1)
    }

    optli: dict[str, str] = {
        "--upper": "UPPER",
        "--lower": "LOWER",
        "-i": "ITALIC",
        "-b": "STRONG",
        "--source": "SOURCE"
    }

    def run(self, cmd_args: list[str]) -> None:
        string = cmd_args[0]

        for n in self.flagbools:
            self.flagbools[n].print()

        if self.flagbools["UPPER"]:
            string = string.upper()
        if self.flagbools["LOWER"]:
            string = string.lower()
        if self.flagbools["ITALIC"]:
            string = "<i>" + string
        if self.flagbools["STRONG"]:
            string = "<b>" + string

        source_val = self.flaglists["SOURCE"].value[0]
        if source_val != None:
            string = source_val + ": " + string

        print(string)

    

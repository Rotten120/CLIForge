from abc import ABC, abstractmethod
from cmds.flag import FlagBool, FlagList

class Command(ABC):
    flagbools: dict[str, FlagBool] = {
        """
        FLAG1: FlagBool(True/False),
        FLAG2: FlagBool(True/False)
        """
    }
    
    flaglists: dict[str, FlagList] = {
        """
        FLAG3: FlagList([arg1, arg2], 2)
        """
    }
    
    optli: dict[str, str] = {
        """
        INPUT1: FLAG_NAME1,
        INPUT2: FLAG_NAME1,
        INPUT3: FLAG_NAME2,
        INPUT4: FLAG_NAME3
        """
        }

    """
    NEGATIVE ARGCOUNT MEANS THERE SHOULD BE AT LEAST
    ABS(X) ARGUMENTS PASSED (i.e. -2 means at least 2 args)
    """

    def __init__(self, parsed_args: dict[str, list[str]]):
        self.execarg(parsed_args)

    def execarg(self, parsed_args: dict[str, list[str]]) -> None:
        for opt in parsed_args:
            if opt in self.optli:
                flag = self.optli[opt]
                value = parsed_args[opt]
                self.set_flag(flag, value)
            elif opt != "cmd_arg":
                raise Exception("option not exist")

        self.run(parsed_args["cmd_arg"])

    def set_flag(self, flag: str, value: list[str]) -> None:
        if flag in self.flagbools:
            self.flagbools[flag].update_flag(flag, value)
        elif flag in self.flaglists:
            self.flaglists[flag].update_flag(flag, value)

    @abstractmethod
    def run(self, cmd_args: list[str]) -> None:
        pass

class Flag:
    def __init__(self, default, argcnt: int):
        self.value = default
        self.argcnt = argcnt

    def __check_argcnt(self, flag_name: str, val_arglen: int) -> None:
        argcount = self.argcnt
        if argcount >= 0:
            if val_arglen != argcount:
                raise TypeError(f"{flag_name} takes {argcount} positional arguments but {val_arglen} was given")
        else:
            argcount *= 1
            if val_arglen < argcount:
                raise TypeError(f"{flag_name} takes at least {argcount} positional arguments but {val_arglen} was givne")

    def update_flag(self, flag_name: str, value: list[str] == []) -> None:
        self.__check_argcnt(flag_name, len(value))
        self.value = value

# FlagBool ignores __check_argcnt since it only needs 0/1 args
class FlagBool(Flag):
    def __init__(self, default: bool):
        super().__init__(default, 1)

    def __bool__(self):
        return self.value

    def update_flag(self, flag_name: str, value: list[str] == []) -> None:
        val_arglen = len(value)
        if val_arglen == 0:
            self.value = not self.value
        elif val_arglen == 1:
            self.value = self.__str_to_bool(value[0])
        else:
            raise TypeError(f"{flag_name} takes 0 or 1 positional arguments but {val_arglen} was given")

    def print(self):
        print(self.value, self.argcnt)

    @staticmethod
    def __str_to_bool(value: str) -> bool:
        if value == "True" or value == "true":
            return True
        elif value == "False" or value == "false":
            return False
        else:
            raise Exception(f"flag takes 'True' or 'False' argument but {value} was given")

class FlagList(Flag):
    def __init__(self, default: list[str], argcnt: int):
        super().__init__(default, argcnt)

        

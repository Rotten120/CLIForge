class Flag:
    def __init__(self, default, argcnt: int):
        self.value = default
        self.argcnt = argcnt

    def __check_argcnt(self, flag_name: str, val_arglen: int) -> None:
        argcount = self.argcnt
        if argcount >= 0 and val_arglen != argcount:
            raise TypeError(f"{flag_name} takes {argcount} positional arguments but {val_arglen} was given")
        if argcount < 0 and val_arglen <= 0:
            raise TypeError(f"{flag_name} takes at least 1 positional arguments but 0 was given")
        
    def update_flag(self, flag_name: str, value: list[str] == []) -> None:
        self.__check_argcnt(flag_name, len(value))
        self.value = value

    def print(self):
        print(f"value={self.value} | argcnt={self.argcnt}")

class FlagToggle(Flag):
    def __init__(self, default: bool):
        super().__init__(default, 0)
        self.toggled_val = not default

    def __bool__(self):
        return self.value

    def update_flag(self, flag_name: str, value: list[str] == []) -> None:
        val_arglen = len(value)
        if val_arglen != 0:
            err_msg = f"{flag_name} takes 0 positional arguments but {val_arglen} was given"
            raise TypeError(err_msg)
        self.value = self.toggled_val

    def print(self):
        print(f"value={self.value} | toggled value={self.toggled_val} | argcnt={self.argcnt}")

class FlagValue(Flag):
    def __init__(self, default: list[str], argcnt: int):
        super().__init__(default, argcnt)

        

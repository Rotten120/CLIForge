from abc import ABC, abstractmethod
from cmds.flag import FlagToggle, FlagValue

class Command(ABC):
    cli_name: str = "cmd"
    cmd_flag_default: FlagValue | FlagToggle = FlagValue([None], 1)
    flag_default: dict[str, FlagToggle | FlagValue] = {
        #FLAGNAME -> FLAGVAL
    }

    flag_queue: dict[str, str] = {
        # OPTION -> FLAGNAME
    }
    
    def __init__(self, args: dict[str, list[str]]):
        self.args = args
        self.cmd_flag = self.cmd_flag_default
        self.flags = self.flag_default
        self.execarg()

    def execarg(self) -> None:
        executed_queues = []
        last_opt = list(self.args.keys())[-1]

        for opt in self.args:
            if opt == "--":
                continue
            if not(opt in self.flag_queue):
                raise Exception(f"Option {opt} does not exist. Try {self.cli_name} help")
            
            flag = self.flag_queue[opt]
            if opt == last_opt:
                self.extract_cmdargs(opt, flag)

            arg = self.args[opt]
            self.flags[flag].update_flag(flag, arg)

        self.cmd_flag.update_flag(self.cli_name, self.args['--'])
        self.execute_command()

    def extract_cmdargs(self, opt: str, flag: str) -> None:
        cmd_args = self.args['--']
        flag_args = self.args[opt]
                
        cmd_arglen = len(cmd_args)
        flag_arglen = len(flag_args)
        
        flag_argcnt = self.flags[flag].argcnt
        cmd_argcnt = self.cmd_flag.argcnt

        # transfers last `num` eles of src to dest
        def update_args(eles_to_transfer: int) -> None:
            if eles_to_transfer == 0:
                return
            nonlocal opt
            self.args['--'] = cmd_args + flag_args[-eles_to_transfer:]
            self.args[opt] = flag_args[:-eles_to_transfer]

        # MANY-EXACT
        if cmd_argcnt == -1 and flag_argcnt >= 0:
            if cmd_arglen == 0 and flag_arglen > flag_argcnt:
                update_args(flag_argcnt)

        # EXACT-MANY
        if cmd_argcnt >= 0 and flag_argcnt == -1:
            if cmd_arglen == 0 and flag_arglen > cmd_argcnt:
                update_args(cmd_argcnt)

        # EXACT-EXACT
        if cmd_argcnt >= 0 and flag_argcnt >= 0:
            if cmd_arglen == 0 and flag_arglen > flag_argcnt:
                update_args(flag_arglen - flag_argcnt)

        # MANY-MANY DOES NOT NEED ONE

    @abstractmethod
    def execute_command(self) -> None:
        pass

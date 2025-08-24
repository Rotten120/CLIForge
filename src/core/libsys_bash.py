import os
from utils.command_parser import CommandParser as CmdParse
from shared.core.lib_conn import LibConn

class LibSysBash(LibConn):
    __cmds = {}
    config = {}

    def init(config, cmds):
        dblog = config["dblog"]
        LibConn.init(
            dblog["host"],
            dblog["user"],
            dblog["pass"],
            dblog["db"]
        )

        LibSysBash.__cmds = cmds
        LibSysBash.config = config

    def run():
        prompt = ""
        while True:
            prompt = input("$ ")

            if prompt.startswith("lib "):
                args = CmdParse.split(prompt)
                LibSysBash.run_lib_cmd(args[1], CmdParse.parse(args[2:]))
            else:
                LibSysBash.run_os_cmd(prompt)

    def run_lib_cmd(cmd, params = []):
        if cmd == "disconnect":
            quit()
        try:
            LibSysBash.__cmds[cmd].execute(params)
        except KeyError:
            print(f"lib: `{cmd}` is not a lib command. See 'lib --help'")

    def run_os_cmd(prompt):
        if prompt != "exit":
            os.system(prompt)
        else:
            print("lib: database connection still online. Use 'lib disconnect' to terminate connection")

    
    


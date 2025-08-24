from cmds.cmd import *

class Config:
    def execute(argv):
        print(argv)

    def print_config():
        for namespace in LibBash.config:
            attrs = LibBash.config[namespace]
            for key in attrs:
                value = attrs[key]
                print(namespace, '.', key, '=', value, sep = '')

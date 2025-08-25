from core.cliforge import CliForge
from utils.config_codec import ConfigCodec
from cmds import *

def fetch_config(file_path: str = "CONFIG") -> dict[str, str]:
    with open(file_path, 'r') as config:
        return ConfigCodec.parse_config(config)

if __name__ == "__main__":
    cmd_class = get_cmd_class()
    config_parsed = fetch_config()

    forge = CliForge(config_parsed, cmd_class)
    forge.exec_cmd("cli format testcase --source Rotten -b -i")


    

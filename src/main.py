import utils.import_shared as imp
imp.port_shared()

from cmds import get_cmd_class
from core.libsys_bash import LibSysBash
from utils.config_translate import ConfigTranslation as ConfigCodec

def fetch_config(file_path = "CONFIG"):
    with open(file_path, 'r') as config:
        return ConfigCodec.parse_config(config)

if __name__ == "__main__":
    cmd_dict = get_cmd_class()
    config_parsed = fetch_config()
    
    LibSysBash.init(config_parsed, cmd_dict)
    LibSysBash.run()


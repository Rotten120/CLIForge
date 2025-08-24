from core.cliforge import CliForge
from utils.config_codec import ConfigCodec

def fetch_config(file_path = "CONFIG"):
    with open(file_path, 'r') as config:
        return ConfigCodec.parse_config(config)

if __name__ == "__main__":
    config_parsed = fetch_config()

    forge = CliForge(config_parsed, {})
    forge.exec_cmd("git asd --verion 'asd'   asd")



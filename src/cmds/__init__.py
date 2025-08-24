from .config import Config
from .connect import Connect

def get_cmd_class():
    return {
        "config": Config,
        "connect": Connect
    }

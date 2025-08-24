import sys
import os

def port_shared():
    paths = os.path.join(os.path.dirname(__file__), '..', '..')
    abspath = os.path.abspath(paths)
    sys.path.append(abspath)

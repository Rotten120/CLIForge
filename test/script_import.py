import sys
import os

paths = os.path.join(os.path.dirname(__file__), '..', 'src')
abspath = os.path.abspath(paths)

sys.path.append(abspath)

import unittest

import sys
import os

paths = os.path.join(os.path.dirname(__file__), '..', 'src')
abspath = os.path.abspath(paths)

sys.path.append(abspath)

import unittest

class TestCase(unittest.TestCase):
    def _exe_test(self, test_input, test_output, func):
        for inp, out in zip(test_input, test_output):
            with self.subTest(text=inp):
                self.assertEqual(func(inp), out)

    def _exe_errs(self, test_input, err_output, func):
        for inp, err in zip(test_input, err_output):
            with self.subTest(text=inp):
                with self.assertRaises(err):
                    func(inp)

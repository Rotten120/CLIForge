from script_import import *
from utils.arg_parser import ArgParser

class TestSpaces(unittest.TestCase):
    def test_spaces(self):
        test_cases = {
            "    Leading Spaces": ['Leading', 'Spaces'],
            "Trailing Spaces   ": ['Trailing', 'Spaces'],
            "Multi  Spaces  Between": ['Multi', 'Spaces', 'Between']
        }

        for inp in test_cases:
            exp = test_cases[inp]
            with self.subTest(text=inp):
                self.assertEqual(ArgParser.tokenize(inp), exp)

class TestEquals(unittest.TestCase):
    def test_equals(self):
        test_cases = {
            "one_arg=argument1": ['one_arg', '=', 'argument1'],
            "multi_equal=param1=param2=param3": ['multi_equal', '=', 'param1=param2=param3'],
            "ending in=": ['ending', 'in', '='],
            "empty =signs=param1": ['empty', '=signs', '=', 'param1'],
            "spaces after= equal": ['spaces', 'after', '=', 'equal']
        }
    
        for inp in test_cases:
            exp = test_cases[inp]
            with self.subTest(text=inp):
                self.assertEqual(ArgParser.tokenize(inp), exp)
        
class TestQuotes(unittest.TestCase):
    def test_quotes(self):
        test_cases = {
            "combi'ned argument'": ['combined argument'],
            "single 'quote  inputs'": ['single', 'quote  inputs'],
            'double "quote  inputs"': ['double', 'quote  inputs']
        }

        for inp in test_cases:
            exp = test_cases[inp]
            with self.subTest(text=inp):
                self.assertEqual(ArgParser.tokenize(inp), exp)
                
    def test_errs(self):
        error_cases = {
            "unclosed 'quote": ValueError
        }

        for inp in error_cases:
            exp_err = error_cases[inp]
            with self.assertRaises(exp_err):
                ArgParser.tokenize(inp)

if __name__ == "__main__":
    unittest.main()

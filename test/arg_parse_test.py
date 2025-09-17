from script_import import *
from utils.arg_parser import ArgParser

class TestInputs(unittest.TestCase):
    def test_spacing(self):
        test_cases = {
            "   Leading Spaces": ['Leading', 'Spaces'],
            "Trailing Spaces  ": ['Trailing', 'Spaces'],
            "Multi  Spaces  in  Between": ['Multi', 'Spaces', 'in', 'Between']
        }

        for inp in test_cases:
            out = test_cases[inp]
            self.assertEqual(ArgParser.tokenize(inp), out)

    def test_on_equal(self):
        test_cases = {
            "one_arg=argument1" : ['one_arg', '=', 'argument1'],
            "multi_equal=param1=param2" : ['multi_equal', '=', 'param1=param2'],
            "ending in=" : ['ending', 'in', '='],
            "empty =signs=param1": ['empty', '=signs', '=', 'param1']
        }

        for inp in test_cases:
            out = test_cases[inp]
            self.assertEqual(ArgParser.tokenize(inp), out)

    def test_quotes(self):
        test_cases = {
            "combi'ned  argument'": ['combined  argument'],
            "single 'quote  inputs'": ['single', 'quote  inputs'],
            'double "quote  inputs"': ['double', 'quote  inputs']
        }

        for inp in test_cases:
            out = test_cases[inp]
            self.assertEqual(ArgParser.tokenize(inp), out)

if __name__ == "__main__":
    unittest.main()

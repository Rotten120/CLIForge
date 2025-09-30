from script_import import *
from utils.arg_parser import ArgParser

class TestSpaces(TestCase):
    def test_spaces(self):
        test_in = [
            "    Leading Spaces",
            "Trailing Spaces   ",
            "Multi  Spaces  Between",
        ]

        test_out = [
            ['Leading', 'Spaces'],
            ['Trailing', 'Spaces'],
            ['Multi', 'Spaces', 'Between'],
        ]

        self._exe_test(test_in, test_out, ArgParser.tokenize)

class TestEquals(TestCase):
    def test_equals(self):
        test_in = [
            "one_arg=argument1",
            "multi_equal=param1=param2=param3",
            "ending in=",
            "empty =signs=param1",
            "spaces after= equal",
        ]

        test_out = [
            ['one_arg', '=', 'argument1'],
            ['multi_equal', '=', 'param1=param2=param3'],
            ['ending', 'in', '='],
            ['empty', '=signs', '=', 'param1'],
            ['spaces', 'after', '=', 'equal'],
        ]

        self._exe_test(test_in, test_out, ArgParser.tokenize)
        
class TestQuotes(TestCase):
    def test_quotes(self):
        test_in = [
            "combi'ned argument'",
            "single 'quote  inputs'",
            'double "quote  inputs"',
        ]

        test_out = [
            ['combined argument'],
            ['single', 'quote  inputs'],
            ['double', 'quote  inputs'],
        ]

        self._exe_test(test_in, test_out, ArgParser.tokenize)
                
    def test_errs(self):
        err_in = [
            "unclosed 'quote"
        ]

        err_out = [
            ValueError
        ]

        self._exe_errs(err_in, err_out, ArgParser.tokenize)

if __name__ == "__main__":
    unittest.main()

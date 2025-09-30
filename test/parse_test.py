from script_import import *
from utils.arg_parser import ArgParser

class TestEquals(TestCase):
    def test_equals(self):
        test_in = [
            ['arg1', 'arg2'],
            ['-a', '=', 'arg1', '-b', 'arg2']
        ]

        test_out = [
            {'--': ['arg1', 'arg2']},
            {'--': [], '-a': ['arg1'], '-b': ['arg2']}
        ]
        
        self._exe_test(test_in, test_out, ArgParser.parse)
                
    def test_errs(self):
        err_in = [
            ['-a', '=', '='],
            ['-a', '=', 'arg1', '=', 'arg2'],
            ['-a', '='],
            ['-a', '=', '-b'],
            ['-a', '=', 'arg1', 'arg2']
        ]

        err_out = [
            TypeError, TypeError,
            ValueError, ValueError, ValueError
        ]

        self._exe_errs(err_in, err_out, ArgParser.parse)

class TestTwoHyphen(TestCase):
    def test_two_hyphen(self):
        test_in = [
            ['--', '-a', 'arg1', 'arg2'],
            ['-a', 'arg1', '--', '-b', '-c'],
            ['-a', '--', 'arg1', '--', 'arg2']
        ]

        test_out = [
            {'--': ['-a', 'arg1', 'arg2']},
            {'--': ['-b', '-c'], '-a': ['arg1']},
            {'--': ['arg1', '--', 'arg2'], '-a': []}
        ]

        self._exe_test(test_in, test_out, ArgParser.parse)

if __name__ == "__main__":
    unittest.main()

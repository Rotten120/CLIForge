from script_import import *
from utils.arg_parser import ArgParser

class Test(unittest.TestCase):
    def test_case(self):
        test_cases = [
            ['arg1', 'arg2'],
            ['-a', '=', 'arg1', '-b', 'arg2']
        ]

        test_outputs = [
            {'--': ['arg1', 'arg2']},
            {'--': [], '-a': ['arg1'], '-b': ['arg2']}
        ]
        
        for inp, exp in zip(test_cases, test_outputs):
            with self.subTest(text=inp):
                self.assertEqual(ArgParser.parse(inp), exp)

    def test_errs(self):
        error_cases = [
            ['-a', '=', '='],
            ['-a', '=', 'arg1', '=', 'arg2'],
            ['-a', '='],
            ['-a', '=', '-b'],
            ['-a', '=', 'arg1', 'arg2']
        ]

        error_outputs = [
            TypeError,
            TypeError,
            ValueError,
            ValueError,
            ValueError
        ]

        for inp, exp_err in zip(error_cases, error_outputs):
            with self.subTest(text=inp):
                with self.assertRaises(exp_err):
                    ArgParser.parse(inp)

if __name__ == "__main__":
    unittest.main()

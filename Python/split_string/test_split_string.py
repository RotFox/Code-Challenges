from split_string import solution
import unittest

class TestSplitString(unittest.TestCase):
    def test(self):

        tests = (
            ("asdfadsf", ['as', 'df', 'ad', 'sf']),
            ("asdfads", ['as', 'df', 'ad', 's_']),
            ("", []),
            ("x", ["x_"]),
        )

        for inp, exp in tests:
            self.assertEqual(solution(inp), exp)

if __name__ == '__main__':
    unittest.main()

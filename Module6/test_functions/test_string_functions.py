import unittest
from more_functions import string_functions


class FunctionTestCase(unittest.TestCase):
    def test_multiple_string(self):
        result = string_functions.multiply_string("Jacob", 3)
        expected = "JacobJacobJacob"
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()

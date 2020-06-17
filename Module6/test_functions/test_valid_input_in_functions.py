import unittest
from more_functions import validate_input_in_functions


class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        result = validate_input_in_functions.score_input("Jacob's Test")
        expected = "Jacob's Test: 0"
        self.assertEquals(result, expected)

    def test_score_input_test_score_valid(self):
        result = validate_input_in_functions.score_input("Jacob's Test", 95)
        expected = "Jacob's Test: 95"
        self.assertEquals(result, expected)

    def test_score_input_test_score_below_range(self):
        result = validate_input_in_functions.score_input("Jacob's Test", -82)
        expected = "Invalid test score, try again!"
        self.assertEquals(result, expected)

    def test_score_input_test_score_above_range(self):
        result = validate_input_in_functions.score_input("Jacob's Test", 102)
        expected = "Invalid test score, try again!"
        self.assertEquals(result, expected)

    def test_score_input_test_score_non_numeric(self):
        result = validate_input_in_functions.score_input("Jacob's Test", "h")
        expected = "Invalid test score, try again!"
        self.assertEquals(result, expected)

    def test_score_input_invalid_message(self):
        result = validate_input_in_functions.score_input("Jacob's Test", -32)
        expected = "Invalid test score, try again!"
        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main()

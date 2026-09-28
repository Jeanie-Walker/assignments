import unittest
from fractions import Fraction
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()


"""Test Results:

I ran the tests according to the tutorial instructions. The output "F." means one failed and one passed.

test_list_int passed because sum([1, 2, 3]) returned 6, as expected.

test_list_fraction failed because 1/4 + 1/4 + 2/5 equals 9/10, not 1.
The test was written with the wrong expected value on purpose, so the
sum() function itself works fine. The error shows which test failed,
the line number, and the expected vs. actual values, which makes it
easy to find and fix problems."""
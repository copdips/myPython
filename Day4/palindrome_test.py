import unittest
from palindrome import *

class Tests(unittest.TestCase):
    def test_digits_1(self):
        self.assertListEqual([1,4,2], digits(241))
    def test_digits_2(self):
        self.assertListEqual([1,2,3,4,5,5], digits(554321))
    def test_is_palindrome_negative(self):
        """ should return false """
        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome(-121))
    def test_is_palindrome_positive(self):
        """ should return true """
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome(11))

unittest.main()

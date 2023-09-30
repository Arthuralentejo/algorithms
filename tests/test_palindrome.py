import unittest

from algo.palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_positives(self):
        self.assertTrue(is_palindrome('tenet'))  # add assertion here
        self.assertTrue(is_palindrome('osso'))  # add assertion here
        self.assertTrue(is_palindrome('ana'))  # add assertion here
        self.assertTrue(is_palindrome('radar'))  # add assertion here

    def test_negatives(self):
        self.assertFalse(is_palindrome('amar'))
        self.assertFalse(is_palindrome('roma'))
        self.assertFalse(is_palindrome('vida'))


if __name__ == '__main__':
    unittest.main()

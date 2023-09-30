import unittest
from algorithms.two_sums import two_sums


class TestTwoSums(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(two_sums([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sums([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sums([3, 5, 7, 11], 10), [0, 2])

    def test_negative(self):
        self.assertEqual(two_sums([2, 7, 11, 15], 10), [])
        self.assertEqual(two_sums([3, 2, 4], 8), [])
        self.assertEqual(two_sums([3, 5, 7, 11], 9), [])


if __name__ == '__main__':
    unittest.main()

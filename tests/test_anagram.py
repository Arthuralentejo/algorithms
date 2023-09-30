import unittest

from algorithms.anagram import is_anagram


class TestAnagram(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_anagram("amor", "roma"))
        self.assertTrue(is_anagram("amor", "RoMa"))

    def test_negative(self):
        self.assertFalse(is_anagram("amor", "romaa"))
        self.assertFalse(is_anagram("amor", "mor"))
        self.assertFalse(is_anagram("amor", "ma ro"))
        self.assertFalse(is_anagram("amor", "pomar"))


if __name__ == '__main__':
    unittest.main()

import unittest
from  longest_substring import lengthOfLongestSubstring

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(lengthOfLongestSubstring("abcdef"), 6)

    def test_all_same_characters(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbbb"), 1)

    def test_example_1(self):
        # LeetCode example
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

    def test_repeating_characters_in_middle(self):
        self.assertEqual(lengthOfLongestSubstring("abba"), 2)

    def test_with_spaces(self):
        self.assertEqual(lengthOfLongestSubstring("a b c a b c"), 3)

    def test_with_special_characters(self):
        self.assertEqual(lengthOfLongestSubstring("!@#$%^&*!"), 7)

    def test_long_string(self):
        s = "abcdefghijklmnopqrstuvwxyz" * 100
        self.assertEqual(lengthOfLongestSubstring(s), 26)


if __name__ == "__main__":
    unittest.main()

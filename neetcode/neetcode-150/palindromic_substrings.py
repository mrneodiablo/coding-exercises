"""
Docstring for neetcode.neetcode-150.palindromic_substrings
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.


Example 1:
    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""

import unittest


class Solution:
    def isPalindromicSubstrings(self, left, right, s, cache):
        if (left, right) in cache:
            return cache[(left, right)]

        if left > right:
            result = True
        elif left == right:
            result = True
        elif s[left] == s[right]:
            result = self.isPalindromicSubstrings(left + 1, right - 1, s, cache)
        else:
            result = False

        cache[(left, right)] = result
        return result

    def countSubstrings(self, s: str) -> int:
        ans = 0
        cache = {}  # Cache to save check palindrome
        for left in range(len(s)):
            for right in range(left, len(s)):
                if self.isPalindromicSubstrings(left, right, s, cache):
                    ans += 1
        return ans


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_simple_string(self):
        """Test with string 'abc' - each character is a palindrome"""
        s = "abc"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 3)

    def test_case_2_all_same_characters(self):
        """Test with string 'aaa' - multiple overlapping palindromes"""
        s = "aaa"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 6)

    def test_case_3_single_character(self):
        """Test with single character - edge case"""
        s = "a"
        result = self.solution.countSubstrings(s)
        self.assertEqual(result, 1)

    def test_case_4_long_repeating_characters(self):
        """Test with 100 same characters - stress test for O(n^3) algorithms"""
        s = "a" * 100
        result = self.solution.countSubstrings(s)
        # For n same characters: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2
        expected = 100 * 101 // 2
        self.assertEqual(result, expected)

    def test_case_5_alternating_pattern(self):
        """Test with alternating pattern"""
        s = "abababa"
        result = self.solution.countSubstrings(s)
        # "a", "b", "a", "b", "a", "b", "a" = 7
        # "aba", "bab", "aba", "bab", "aba" = 5
        # "ababa", "babab", "ababa" = 3
        # "abababa" = 1
        self.assertEqual(result, 16)

    def test_case_6_mixed_palindromes(self):
        """Test with mixed palindromes"""
        s = "racecar"
        result = self.solution.countSubstrings(s)
        # r, a, c, e, c, a, r = 7 single chars
        # cec = 1
        # aceca = 1
        # racecar = 1
        # Total = 10
        self.assertEqual(result, 10)

    def test_case_7_large_input_near_constraint(self):
        """Test with 500 characters - performance test"""
        s = "ab" * 250  # 500 characters
        result = self.solution.countSubstrings(s)
        # All single chars + many "aba", "bab" patterns
        # For "ababab..." pattern: many overlapping palindromes
        self.assertEqual(result, 62750)

    def test_case_8_worst_case_performance(self):
        """Test with 200 same characters - worst case for bad algorithms"""
        s = "z" * 200
        result = self.solution.countSubstrings(s)
        expected = 200 * 201 // 2
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

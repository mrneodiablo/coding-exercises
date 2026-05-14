"""
115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.


Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

import unittest


class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s) or (len(s) - i) < (len(t) - j):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # skip i:
            result = dfs(i + 1, j)

            if s[i] == t[j]:
                result += dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)


class TestNumDistinct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # "rabbbit" contains "rabbit" in 3 distinct ways
        self.assertEqual(self.solution.numDistinct("rabbbit", "rabbit"), 3)

    def test_example2(self):
        # "babgbag" contains "bag" in 5 distinct ways
        self.assertEqual(self.solution.numDistinct("babgbag", "bag"), 5)

    def test_t_longer_than_s(self):
        # t longer than s → impossible → 0
        self.assertEqual(self.solution.numDistinct("ab", "abc"), 0)

    def test_t_equals_s(self):
        # s == t → exactly 1 way
        self.assertEqual(self.solution.numDistinct("abc", "abc"), 1)

    def test_single_char_repeated(self):
        # s = "aaa", t = "a" → 3 ways to pick one 'a'
        self.assertEqual(self.solution.numDistinct("aaa", "a"), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

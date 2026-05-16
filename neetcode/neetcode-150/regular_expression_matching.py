"""
Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dfs(i, j):

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            result = False

            if j + 1 < len(p) and p[j + 1] == "*":
                # check the next index of p is "*"
                # option 1: skip "x*"
                result = dfs(i, j + 2)

                # option 2: use "x*" nếu match
                if not result and i < len(s) and (p[j] == "." or p[j] == s[i]):
                    result = dfs(i + 1, j)

            elif i < len(s) and (p[j] == "." or p[j] == s[i]):
                result = dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)


class TestIsMatch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_match_single_char(self):
        # "a" does not match entire "aa"
        self.assertFalse(self.solution.isMatch("aa", "a"))

    def test_star_repeats_char(self):
        # "a*" matches "aa" (repeat 'a' twice)
        self.assertTrue(self.solution.isMatch("aa", "a*"))

    def test_dot_star_matches_all(self):
        # ".*" matches any string
        self.assertTrue(self.solution.isMatch("ab", ".*"))

    def test_star_as_zero_occurrences(self):
        # "a*b" → 'a' appears 0 times, then 'b' matches "b"
        self.assertTrue(self.solution.isMatch("b", "a*b"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

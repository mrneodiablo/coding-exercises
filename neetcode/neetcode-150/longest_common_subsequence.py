"""
Docstring for neetcode.neetcode-150.longest_common_subsequence
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

import unittest


class Solution:

    def longestCommonSubsequenceDP(self, text1: str, text2: str) -> int:
        # number raw is the length of text1, column is the length of text2, why + 1?
        # because we need to consider the empty string case
        # for example, text1 = "a", text2 = "", the longest common subsequence is 0
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]

    def longestCommonSubsequenceBruteForce(self, text1: str, text2: str) -> int:
        # let call (i,j) is the longest common subsequence between text1[i:] and text2[j:]
        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # base case
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)

            skip_text1 = helper(i + 1, j)
            skip_text2 = helper(i, j + 1)

            result = max(skip_text1, skip_text2)

            memo[(i, j)] = result
            return result

        return helper(0, 0)


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case 1: Common subsequence 'ace'"""
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        result = self.solution.longestCommonSubsequenceDP(text1, text2)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test case 2: Identical strings"""
        text1 = "abc"
        text2 = "abc"
        expected = 3
        result = self.solution.longestCommonSubsequenceDP(text1, text2)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """Test case 3: No common subsequence"""
        text1 = "abc"
        text2 = "def"
        expected = 0
        result = self.solution.longestCommonSubsequenceDP(text1, text2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

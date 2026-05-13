"""
Interleaving String
Given strings s1, s2, and s3,
find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: true
    Explanation: One way to obtain s3 is:
    Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
    Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
    Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: false
    Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
    Input: s1 = "", s2 = "", s3 = ""
    Output: true

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""

import unittest


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # fill the first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # fill the first raw
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[k]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[k]

                dp[i][j] = from_s1 or from_s2

        return dp[m][n]

    def isInterleaveDFS(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(i, j):
            k = i + j

            if i == len(s1) and j == len(s2):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            result = False

            if i < len(s1) and s1[i] == s3[k]:
                result = dfs(i + 1, j)

            if not result and j < len(s2) and s2[j] == s3[k]:
                result = dfs(i, j + 1)

            memo[(i, j)] = result
            return memo[(i, j)]

        return dfs(0, 0)


class TestIsInterleave(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # "aa"+"dbbc"+"bc"+"a"+"c" = "aadbbcbcac"
        self.assertTrue(self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_example2(self):
        # impossible to interleave
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_empty_strings(self):
        # all empty
        self.assertTrue(self.solution.isInterleave("", "", ""))

    def test_length_mismatch(self):
        # len(s1) + len(s2) != len(s3) → always False
        self.assertFalse(self.solution.isInterleave("abc", "def", "abcde"))

    def test_one_empty_s1(self):
        # s1 is empty → s3 must equal s2
        self.assertTrue(self.solution.isInterleave("", "abc", "abc"))
        self.assertFalse(self.solution.isInterleave("", "abc", "abx"))


if __name__ == "__main__":
    unittest.main(verbosity=2)

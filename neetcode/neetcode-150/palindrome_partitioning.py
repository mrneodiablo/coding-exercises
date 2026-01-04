"""
Docstring for neetcode.neetcode-150.palindrome_partitioning
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

from typing import List
import unittest


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            # Base case: cut at final string
            if start == len(s):
                res.append(path.copy())
                return

            # try all cutting way at start point
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]

                if piece == piece[::-1]:  # if palindrome
                    path.append(piece)
                    backtrack(end, path)  # start the rest
                    path.pop()  # Backtrack: try another way

        backtrack(0, [])
        return res


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case with 'aab' - should return [['a','a','b'],['aa','b']]"""
        s = "aab"
        result = self.solution.partition(s)
        expected = [["a", "a", "b"], ["aa", "b"]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        """Test case with single character 'a' - should return [['a']]"""
        s = "a"
        result = self.solution.partition(s)
        expected = [["a"]]
        self.assertEqual(result, expected)

    def test_all_palindrome(self):
        """Test case with 'aba' - should return [['a','b','a'],['aba']]"""
        s = "aba"
        result = self.solution.partition(s)
        expected = [["a", "b", "a"], ["aba"]]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main(verbosity=2)

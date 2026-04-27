"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

import unittest


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        caching = {}

        def bruteForce(i, j):
            if (i, j) in caching:
                return caching[(i, j)]

            if i == len(word1):
                caching[(i, j)] = len(word2) - j  # insert word2[j:]
                return caching[(i, j)]

            if j == len(word2):
                caching[(i, j)] = len(word1) - i  # delete word1[i:]
                return caching[(i, j)]

            if word1[i] == word2[j]:
                caching[(i, j)] = bruteForce(i + 1, j + 1)
                return caching[(i, j)]

            if word1[i] != word2[j]:
                caching[(i, j)] = 1 + min(
                    # replace i
                    bruteForce(i + 1, j + 1),
                    # delete j
                    bruteForce(i + 1, j),
                    # insert
                    bruteForce(i, j + 1),
                )

                return caching[(i, j)]

        return bruteForce(0, 0)


class TestMinDistance(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.minDistance("horse", "ros"), 3)

    def test_example2(self):
        self.assertEqual(self.sol.minDistance("intention", "execution"), 5)

    def test_one_empty_string(self):
        # Converting "" to "abc" requires 3 inserts
        self.assertEqual(self.sol.minDistance("", "abc"), 3)

    def test_identical_strings(self):
        # No operations needed
        self.assertEqual(self.sol.minDistance("same", "same"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

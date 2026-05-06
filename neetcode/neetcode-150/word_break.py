"""
139. Word Break

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

from typing import List
import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)

        def bruteForce(i):
            if i == len(s):
                return True

            if cache[i] is not None:
                return cache[i]

            for w in wordDict:
                if s[i:].startswith(w):
                    if bruteForce(i + len(w)):
                        return True

            cache[i] = False
            return False

        return bruteForce(0)


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertTrue(self.sol.wordBreak("leetcode", ["leet", "code"]))

    def test_example2(self):
        # reuse "apple" twice
        self.assertTrue(self.sol.wordBreak("applepenapple", ["apple", "pen"]))

    def test_example3(self):
        # cannot segment "catsandog"
        self.assertFalse(
            self.sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        )

    def test_single_word(self):
        self.assertTrue(self.sol.wordBreak("dog", ["dog"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)

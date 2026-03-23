"""
127. Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        queue = deque([beginWord])
        visited = {beginWord}
        level = 1

        while queue:
            for i in range(len(queue)):

                word = queue.popleft()

                if word == endWord:
                    return level

                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            level += 1
        return 0

    def ladderLengthDFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        output = []

        def dfs(nextword: str, visited: set, level: int):

            if nextword == endWord:
                output.append(level)
                return

            if (nextword in visited) or (nextword not in wordList):
                return

            # checking
            for i in range(len(nextword)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = nextword[:i] + c + nextword[i + 1:]
                    visited.add(nextword)
                    dfs(new_word, visited, level + 1)
                    visited.remove(nextword)

        wordList.append(beginWord)

        dfs(beginWord, set(), 1)

        return 0 if not output else min(output)


class TestWordLadder(unittest.TestCase):

    def test_example_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 5)

    def test_example_2_endword_not_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        result = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)

    def test_one_step_transformation(self):
        # beginWord và endWord chỉ khác 1 chữ → 2 bước
        beginWord = "hot"
        endWord = "dot"
        wordList = ["dot"]
        result = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 2)

    def test_no_possible_transformation(self):
        # không có đường biến đổi nào từ beginWord đến endWord
        beginWord = "hit"
        endWord = "xyz"
        wordList = ["xyz", "abc", "def"]
        result = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

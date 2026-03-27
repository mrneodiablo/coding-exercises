"""
Alien Dictionary

There is a foreign language which uses the latin alphabet,
but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary,
where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid,
return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.

Example 1:

Input: ["z","o"]
Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # invalid case: "ab" trước "a"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        queue = deque(c for c in in_degree if in_degree[c] == 0)
        ans = []

        while queue:
            c = queue.popleft()
            ans.append(c)
            for neigbor in adj[c]:
                in_degree[neigbor] -= 1
                if in_degree[neigbor] == 0:
                    queue.append(neigbor)

        return "".join(ans) if len(ans) == len(in_degree) else ""

    def foreignDictionaryDFS(self, words: List[str]) -> str:

        ans = []

        # Bước 1: build graph
        adj = {}  # tất cả unique chars
        for word in words:
            for c in word:
                adj[c] = set()

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # invalid case: "ab" "a"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # DFS
        visited = {}

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visited[c] = False
            ans.append(c)

        for c in adj:
            if dfs(c):
                return ""

        return "".join(reversed(ans))


class TestAlienDictionary(unittest.TestCase):

    def test_example_1_two_words(self):
        # "z" trước "o" → z < o
        words = ["z", "o"]
        result = Solution().foreignDictionary(words)
        self.assertEqual(result, "zo")

    def test_example_2_five_words(self):
        words = ["hrn", "hrf", "er", "enn", "rfnn"]
        result = Solution().foreignDictionary(words)
        self.assertEqual(result, "hernf")

    def test_invalid_prefix_order(self):
        # "ab" đứng trước "a" → invalid vì "a" là prefix của "ab"
        words = ["ab", "a"]
        result = Solution().foreignDictionary(words)
        self.assertEqual(result, "")

    def test_single_word(self):
        # chỉ có 1 từ → không suy ra được thứ tự nào → return các ký tự unique
        words = ["abc"]
        result = Solution().foreignDictionary(words)
        self.assertIn(result, ["abc", "acb", "bac", "bca", "cab", "cba"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

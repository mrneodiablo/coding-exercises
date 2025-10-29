"""
Word Search II

Given an m x n board of characters and a list of strings words,
return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

EX1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

EX2:
Input: board = [["a","b"],["c","d"]],
words = ["abcb"]
Output: []
"""

from typing import List


class Solution:
    def findWords(self,
                  board: List[List[str]],
                  words: List[str]) -> List[str]:
        output = set()
        data_trie = {}

        # Create proper visited matrix
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(row, col, node, word):
            # Base case: out of bounds
            if (row < 0 or
                    row >= len(board) or
                    col < 0 or
                    col >= len(board[0])):
                return

            # Base case: already visited
            if visited[row][col]:
                return

            # Base case: character not in trie
            char = board[row][col]
            if char not in node:
                return

            # Move to next node in trie
            node = node[char]
            word += char  # Build the word as we go

            # Mark as visited
            visited[row][col] = True

            if "*" in node:
                output.add(word)

            # Explore 4 directions
            # right, down, left, up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                dfs(new_row, new_col, node, word)

            # Backtrack: unmark as visited
            visited[row][col] = False

        # build data trie
        for word in words:
            current_node = data_trie
            for w in word:
                if not current_node.get(w):
                    current_node[w] = {}
                current_node = current_node[w]
            current_node["*"] = 1

        # Start DFS from every cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, data_trie, "")

        return output


s = Solution()
print(
    s.findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
)

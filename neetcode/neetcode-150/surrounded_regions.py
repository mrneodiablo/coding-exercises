"""
130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board.
Such regions are completely enclosed by 'X' cells.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board.
You do not need to return anything.



Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Example 2:

Input: board = [["X"]]

Output: [["X"]]



Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dimensions = [
            (0, -1),  # left
            (0, 1),  # right
            (-1, 0),  # up
            (1, 0),  # down
        ]

        def dfs(cell):
            if board[cell[0]][cell[1]] != "O":
                return

            board[cell[0]][cell[1]] = "S"
            for dimension in dimensions:
                next_row = cell[0] + dimension[0]
                next_column = cell[1] + dimension[1]

                if (
                    (0 <= next_row < len(board)) and (0 <= next_column < len(board[0])) and board[next_row][next_column] == "O"
                ):
                    dfs((next_row, next_column))

        # Find all cell in. the edge, that cannot capture
        for row in range(len(board)):
            for column in range(len(board[0])):
                if row in [0, (len(board) - 1)] or column in [0, len(board[0]) - 1]:
                    dfs((row, column))

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == "O":
                    board[row][column] = "X"
                if board[row][column] == "S":
                    board[row][column] = "O"

    def solveBFS(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dimensions = [
            (0, -1),  # left
            (0, 1),  # right
            (-1, 0),  # up
            (1, 0),  # down
        ]
        queue = deque()
        visited = set()

        # Find all cell in. the edge, that cannot capture
        for row in range(len(board)):
            for column in range(len(board[0])):
                if row in [0, (len(board) - 1)] or column in [0, len(board[0]) - 1]:
                    if board[row][column] == "O":
                        queue.append((row, column))

        while queue:
            connect = queue.popleft()
            if connect not in visited:
                board[connect[0]][connect[1]] = "S"
                visited.add(connect)
                for dimension in dimensions:
                    next_row = connect[0] + dimension[0]
                    next_column = connect[1] + dimension[1]

                    if (
                        (0 <= next_row < len(board)) and (0 <= next_column < len(board[0])) and board[next_row][next_column] == "O"
                    ):
                        queue.append((next_row, next_column))

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == "O":
                    board[row][column] = "X"
                if board[row][column] == "S":
                    board[row][column] = "O"


class TestSurroundedRegions(unittest.TestCase):

    def test_example_1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        Solution().solve(board)
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],  # O ở edge không bị capture
        ]
        self.assertEqual(board, expected)

    def test_example_2_single_cell(self):
        board = [["X"]]
        Solution().solve(board)
        self.assertEqual(board, [["X"]])

    def test_all_os_connected_to_edge(self):
        # Tất cả O đều kết nối với edge → không cái nào bị capture
        board = [["X", "X", "X"], ["O", "O", "O"], ["X", "X", "X"]]
        Solution().solve(board)
        expected = [
            ["X", "X", "X"],
            ["O", "O", "O"],  # không bị capture vì kết nối edge
            ["X", "X", "X"],
        ]
        self.assertEqual(board, expected)

    def test_surrounded_region_fully_captured(self):
        # O ở giữa hoàn toàn bị bao quanh bởi X → bị capture
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "X"],
        ]
        Solution().solve(board)
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        self.assertEqual(board, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

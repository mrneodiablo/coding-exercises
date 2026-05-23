"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
    Input: matrix = [[1]]
    Output: 1
"""

import unittest
from typing import List
from collections import deque


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        in_degree = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        (0 <= ni < rows)
                        and (0 <= nj < cols)
                        and (matrix[ni][nj] > matrix[i][j])
                    ):
                        in_degree[ni][nj] += 1

        queue = deque(
            [(i, j) for i in range(rows) for j in range(cols) if in_degree[i][j] == 0]
        )

        layer = 0
        while queue:
            layer += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        (0 <= ni < rows)
                        and (0 <= nj < cols)
                        and (matrix[ni][nj] > matrix[i][j])
                    ):
                        in_degree[ni][nj] -= 1
                        if in_degree[ni][nj] == 0:
                            queue.append((ni, nj))

        return layer

    def longestIncreasingPathDFS(self, matrix: List[List[int]]) -> int:
        memo = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            result = 1

            for di, dj in [
                (0, 1),  # right
                (0, -1),  # left
                (1, 0),  # under
                (-1, 0),  # on
            ]:
                ni = i + di
                nj = j + dj

                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    result = max(result, 1 + dfs(ni, nj))
            memo[(i, j)] = result

            return result

        return max(dfs(i, j) for i in range(rows) for j in range(cols))


class TestLongestIncreasingPath(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # path: 1 → 2 → 6 → 9
        matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_example2(self):
        # path: 3 → 4 → 5 → 6
        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_single_cell(self):
        matrix = [[1]]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 1)

    def test_strictly_increasing_row(self):
        # path: 1 → 2 → 3 → 4 → 5, length 5
        matrix = [[1, 2, 3, 4, 5]]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)

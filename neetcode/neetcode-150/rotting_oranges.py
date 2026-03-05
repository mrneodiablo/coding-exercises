"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

"""

from collections import deque
from typing import List
import unittest


class Solution:
    def orangesRottingBruteForce(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh_orange = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_orange += 1

        while True:
            new_rotten = []
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and (grid[nr][nc] == 2):
                                new_rotten.append((r, c))
                                break
            if not new_rotten:
                break

            for r, c in new_rotten:
                grid[r][c] = 2
                fresh_orange -= 1

            minutes += 1
        return minutes if fresh_orange == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ans = 0
        fresh_orange = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh_orange += 1

        while queue:
            length_queue = len(queue)
            is_rotten = False
            for _ in range(length_queue):
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh_orange -= 1
                        queue.append((nr, nc))
                        is_rotten = True

            if is_rotten:
                ans += 1

        return -1 if fresh_orange > 0 else ans


class TestOrangesRotting(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Rotten spreads to all fresh oranges in 4 minutes
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(self.solution.orangesRotting(grid), 4)

    def test_example_2_impossible(self):
        # Bottom-left fresh orange is isolated, impossible to rot
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)

    def test_no_fresh_oranges(self):
        # No fresh oranges at all, answer is 0
        grid = [[0, 2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

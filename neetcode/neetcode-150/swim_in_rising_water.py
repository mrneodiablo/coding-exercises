"""
778. Swim in Rising Water

You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time.
At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
You can swim infinite distances in zero time.
Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1)
if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Constraints:
    n == grid.length
    n == grid[i].length
    1 <= n <= 50
    0 <= grid[i][j] < n2
    Each value grid[i][j] is unique.

"""

import unittest
from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        result = float("inf")

        def dfs(row, col, current_max):
            nonlocal result
            if row == n - 1 and col == n - 1:
                result = min(result, current_max)
                return

            visited.add((row, col))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr <= n - 1 and 0 <= nc <= n - 1 and (nr, nc) not in visited:
                    dfs(nr, nc, max(current_max, grid[nr][nc]))

            visited.remove((row, col))

        dfs(0, 0, grid[0][0])
        return result

    def swimInWaterDijkstra(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # (value, row, col)
        minheap = [(grid[0][0], 0, 0)]
        visited = set()

        while minheap:
            time, row, col = heapq.heappop(minheap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == n - 1 and col == n - 1:
                return time

            for r, c in [
                # on
                (-1, 0),
                # under
                (1, 0),
                # left
                (0, -1),
                # right
                (0, 1),
            ]:
                if (
                    ((row + r, col + c) not in visited)
                    and (0 <= row + r <= n - 1)
                    and (0 <= col + c <= n - 1)
                ):
                    heapq.heappush(
                        minheap, (max(time, grid[row + r][col + c]), row + r, col + c)
                    )
        return 0


class TestSwimInWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # 2x2 grid: must wait until t=3 to reach (1,1)
        grid = [[0, 2], [1, 3]]
        self.assertEqual(self.solution.swimInWater(grid), 3)

    def test_example2(self):
        # 5x5 grid: optimal path requires waiting until t=16
        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        self.assertEqual(self.solution.swimInWater(grid), 16)

    def test_single_cell(self):
        # 1x1 grid: already at destination, answer is the elevation value
        grid = [[0]]
        self.assertEqual(self.solution.swimInWater(grid), 0)

    def test_obstacle_in_middle(self):
        # Best path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2), max elevation = 5
        grid = [
            [0, 1, 5],
            [9, 8, 2],
            [7, 6, 3],
        ]
        self.assertEqual(self.solution.swimInWater(grid), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)

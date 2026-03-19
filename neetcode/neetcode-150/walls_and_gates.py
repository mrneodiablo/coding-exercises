"""
286. Walls And Gates - Explanation
Problem Link

Description
You are given a m×n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]


Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [
            (0, -1),  # left
            (0, 1),  # right
            (-1, 0),  # up
            (1, 0),  # down
        ]
        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            cell = queue.popleft()

            for direction in directions:
                new_r = direction[0] + cell[0]
                new_c = direction[1] + cell[1]
                if (
                    0 <= new_r < len(grid)
                    and 0 <= new_c < len(grid[0])
                    and grid[new_r][new_c] == 2147483647
                ):
                    grid[new_r][new_c] = grid[cell[0]][cell[1]] + 1
                    queue.append((new_r, new_c))

    def islandsAndTreasureSingleDatasource(self, grid: List[List[int]]) -> None:

        directions = [
            (0, -1),  # left
            (0, 1),  # right
            (-1, 0),  # up
            (1, 0),  # down
        ]
        queue = deque()
        treasures = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasures.append((row, col))

        for tr in treasures:
            queue.append(tr)
            while queue:
                cell = queue.popleft()

                for direction in directions:
                    new_r = direction[0] + cell[0]
                    new_c = direction[1] + cell[1]
                    if (
                        0 <= new_r < len(grid)
                        and 0 <= new_c < len(grid[0])
                        and grid[new_r][new_c] not in [0, -1]
                    ):
                        if grid[cell[0]][cell[1]] + 1 <= grid[new_r][new_c]:
                            grid[new_r][new_c] = grid[cell[0]][cell[1]] + 1
                            queue.append((new_r, new_c))


class TestWallsAndGates(unittest.TestCase):

    def test_single_gate(self):
        # Chỉ có 1 treasure chest ở giữa
        INF = 2147483647
        grid = [[INF, INF, INF], [INF, 0, INF], [INF, INF, INF]]
        Solution().islandsAndTreasure(grid)
        expected = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        self.assertEqual(grid, expected)

    def test_all_walls(self):
        # Toàn bộ là walls → grid không đổi
        grid = [[-1, -1], [-1, -1]]
        Solution().islandsAndTreasure(grid)
        expected = [[-1, -1], [-1, -1]]
        self.assertEqual(grid, expected)

    def test_unreachable_land_cell(self):
        # INF bị bao quanh bởi walls → không reach được treasure → giữ nguyên INF
        INF = 2147483647
        grid = [[0, -1, INF], [-1, -1, -1], [INF, -1, 0]]
        Solution().islandsAndTreasure(grid)
        expected = [[0, -1, INF], [-1, -1, -1], [INF, -1, 0]]
        self.assertEqual(grid, expected)

    def test_example_1(self):
        INF = 2147483647
        grid = [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ]
        Solution().islandsAndTreasure(grid)
        expected = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
        self.assertEqual(grid, expected)

    def test_example_2(self):
        INF = 2147483647
        grid = [[0, -1], [INF, INF]]
        Solution().islandsAndTreasure(grid)
        expected = [[0, -1], [1, 2]]
        self.assertEqual(grid, expected)

    def test_no_treasure(self):
        # Không có treasure chest → tất cả INF giữ nguyên
        INF = 2147483647
        grid = [[INF, INF], [INF, INF]]
        Solution().islandsAndTreasure(grid)
        expected = [[INF, INF], [INF, INF]]
        self.assertEqual(grid, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

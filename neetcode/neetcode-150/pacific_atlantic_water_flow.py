"""
417. Pacific Atlantic Water Flow
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(cell, visited: set) -> set:
            visited.add(cell)
            for direction in directions:
                nr, nc = cell[0] + direction[0], cell[1] + direction[1]
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[cell[0]][cell[1]]
                ):
                    dfs((nr, nc), visited)

        pacific = set()
        atlantic = set()

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0) and (r, c) not in pacific:
                    dfs((r, c), pacific)
                if (r == rows - 1 or c == cols - 1) and (r, c) not in atlantic:
                    dfs((r, c), atlantic)

        return [list(cell) for cell in pacific & atlantic]

    def pacificAtlanticBFS(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        dimensions = [
            (0, -1),  # left
            (0, 1),  # right
            (-1, 0),  # up
            (1, 0),  # down
        ]

        # find all cell can reach pacific
        init_pacific = []
        visited_pacific = set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    init_pacific.append((r, c))
        queue_pacific = deque(init_pacific)
        while queue_pacific:
            cell = queue_pacific.popleft()
            if cell not in visited_pacific:
                visited_pacific.add(cell)
                pacific_reachable.add(cell)
                for dimension in dimensions:
                    next_row = cell[0] + dimension[0]
                    next_column = cell[1] + dimension[1]
                    if (
                        (0 <= next_row < len(heights))
                        and (0 <= next_column < len(heights[0]))
                        and heights[next_row][next_column] >= heights[cell[0]][cell[1]]
                        and heights[next_row][next_column] not in pacific_reachable
                    ):
                        queue_pacific.append((next_row, next_column))

        # find all cell can reach atlantic
        init_atlantic = []
        visited_atlantic = set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    init_atlantic.append((r, c))
        queue_atlantic = deque(init_atlantic)
        while queue_atlantic:
            cell = queue_atlantic.popleft()
            if cell not in visited_atlantic:
                visited_atlantic.add(cell)
                atlantic_reachable.add(cell)
                for dimension in dimensions:
                    next_row = cell[0] + dimension[0]
                    next_column = cell[1] + dimension[1]
                    if (
                        (0 <= next_row < len(heights))
                        and (0 <= next_column < len(heights[0]))
                        and heights[next_row][next_column] >= heights[cell[0]][cell[1]]
                        and heights[next_row][next_column] not in atlantic_reachable
                    ):
                        queue_atlantic.append((next_row, next_column))

        return [list(cell) for cell in pacific_reachable & atlantic_reachable]


class TestPacificAtlantic(unittest.TestCase):

    def test_example_1(self):
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
        result = Solution().pacificAtlantic(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2_single_cell(self):
        heights = [[1]]
        result = Solution().pacificAtlantic(heights)
        self.assertEqual(result, [[0, 0]])

    def test_all_same_height(self):
        # tất cả cell cùng height → tất cả đều flow được cả 2 ocean
        heights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = Solution().pacificAtlantic(heights)
        expected = [[r, c] for r in range(3) for c in range(3)]
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main(verbosity=2)

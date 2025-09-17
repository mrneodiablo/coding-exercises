"""
Max Area of Island
You are given an m x n binary matrix grid.
An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11,
because the island must be connected 4-directionally.
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area_islands = 0
        checker = {}
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                current_area = 0
                if grid[i][j] == 1 and not checker.get((i, j)):
                    queue.append((i, j))
                    checker[(i, j)] = 1

                    while len(queue) > 0:
                        current = queue.popleft()
                        current_area += 1

                        # left
                        if (
                            current[0] - 1 >= 0
                            and grid[current[0] - 1][current[1]] == 1
                            and not checker.get((current[0] - 1, current[1]))
                        ):
                            queue.append((current[0] - 1, current[1]))
                            checker[(current[0] - 1, current[1])] = 1

                        # right
                        if (
                            current[0] + 1 < len(grid)
                            and grid[current[0] + 1][current[1]] == 1
                            and not checker.get((current[0] + 1, current[1]))
                        ):
                            queue.append((current[0] + 1, current[1]))
                            checker[(current[0] + 1, current[1])] = 1

                        # above
                        if (
                            current[1] - 1 >= 0
                            and grid[current[0]][current[1] - 1] == 1
                            and not checker.get((current[0], current[1] - 1))
                        ):
                            queue.append((current[0], current[1] - 1))
                            checker[(current[0], current[1] - 1)] = 1

                        # under
                        if (
                            current[1] + 1 < len(grid[0])
                            and grid[current[0]][current[1] + 1] == 1
                            and not checker.get((current[0], current[1] + 1))
                        ):
                            queue.append((current[0], current[1] + 1))
                            checker[(current[0], current[1] + 1)] = 1

                    max_area_islands = max(max_area_islands, current_area)

        return max_area_islands


class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem description
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        expected = 6  # Largest island has area 6
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: No islands (all water)
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        expected = 0  # No islands
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: Single large island
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
        expected = 4  # Each island has area 4, max is 4
        result = self.solution.maxAreaOfIsland(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_max_area_of_island():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Example from problem description")
    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    expected1 = 6
    result1 = solution.maxAreaOfIsland(grid1)
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: No islands (all water)")
    grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    expected2 = 0
    result2 = solution.maxAreaOfIsland(grid2)
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Two equal islands")
    grid3 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
    expected3 = 4
    result3 = solution.maxAreaOfIsland(grid3)
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Single cell island")
    grid4 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    expected4 = 1
    result4 = solution.maxAreaOfIsland(grid4)
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Entire grid is one island")
    grid5 = [[1, 1], [1, 1]]
    expected5 = 4
    result5 = solution.maxAreaOfIsland(grid5)
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxAreaOfIsland)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "=" * 50)
    test_max_area_of_island()

"""
Given an m x n 2D binary grid grid
which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

import unittest
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checker = {}
        queue = deque()
        lands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1" and
                        not checker.get((i, j))):

                    queue.append((i, j))
                    checker[(i, j)] = 1
                    lands += 1

                    while len(queue) > 0:
                        current_land = queue.popleft()

                        # left
                        if current_land[0] - 1 >= 0:
                            left = (current_land[0] - 1, current_land[1])
                            if (grid[left[0]][left[1]] == "1" and
                                    checker.get(left) is None):

                                queue.append(left)
                                checker[left] = 1

                        # right
                        if current_land[0] + 1 < len(grid):
                            right = (current_land[0] + 1, current_land[1])
                            if (grid[right[0]][right[1]] == "1" and
                                    checker.get(right) is None):

                                queue.append(right)
                                checker[right] = 1

                        # on
                        if current_land[1] - 1 >= 0:
                            above = (current_land[0], current_land[1] - 1)
                            if (grid[above[0]][above[1]] == "1" and
                                    checker.get(above) is None):

                                queue.append(above)
                                checker[above] = 1

                        # under
                        if current_land[1] + 1 < len(grid[0]):
                            under = (current_land[0], current_land[1] + 1)
                            if (grid[under[0]][under[1]] == "1" and
                                    checker.get(under) is None):

                                queue.append(under)
                                checker[under] = 1

        return lands


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Multiple islands - Example 1 from problem
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1  # One large connected island
        result = self.solution.numIslands(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Multiple separate islands -
        # Example 2 from problem
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3  # Three separate islands
        result = self.solution.numIslands(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: No islands - all water
        grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        expected = 0  # No islands
        result = self.solution.numIslands(grid)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_num_islands():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: One large island")
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected1 = 1
    result1 = solution.numIslands(grid1)
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Three separate islands")
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    expected2 = 3
    result2 = solution.numIslands(grid2)
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: No islands (all water)")
    grid3 = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
    expected3 = 0
    result3 = solution.numIslands(grid3)
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Single cell island")
    grid4 = [["1"]]
    expected4 = 1
    result4 = solution.numIslands(grid4)
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Diagonal islands (should be separate)")
    grid5 = [["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]]
    expected5 = 5  # 5 separate islands (diagonal doesn't connect)
    result5 = solution.numIslands(grid5)
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumIslands)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "=" * 50)
    test_num_islands()

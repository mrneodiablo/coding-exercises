"""
Docstring for neetcode.neetcode-150.unique_paths
Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
    Input: m = 3, n = 7
    Output: 28

Example 2:

Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down
"""

import unittest


class Solution:
    def uniquePathsBacktracking(self, m: int, n: int) -> int:
        ans = 0

        def backtracking(path):
            nonlocal ans

            if path[-1][0] >= m or path[-1][1] >= n:
                return

            if path[-1][0] == m - 1 and path[-1][1] == n - 1:
                ans += 1
                return

            # move right
            right = (path[-1][0], path[-1][1] + 1)
            path.append(right)
            backtracking(path)
            path.pop()

            # move bottom
            bottom = (path[-1][0] + 1, path[-1][1])
            path.append(bottom)
            backtracking(path)
            path.pop()

        backtracking([(0, 0)])

        return ans

    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def backtracking(i, j):

            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in cache:
                return cache[(i, j)]

            right_paths = backtracking(i, j + 1)
            down_paths = backtracking(i + 1, j)

            cache[(i, j)] = right_paths + down_paths

            return cache[(i, j)]

        return backtracking(0, 0)


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_3x7_grid(self):
        """Test 3x7 grid should return 28 unique paths"""
        m, n = 3, 7
        expected = 28
        result = self.solution.uniquePaths(m, n)
        self.assertEqual(result, expected)

    def test_case_2_3x2_grid(self):
        """Test 3x2 grid should return 3 unique paths"""
        m, n = 3, 2
        expected = 3
        result = self.solution.uniquePaths(m, n)
        self.assertEqual(result, expected)

    def test_case_3_1x1_grid(self):
        """Test 1x1 grid should return 1 unique path (edge case)"""
        m, n = 1, 1
        expected = 1
        result = self.solution.uniquePaths(m, n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

from typing import List
import unittest


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        R, C = len(grid), len(grid[0])

        def bfs(i, j, rows, cols):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            bfs(i + 1, j, rows, cols)
            bfs(i - 1, j, rows, cols)
            bfs(i, j + 1, rows, cols)
            bfs(i, j - 1, rows, cols)

        for i in range(0, R):
            for j in range(0, C):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j, R, C)
        return islands


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expect = 1
        self.assertEqual(
            str(self.solution.numIslands(grid)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expect = 3
        self.assertEqual(
            str(self.solution.numIslands(grid)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

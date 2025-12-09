from typing import List
import unittest


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        lower = 0
        higher = row * col - 1
        while lower <= higher:
            middle = (lower + higher) // 2
            r, c = divmod(middle, col)
            if target < matrix[r][c]:
                higher = middle - 1
            elif target > matrix[r][c]:
                lower = middle + 1
            else:
                return True
        return False


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 13
        expect = False
        self.assertEqual(
            str(self.solution.searchMatrix(matrix, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        target = 3
        expect = True
        self.assertEqual(
            str(self.solution.searchMatrix(matrix, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

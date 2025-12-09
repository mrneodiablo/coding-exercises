from typing import List
import unittest


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ans = []
        while left < right and top < bottom:

            # get every thing in top
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1

            # get every things in right
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every things in bottom
            for i in range(right - 1, left, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every things in left
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expect = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(
            str(self.solution.spiralOrder(matrix)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expect = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(
            str(self.solution.spiralOrder(matrix)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

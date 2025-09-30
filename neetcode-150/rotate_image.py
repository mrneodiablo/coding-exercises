"""
48. Rotate Image
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        Với bài này đầu tiên là chuyển bị ma trân, sau đó revert row là ra
        """

        # # so transpose matrix
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         # Swap elements across the diagonal
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # # revert row
        # for i in range(n):
        #     matrix[i].reverse()

        n = len(matrix)
        circle = n // 2
        for layer in range(circle):
            first = layer
            last = n - 1 - layer
            # rotation: số bước trên một cạnh (không tính góc cuối)
            for i in range(last - first):
                # Lưu giá trị góc trên-trái
                topLeft = matrix[first][first + i]

                # Dịch chuyển các vị trí 4 cạnh

                # trái lên trên
                matrix[first][first + i] = matrix[last - i][first]

                # dưới sang trái
                matrix[last - i][first] = matrix[last][last - i]

                # phải xuống dưới
                matrix[last][last - i] = matrix[first + i][last]

                # trên sang phải
                matrix[first + i][last] = topLeft

        return matrix


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: 3x3 matrix from problem description"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_run_2(self):
        """Test case 2: 4x4 matrix"""
        matrix = [[5, 1, 9, 11],
                  [2, 4, 8, 10],
                  [13, 3, 6, 7],
                  [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5],
                    [14, 3, 4, 1],
                    [12, 6, 8, 9],
                    [16, 7, 10, 11]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_run_3(self):
        """Test case 3: 1x1 matrix (edge case)"""
        matrix = [[1]]
        expected = [[1]]
        self.solution.rotate(matrix)
        self.assertEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()

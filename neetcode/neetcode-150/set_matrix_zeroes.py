"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix,
if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        element_zero = []

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    element_zero.append((row, column))

        for zero in element_zero:
            # all element in raw zero[0] = 0
            raw = zero[0]
            for i in range(len(matrix[0])):
                matrix[raw][i] = 0

            # all element in column zero[1] = 0
            column = zero[1]
            for i in range(len(matrix)):
                matrix[i][column] = 0


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic matrix with one zero
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Test 1:")
    print(f"Input:  {matrix1}")
    solution.setZeroes(matrix1)
    print(f"Output: {matrix1}")
    print("Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]")
    print()

    # Test case 2: Multiple zeros
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("Test 2:")
    print(f"Input:  {matrix2}")
    solution.setZeroes(matrix2)
    print(f"Output: {matrix2}")
    print("Expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]")
    print()

    # Test case 3: Single row
    matrix3 = [[1, 0, 3]]
    print("Test 3:")
    print(f"Input:  {matrix3}")
    solution.setZeroes(matrix3)
    print(f"Output: {matrix3}")
    print("Expected: [[0, 0, 0]]")
    print()

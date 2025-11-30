"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left <= right and top <= bottom:

            # get the top edge
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # get the right edge
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # get the bottom edge (kiểm tra còn hàng không)
            if top <= bottom:  # ✅ Thêm điều kiện
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # get the left edge (kiểm tra còn cột không)
            if left <= right:  # ✅ Thêm điều kiện
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: 3x3 square matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.spiralOrder(matrix1)
    print("Test 1:")
    print(f"Input:  {matrix1}")
    print(f"Output: {result1}")
    print("Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]")
    print("Explanation: Right→Down→Left→Up→Right→Down")
    print()

    # Test case 2: 3x4 rectangular matrix
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result2 = solution.spiralOrder(matrix2)
    print("Test 2:")
    print(f"Input:  {matrix2}")
    print(f"Output: {result2}")
    print("Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]")
    print("Explanation: Right→Down→Left→Up→Right→Down")
    print()

    # Test case 3: Single row matrix
    matrix3 = [[1, 2, 3, 4]]
    result3 = solution.spiralOrder(matrix3)
    print("Test 3:")
    print(f"Input:  {matrix3}")
    print(f"Output: {result3}")
    print("Expected: [1, 2, 3, 4]")
    print("Explanation: Just go right")
    print()

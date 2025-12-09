"""
Search a 2D Matrix
You are given an m x n integer matrix
matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than
the last integer of the previous row.
Given an integer target, return true
if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:
    def searchMatrix(self,
                     matrix: List[List[int]],
                     target: int) -> bool:

        left = 0
        right = len(matrix) - 1
        match_row = None
        while left <= right:
            middle = (left + right) // 2

            if target < matrix[middle][0]:
                right = middle - 1

            if target > matrix[middle][-1]:
                left = middle + 1

            if matrix[middle][-1] >= target >= matrix[middle][0]:
                match_row = matrix[middle]
                break

        if not match_row:
            return False

        left = 0
        right = len(match_row) - 1
        while left <= right:

            middle = (left + right) // 2

            if target < match_row[middle]:
                right = middle - 1

            elif target > match_row[middle]:
                left = middle + 1
            else:
                return True

        return False


solution = Solution()
print(
    solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        target=3
    )
)

print(
    solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        target=23
    )
)

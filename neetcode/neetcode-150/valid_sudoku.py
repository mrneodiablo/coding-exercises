"""
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain
the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but
is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1,
except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digit = "123456789"

        # Check rows
        for row in board:
            seen = {}
            for cell in row:
                if cell in digit:
                    if cell in seen:
                        return False
                    seen[cell] = True

        # Check columns
        for col in range(9):
            seen = {}
            for row in range(9):
                cell = board[row][col]
                if cell in digit:
                    if cell in seen:
                        return False
                    seen[cell] = True

        # Check 3x3 boxes
        for box_row in range(3):
            for box_col in range(3):
                seen = {}
                # Check each cell in the current 3x3 box
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        cell = board[row][col]
                        if cell in digit:
                            if cell in seen:
                                return False
                            seen[cell] = True

        return True


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Valid Sudoku (from example 1)
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    result1 = solution.isValidSudoku(board1)
    print(f"Test 1 (Valid Sudoku): {result1}")
    print("Expected: True")
    print()

    # Test case 2: Invalid Sudoku - duplicate in 3x3 box (from example 2)
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    result2 = solution.isValidSudoku(board2)
    print(f"Test 2 (Invalid - duplicate in box): {result2}")
    print("Expected: False")
    print()

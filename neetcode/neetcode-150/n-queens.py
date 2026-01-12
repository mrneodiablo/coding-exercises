"""
Docstring for neetcode.neetcode-150.n-queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""

from typing import List
import unittest


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        # possition possible to attack
        cols = set()  # collumns has Queen
        diag1 = set()  # Track positive diagonals (row - col)
        diag2 = set()  # Track negative diagonals (row + col)

        def backtrack(row):
            # Base case: reached the end, found a solution
            if row == n:
                ans.append(["".join(board[i]) for i in range(n)])
                return

            # Try placing queen in each column of current row
            for col in range(n):
                # Check if position is safe
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return ans


class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_equals_1(self):
        """Test case for n=1, single queen on 1x1 board"""
        result = self.solution.solveNQueens(1)
        expected = [["Q"]]
        self.assertEqual(result, expected)

    def test_n_equals_4(self):
        """Test case for n=4, two distinct solutions"""
        result = self.solution.solveNQueens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        # Check if the result has 2 solutions
        self.assertEqual(len(result), 2)
        # Check if both expected solutions are in the result
        for solution in expected:
            self.assertIn(solution, result)

    def test_n_equals_2(self):
        """Test case for n=2, no solution exists"""
        result = self.solution.solveNQueens(2)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

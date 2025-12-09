"""
79. Word Search
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
       word = "ABCCED"
Output: true
"""

from typing import List
import unittest


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board[0])
        n = len(board)

        # DFS
        def dfs(x, y, idx, visited):
            # Base case: Sai ký tự hoặc đã thăm hoặc out-of-bound
            if not (0 <= x < n and 0 <= y < m):
                return False

            if (x, y) in visited:
                return False

            if board[x][y] != word[idx]:
                return False

            # Nếu đi hết word
            if idx == len(word) - 1:
                return True

            # Tách nhánh: visited_new là set mới chứa các ô đã đi
            visited_new = visited | {(x, y)}

            # Thử 4 hướng
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if dfs(x + dx, y + dy, idx + 1, visited_new):
                    return True

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False

        # BFS
        # for i in range(n):
        #     for j in range(m):
        #         if board[i][j] == word[0]:
        #             queue = deque()
        #             queue.append((i, j, 0, set([(i, j)])))
        #             while queue:
        #                 x, y, idx, visited = queue.popleft()

        #                 if idx == len(word) - 1:
        #                     return True

        #                 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #                     nx, ny = x + dx, y + dy
        #                     if (
        #                         0 <= nx < n
        #                         and 0 <= ny < m
        #                         and (nx, ny) not in visited
        #                         and (idx + 1) < len(word)
        #                         and board[nx][ny] == word[idx + 1]
        #                     ):
        #                         queue.append(
        #                           (nx, ny, idx + 1, visited | {(nx, ny)}))
        # return False


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description - Word exists"""
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCCED"
        expected = True
        result = self.solution.exist(board, word)
        self.assertEqual(result, expected)

    def test_run_2(self):
        """Test case 2: Word does not exist
        - letters present but no valid path"""
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "SEE"
        expected = True
        result = self.solution.exist(board, word)
        self.assertEqual(result, expected)

    def test_run_3(self):
        """Test case 3: Word requires backtracking - should return False"""
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCB"
        expected = False
        result = self.solution.exist(board, word)
        self.assertEqual(result, expected)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("WORD SEARCH - TEST CASES")
    print("=" * 50)

    # Test 1: Example from problem description - Word exists
    print("Test 1: Example from problem description - Word exists")
    board1 = [["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]]
    word1 = "ABCCED"
    expected1 = True
    result1 = solution.exist(board1, word1)

    print("  Board:")
    for row in board1:
        print(f"    {row}")
    print(f"  Word: '{word1}'")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print("  Path: A(0,0) → B(0,1) → C(0,2) → C(1,2) → E(2,2) → D(2,1)")
    passed1 = result1 == expected1
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Word does not exist - letters present but no valid path
    print("Test 2: Word does not exist - letters present but no valid path")
    board2 = [["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]]
    word2 = "SEE"
    expected2 = False
    result2 = solution.exist(board2, word2)

    print("  Board:")
    for row in board2:
        print(f"    {row}")
    print(f"  Word: '{word2}'")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print("  Note: Letters S, E, E exist but no adjacent path forms 'SEE'")
    passed2 = result2 == expected2
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Word requires backtracking - should return False
    print("Test 3: Word requires backtracking - should return False")
    board3 = [["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]]
    word3 = "ABCB"
    expected3 = False
    result3 = solution.exist(board3, word3)

    print("  Board:")
    for row in board3:
        print(f"    {row}")
    print(f"  Word: '{word3}'")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Single character word
    print("Test 4: Single character word")
    board4 = [["A", "B"], ["C", "D"]]
    word4 = "A"
    expected4 = True
    result4 = solution.exist(board4, word4)

    print("  Board:")
    for row in board4:
        print(f"    {row}")
    print(f"  Word: '{word4}'")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print("  Note: Simple case - single character exists")
    passed4 = result4 == expected4
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: Word longer than possible
    print("Test 5: Word longer than board size")
    board5 = [["A", "B"], ["C", "D"]]
    word5 = "ABCDEFGH"
    expected5 = False
    result5 = solution.exist(board5, word5)

    print("  Board:")
    for row in board5:
        print(f"    {row}")
    print(f"  Word: '{word5}'")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print("  Note: Word has 8 letters but board only has 4 cells")
    passed5 = result5 == expected5
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()

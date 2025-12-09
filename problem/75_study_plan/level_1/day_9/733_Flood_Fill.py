from typing import List
import unittest


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color:
            return image

        def bfs(r, c):
            if image[r][c] == oldColor:
                image[r][c] = color
                if r >= 1:
                    bfs(r - 1, c)
                if r + 1 < R:
                    bfs(r + 1, c)
                if c >= 1:
                    bfs(r, c - 1)
                if c + 1 < C:
                    bfs(r, c + 1)

        bfs(sr, sc)
        return image


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        # [1,1,1]
        # [1,1,0]
        # [1,0,1]
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        color = 2
        expect = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        self.assertEqual(
            str(self.solution.floodFill(image, sr, sc, color)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        # [1,1,1]
        # [1,1,0]
        # [1,0,1]
        image = [[0, 0, 0], [0, 0, 0]]
        sr = 0
        sc = 0
        color = 0
        expect = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(
            str(self.solution.floodFill(image, sr, sc, color)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

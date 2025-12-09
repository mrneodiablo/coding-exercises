import unittest


class Solution:
    # 1  1  1  1   1   1  1
    # 1  2  3  4   5   6  7
    # 1  3  6  10  15  21 28
    def uniquePaths(self, m: int, n: int) -> int:
        data = []
        for i in range(0, m):
            out_n = []
            for j in range(0, n):
                if i == 0:
                    out_n.append(1)
                else:
                    if j <= 0:
                        out_n.append(1)
                    else:
                        out_n.append(data[i - 1][j] + out_n[j - 1])
            data.append(out_n)
        return data[len(data) - 1][-1:][0]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        m = 3
        n = 7
        expect = 28
        self.assertEqual(
            str(self.solution.uniquePaths(m, n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        m = 3
        n = 2
        expect = 3
        self.assertEqual(
            str(self.solution.uniquePaths(m, n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

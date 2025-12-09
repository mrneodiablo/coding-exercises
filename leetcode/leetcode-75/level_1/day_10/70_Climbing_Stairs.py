import unittest

# n = 1:
# 1
# ==> 1

# n = 2
# 1 1
# 2
# ==> 2

# n = 3
# 1 1 1
# 1 2
# 2 1
# --> 3

# n = 4
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2
# --> 5

# n = 5
# 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 2 2 1
# 2 1 2
# 1 2 2
# ==> Fibonaci number


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        fibonaci = [1, 2]
        for i in range(3, n + 1):
            number = fibonaci[i - 2 - 1] + fibonaci[i - 1 - 1]
            fibonaci.append(number)
        return number


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        n = 2
        expect = 2
        self.assertEqual(
            str(self.solution.climbStairs(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        n = 3
        expect = 3
        self.assertEqual(
            str(self.solution.climbStairs(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

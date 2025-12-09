import unittest


class Solution:
    def fib(self, n: int) -> int:
        fibonacci_list = [0, 1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n + 1):
            number = fibonacci_list[i - 1] + fibonacci_list[i - 2]
            fibonacci_list.append(number)
        return number


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        n = 2
        expect = 1
        self.assertEqual(
            str(self.solution.fib(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        n = 3
        expect = 2
        self.assertEqual(
            str(self.solution.fib(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        n = 4
        expect = 3
        self.assertEqual(
            str(self.solution.fib(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

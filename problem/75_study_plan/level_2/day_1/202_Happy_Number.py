import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        break_loop = set()
        while n != 1:
            if n in break_loop:
                return False

            tmp = 0
            break_loop.add(n)
            for i in str(n):
                tmp += int(i) ** 2
            n = tmp
        return True


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        n = 19
        expect = True
        self.assertEqual(
            str(self.solution.isHappy(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        n = 2
        expect = False
        self.assertEqual(
            str(self.solution.isHappy(n)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

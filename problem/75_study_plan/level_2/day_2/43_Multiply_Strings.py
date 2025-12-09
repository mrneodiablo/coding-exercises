import unittest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {
            "0": 48,
            "1": 49,
            "2": 50,
            "3": 51,
            "4": 52,
            "5": 53,
            "6": 54,
            "7": 55,
            "8": 56,
            "9": 57,
        }
        int_num1 = 0
        int_num2 = 0

        for i, s in enumerate(num1):
            int_num1 += (dic[s] - 48) * 10 ** (len(num1) - i - 1)

        for i, s in enumerate(num2):
            int_num2 += (dic[s] - 48) * 10 ** (len(num2) - i - 1)

        return str(int_num1 * int_num2)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        num1 = "2"
        num2 = "3"
        expect = "6"
        self.assertEqual(
            str(self.solution.multiply(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        num1 = "123"
        num2 = "456"
        expect = "56088"
        self.assertEqual(
            str(self.solution.multiply(num1, num2)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

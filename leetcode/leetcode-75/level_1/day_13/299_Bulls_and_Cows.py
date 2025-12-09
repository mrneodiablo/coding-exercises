from typing import Counter
import unittest


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = Counter(secret) - Counter(guess)
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows = len(secret) - sum(dic.values()) - bulls
        return str(bulls) + "A" + str(cows) + "B"


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    # def test_run_1(self):
    #     secret = "1807"
    #     guess = "7810"
    #     expect = "1A3B"
    #     self.assertEqual(
    #         str(self.solution.getHint(secret, guess)),
    #         str(expect),
    #         "incorrect, expect is " + str(expect)
    #     )

    # def test_run_2(self):
    #     secret = "1123"
    #     guess  = "0111"
    #     expect = "1A1B"
    #     self.assertEqual(
    #         str(self.solution.getHint(secret, guess)),
    #         str(expect),
    #         "incorrect, expect is " + str(expect)
    #     )

    # def test_run_3(self):
    #     secret = "1122"
    #     guess  = "2211"
    #     expect = "0A4B"
    #     self.assertEqual(
    #         str(self.solution.getHint(secret, guess)),
    #         str(expect),
    #         "incorrect, expect is " + str(expect)
    #     )

    def test_run_4(self):
        secret = "1122"
        guess = "1222"
        expect = "3A0B"
        self.assertEqual(
            str(self.solution.getHint(secret, guess)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

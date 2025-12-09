import unittest


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """_summary_
        Args:
            s (str): _description_

        Returns:
            int: longest palindrome

        Example:
            Input: s = "abccccdd"
            Output: 7
            Explanation: One longest palindrome that can be built is "dccaccd",
            whose length is 7.
        """
        counter = {}
        out = 0
        for char in s:
            if counter.get(char) is None:
                counter[char] = 1
            else:
                counter[char] += 1

        odd = 0
        for value in counter.values():
            if value > 1:
                if value % 2 == 0:
                    out += value
                else:
                    out += value - 1
                    odd += 1
            else:
                odd += 1

        return out + 1 if odd > 0 else out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        prices = "abccccdd"
        expect = 7
        self.assertEqual(
            self.solution.longestPalindrome(prices),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        prices = "a"
        expect = 1
        self.assertEqual(
            self.solution.longestPalindrome(prices),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

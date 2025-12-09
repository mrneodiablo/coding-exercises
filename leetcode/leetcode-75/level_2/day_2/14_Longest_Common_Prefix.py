from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        for i, s in enumerate(strs[0]):
            if strs[0][i] != strs[-1][i]:
                return ans
            ans += s

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        strs = ["flower", "flow", "flight"]
        expect = "fl"
        self.assertEqual(
            str(self.solution.longestCommonPrefix(strs)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        strs = ["dog", "racecar", "car"]
        expect = ""
        self.assertEqual(
            str(self.solution.longestCommonPrefix(strs)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        for i in range(len(s)):
            dic = {}
            counter = 0
            for j in range(i, len(s)):
                if dic.get(s[j]) is not None:
                    ans = max(ans, counter)
                    break
                dic[s[j]] = 1
                counter += 1
                ans = max(ans, counter)
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "au"
        expect = 2
        self.assertEqual(
            str(self.solution.lengthOfLongestSubstring(s)),
            str(expect),
            "incorrect, expect is " + str(expect))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

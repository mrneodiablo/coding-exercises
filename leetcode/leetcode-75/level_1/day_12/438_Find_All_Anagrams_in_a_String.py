from typing import List
import unittest


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        sort_p = list(p)
        sort_p.sort()
        for i in range(0, len(s) - len(p) + 1):
            compare = list(s[i: i + len(p)])
            compare.sort()
            if compare == sort_p:
                out.append(i)
        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        s = "cbaebabacd"
        p = "abc"
        expect = [0, 6]
        self.assertEqual(
            str(self.solution.findAnagrams(s, p)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        s = "abab"
        p = "ab"
        expect = [0, 1, 2]
        self.assertEqual(
            str(self.solution.findAnagrams(s, p)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for character in s:
            if character in t:
                index = t.index(character)
                t = str(t[index + 1:])
            else:
                return False
        return True


class TestSequenceFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "abc"
        t = "ahbgdc"
        expect = True
        self.assertEqual(
            self.solution.isSubsequence(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        s = "axc"
        t = "ahbgdc"
        expect = False
        self.assertEqual(
            self.solution.isSubsequence(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        s = "axc"
        t = "acxbgd"
        expect = False
        self.assertEqual(
            self.solution.isSubsequence(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

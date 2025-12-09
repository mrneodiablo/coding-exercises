import unittest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        if s == t:
            return True

        for i in s:
            if i == "#":
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(i)

        for i in t:
            if i == "#":
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(i)

        return stack_s == stack_t


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        s = "ab#c"
        t = "ad#c"
        expect = True
        self.assertEqual(
            str(self.solution.backspaceCompare(s, t)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        s = "ab##"
        t = "c#d#"
        expect = True
        self.assertEqual(
            str(self.solution.backspaceCompare(s, t)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        s = "a#c"
        t = "b"
        expect = False
        self.assertEqual(
            str(self.solution.backspaceCompare(s, t)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

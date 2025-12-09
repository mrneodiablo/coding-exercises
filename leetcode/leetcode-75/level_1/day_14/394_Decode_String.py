import unittest


class Solution:
    def decodeString(self, s: str) -> bool:
        out = ""
        k = 0
        stack = []
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)  # for two and three digit numbers
            elif c == "[":
                stack.append((out, k))
                out, k = "", 0  # reset global vars
            elif c == "]":
                enc, n = stack.pop()
                out = enc + n * out
            else:
                out += c  # track the lower case letters

        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        s = "3[a]2[bc]"
        expect = "aaabcbc"
        self.assertEqual(
            str(self.solution.decodeString(s)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        s = "3[a2[c]]"
        expect = "accaccacc"
        self.assertEqual(
            str(self.solution.decodeString(s)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    # def test_run_3(self):
    #     s = "2[abc]3[cd]ef"
    #     expect = "abcabccdcdcdef"
    #     self.assertEqual(
    #         str(self.solution.decodeString(s)),
    #         str(expect),
    #         "incorrect, expect is " + str(expect)
    #     )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checking = {}
        added_values = []
        for i, character in enumerate(s):
            if checking.get(character) is None:
                if t[i] not in added_values:
                    checking[character] = t[i]
                    added_values.append(t[i])
                    continue
                return False
            if checking.get(character) != t[i]:
                return False
        return True


class TestSequenceFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        s = "egg"
        t = "add"
        expect = True
        self.assertEqual(
            self.solution.isIsomorphic(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        s = "foo"
        t = "bar"
        expect = False
        self.assertEqual(
            self.solution.isIsomorphic(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        s = "paper"
        t = "title"
        expect = True
        self.assertEqual(
            self.solution.isIsomorphic(s, t),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

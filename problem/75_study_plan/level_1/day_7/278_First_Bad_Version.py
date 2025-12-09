import unittest


def isBadVersion(version: int, badVersion: int) -> int:
    if version == badVersion:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int, badVersion: int) -> int:
        low = 1
        high = n
        midle = (high + low) // 2
        first_bad_version = None

        # if first version is base return anyway
        if isBadVersion(low, badVersion):
            return low

        while high >= low:
            midle_bad_version = isBadVersion(midle, badVersion)

            if midle_bad_version is True:
                first_bad_version = midle
                high = midle - 1
                midle = (high + low) // 2

            if midle_bad_version is False:
                low = midle + 1
                midle = (high + low) // 2

        return first_bad_version


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        num = 5
        badversion = 4
        expect = 4
        self.assertEqual(
            str(self.solution.firstBadVersion(num, badversion)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        num = 1
        badversion = 1
        expect = 1
        self.assertEqual(
            str(self.solution.firstBadVersion(num, badversion)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

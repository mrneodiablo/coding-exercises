from typing import List
import unittest


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        out = [nums[0]]
        for i in range(1, len(nums)):
            out.append(out[i - 1] + nums[i])
        return out


class TestSequenceFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        nums = [1, 2, 3, 4]
        expect = [1, 3, 6, 10]
        self.assertEqual(
            self.solution.running_sum(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        nums = [1, 1, 1, 1, 1]
        expect = [1, 2, 3, 4, 5]
        self.assertEqual(
            self.solution.running_sum(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        nums = [3, 1, 2, 10, 1]
        expect = [3, 4, 6, 16, 17]
        self.assertEqual(
            self.solution.running_sum(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

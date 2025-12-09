from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while high >= low:

            midle = (high + low) // 2

            if nums[midle] == target:
                return midle

            if nums[midle] > target:
                high = midle - 1

            if nums[midle] < target:
                low = midle + 1

        return -1


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expect = 4
        self.assertEqual(
            str(self.solution.search(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expect = -1
        self.assertEqual(
            str(self.solution.search(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        nums = [2, 5]
        target = 2
        expect = 0
        self.assertEqual(
            str(self.solution.search(nums, target)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

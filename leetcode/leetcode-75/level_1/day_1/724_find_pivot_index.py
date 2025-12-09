from typing import List
import unittest


class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


class TestSequenceFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.find_pivot = Solution()

    def test_run_1(self):
        # test case
        nums = [1, 7, 3, 6, 5, 6]
        expect = 3
        self.assertEqual(
            self.find_pivot.pivot_index(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        nums = [1, 2, 3]
        expect = -1
        self.assertEqual(
            self.find_pivot.pivot_index(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        nums = [2, 1, -1]
        expect = 0
        self.assertEqual(
            self.find_pivot.pivot_index(nums),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

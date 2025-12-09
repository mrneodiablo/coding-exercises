"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i in range(len(nums)):
            if not checker.get(nums[i]):
                checker[nums[i]] = [i]
            else:
                checker[nums[i]].append(i)

            first_number = checker.get(target - nums[i])
            if first_number and first_number[0] != i:
                return [first_number[0], i]
        return None


class TestFunctions(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        nums_test = [2, 7, 11, 15]
        target_test = 9
        expect = [0, 1]
        self.assertEqual(
            solution.twoSum(nums_test, target_test),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2(self):
        solution = Solution()
        nums_test = [3, 2, 4]
        target_test = 6
        expect = [1, 2]
        self.assertEqual(
            solution.twoSum(nums_test, target_test),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3(self):
        solution = Solution()
        nums_test = [3, 3]
        target_test = 6
        expect = [0, 1]
        self.assertEqual(
            solution.twoSum(nums_test, target_test),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

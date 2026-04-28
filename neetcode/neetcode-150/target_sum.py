"""
494. Target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List
import unittest


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        caching = {}

        def bruteForce(nums_index, current_sum):

            if nums_index == len(nums):
                return 1 if current_sum == target else 0

            if (nums_index, current_sum) in caching:
                return caching[(nums_index, current_sum)]

            result = bruteForce(
                nums_index + 1, current_sum + nums[nums_index]
            ) + bruteForce(nums_index + 1, current_sum - nums[nums_index])
            caching[(nums_index, current_sum)] = result

            return result

        return bruteForce(0, 0)


class TestFindTargetSumWays(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # 5 ways to make sum = 3 with [1,1,1,1,1]
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_example2(self):
        # Only +1 works
        self.assertEqual(self.sol.findTargetSumWays([1], 1), 1)

    def test_no_ways(self):
        # target unreachable (max sum = 1, target = 2)
        self.assertEqual(self.sol.findTargetSumWays([1], 2), 0)

    def test_zero_target(self):
        # +1-1+1-1 = 0, -1+1-1+1 = 0 → 2 ways
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1, 1], 0), 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Docstring for neetcode.neetcode-150.house_robber
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:

        length_nums = len(nums)

        if length_nums == 1:
            return nums[0]

        if length_nums == 2:
            return max(nums[0], nums[1])

        dp = [0] * length_nums
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, length_nums):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[i]


class TestFunctions(unittest.TestCase):

    def test_case_1_rob_alternate_houses(self):
        """Test case where robbing alternate houses gives maximum"""
        solution = Solution()
        nums = [1, 2, 3, 1]
        expect = 4
        self.assertEqual(
            solution.rob(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_longer_street(self):
        """Test case with longer street requiring optimal selection"""
        solution = Solution()
        nums = [2, 7, 9, 3, 1]
        expect = 12
        self.assertEqual(
            solution.rob(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_single_house(self):
        """Test case with only one house"""
        solution = Solution()
        nums = [5]
        expect = 5
        self.assertEqual(
            solution.rob(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_4_equal_value_houses(self):
        """Test case with houses having similar values at edges"""
        solution = Solution()
        nums = [2, 1, 1, 2]
        expect = 4
        self.assertEqual(
            solution.rob(nums),
            expect,
            f"incorrect, expect is {expect} - rob houses at index 0 and 3",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

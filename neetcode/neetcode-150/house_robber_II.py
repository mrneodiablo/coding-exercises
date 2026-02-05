"""
Docstring for neetcode.neetcode-150.house_robber_II
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.



Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

from typing import List
import unittest


class Solution:
    def rob(self, nums: List[int]) -> int:
        lenth_nums = len(nums)

        if lenth_nums <= 2:
            return max(nums)

        # case 1: rob from 0 to n-2
        # dp1[i] represents max money we can rob from houses[0:n-2]
        dp1 = [0] * (lenth_nums + 1)
        for i in range(0, lenth_nums - 1):
            dp1[i + 2] = max(dp1[i] + nums[i], dp1[i + 1])

        # case 2: rob from 1 to n-1
        # dp2[i] represents max money we can rob from houses[1:n-1]
        dp2 = [0] * (lenth_nums + 2)
        for i in range(1, lenth_nums):
            dp2[i + 2] = max(dp2[i] + nums[i], dp2[i + 1])

        return max(dp1[-1], dp2[-1])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from example 1: [2,3,2] -> 3"""
        nums = [2, 3, 2]
        expected = 3
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Test case from example 2: [1,2,3,1] -> 4"""
        nums = [1, 2, 3, 1]
        expected = 4
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """Test case from example 3: [1,2,3] -> 3"""
        nums = [1, 2, 3]
        expected = 3
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Burst Balloons

You are given n balloons, indexed from 0 to n - 1.
Each balloon is painted with a number on it represented by an array nums.
You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.


Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10


Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

from typing import List
import unittest


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = {}

        def dp(left, right):
            if right - left < 2:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            max_coins = 0
            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]
                total = coins + dp(left, k) + dp(k, right)
                max_coins = max(max_coins, total)

            cache[(left, right)] = max_coins
            return max_coins

        return dp(0, n - 1)

    def maxCoinsBruteForce(self, nums: List[int]) -> int:

        def dfs(balloons):
            if not balloons:
                return 0

            max_coins = 0
            for i in range(len(balloons)):
                left = balloons[i - 1] if i - 1 >= 0 else 1
                right = balloons[i + 1] if i + 1 < len(balloons) else 1
                coins = left * balloons[i] * right

                remaining = balloons[:i] + balloons[i + 1:]
                total = coins + dfs(remaining)
                max_coins = max(max_coins, total)
            return max_coins

        return dfs(nums)


class TestBurstBalloons(unittest.TestCase):

    def test_example_1(self):
        nums = [3, 1, 5, 8]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 167)

    def test_example_2(self):
        nums = [1, 5]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 10)

    def test_single_balloon(self):
        # 1 balloon → 1*nums[0]*1 = nums[0]
        nums = [5]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 5)

    def test_all_ones(self):
        # tất cả balloon = 1 → mỗi lần burst = 1*1*1 = 1
        nums = [1, 1, 1]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 3)  # fix: 3 không phải 4

    def test_two_balloons(self):
        nums = [3, 5]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 20)  # fix: 20 không phải 30

    def test_increasing_order(self):
        nums = [1, 2, 3, 4, 5]
        result = Solution().maxCoins(nums)
        self.assertEqual(result, 110)


if __name__ == "__main__":
    unittest.main(verbosity=2)

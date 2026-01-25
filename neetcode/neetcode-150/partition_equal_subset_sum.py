"""
Docstring for neetcode.neetcode-150.partition_equal_subset_sum
416. Partition Equal Subset Sum
Given an integer array nums,
return true if you can partition the array into two subsets
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import List
import unittest


class Solution:
    def canPartitionImprove(self, nums: List[int]) -> bool:
        # early check
        if len(nums) <= 1:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        # DP with 1D array - need O(target) space
        dp = [False] * (target + 1)
        dp[0] = True  # sum = 0 always true

        # iterate each nums
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

            # Early exit if found
            if dp[target]:
                return True

        return dp[target]

    def canPartition(self, nums: List[int]) -> bool:
        # dung recursive + memory

        # early check
        if len(nums) <= 1:
            return False

        total = sum(nums)

        if total % 2 != 0:
            return False

        memories = {}

        def backtracking(index, current_sum, target):
            # Base cases
            if current_sum == target:
                return True

            if index >= len(nums) or current_sum > target:
                return False

            # Check memoization
            if (index, current_sum) in memories:
                return memories[(index, current_sum)]

            # Try including or excluding current number
            include = backtracking(index + 1, current_sum + nums[index], target)
            exclude = backtracking(index + 1, current_sum, target)

            # Store result in memo
            memories[(index, current_sum)] = include or exclude
            return memories[(index, current_sum)]

        return backtracking(0, 0, total // 2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition_possible(self):
        """Test case where array can be partitioned into equal sum subsets"""
        nums = [1, 5, 11, 5]
        result = self.solution.canPartition(nums)
        self.assertTrue(
            result, "Array [1,5,11,5] can be partitioned as [1,5,5] and [11]"
        )

    def test_partition_impossible(self):
        """Test case where array cannot be partitioned into equal sum subsets"""
        nums = [1, 2, 3, 5]
        result = self.solution.canPartition(nums)
        self.assertFalse(
            result, "Array [1,2,3,5] cannot be partitioned into equal sum subsets"
        )

    def test_single_element(self):
        """Test case with single element - should return False"""
        nums = [100]
        result = self.solution.canPartition(nums)
        self.assertFalse(
            result, "Single element array cannot be partitioned into two equal subsets"
        )

    def test_complex_large_array(self):
        """Complex test case with larger array requiring careful partitioning"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        # Sum = 210, target = 105
        # Can be partitioned: e.g., [20, 19, 18, 17, 16, 15] = 105 and rest = 105
        result = self.solution.canPartition(nums)
        self.assertTrue(
            result,
            "Array [1..20] with sum=210 can be partitioned into two subsets of sum=105 each",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

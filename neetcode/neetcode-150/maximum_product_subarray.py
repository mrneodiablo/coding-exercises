"""
Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.


Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List
import unittest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        cur_max = 1
        cur_min = 1

        for i in range(len(nums)):
            tmp = cur_max
            cur_max = max(nums[i], tmp * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], tmp * nums[i], cur_min * nums[i])
            result = max(result, cur_max)
        return result


class TestMaxProduct(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # [2,3] has product 6
        self.assertEqual(self.sol.maxProduct([2, 3, -2, 4]), 6)

    def test_example2(self):
        # [-2,-1] is not contiguous, answer is 0
        self.assertEqual(self.sol.maxProduct([-2, 0, -1]), 0)

    def test_all_negative(self):
        # [-2,-3] = 6
        self.assertEqual(self.sol.maxProduct([-2, -3, -1]), 6)

    def test_single_element(self):
        self.assertEqual(self.sol.maxProduct([-5]), -5)


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
Maximum Subarray
Given an integer array nums,
find the subarray with the largest sum,
and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = float("-inf")
        summary = 0
        for n in nums:
            if summary + n >= n:
                summary += n
            else:
                summary = n
            max_subarray = max(max_subarray, summary)
        return max_subarray


class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Mixed positive and negative numbers
        # Example from problem description
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6  # subarray [4,-1,2,1] has sum 6
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Single element array
        nums = [1]
        expected = 1  # subarray [1] has sum 1
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: All positive numbers
        nums = [5, 4, -1, 7, 8]
        expected = 23  # entire array [5,4,-1,7,8] has sum 23
        result = self.solution.maxSubArray(nums)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_max_subarray():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Mixed positive/negative [-2,1,-3,4,-1,2,1,-5,4]")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    result1 = solution.maxSubArray(nums1)
    print(f"  Input: {nums1}")
    print(f"  Expected: {expected1} (subarray [4,-1,2,1])")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Single element [1]")
    nums2 = [1]
    expected2 = 1
    result2 = solution.maxSubArray(nums2)
    print(f"  Input: {nums2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: All positive [5,4,-1,7,8]")
    nums3 = [5, 4, -1, 7, 8]
    expected3 = 23
    result3 = solution.maxSubArray(nums3)
    print(f"  Input: {nums3}")
    print(f"  Expected: {expected3} (entire array)")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: All negative [-2,-3,-1,-5]")
    nums4 = [-2, -3, -1, -5]
    expected4 = -1  # best single element
    result4 = solution.maxSubArray(nums4)
    print(f"  Input: {nums4}")
    print(f"  Expected: {expected4} (subarray [-1])")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Two element array [-1,2]")
    nums5 = [-1, 2]
    expected5 = 2  # subarray [2]
    result5 = solution.maxSubArray(nums5)
    print(f"  Input: {nums5}")
    print(f"  Expected: {expected5} (subarray [2])")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxSubArray)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_max_subarray()

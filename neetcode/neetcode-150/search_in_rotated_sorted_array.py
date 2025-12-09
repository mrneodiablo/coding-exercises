"""
Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order
(with distinct values).

Prior to being passed to your function,
nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
such that the resulting array is [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""

import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
                # k in [middle+1, right]
            else:
                right = middle

        k = left

        if nums[-1] >= target >= nums[k]:
            # Search in right part [k, len(nums)-1]
            left, right = k, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        elif k > 0 and nums[k - 1] >= target >= nums[0]:
            # Search in left part [0, k-1]
            left, right = 0, k - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target not found
        return -1


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Target found in rotated array
        # (target in right part)
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        expected = 4
        result = self.solution.search(nums, target)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected},but got {result}")

    def test_run_2(self):
        # Test case 2: Target not found in rotated array
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        expected = -1
        result = self.solution.search(nums, target)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, but got {result}")

    def test_run_3(self):
        # Test case 3: Target found in left part of rotated array
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 6
        expected = 2
        result = self.solution.search(nums, target)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, but got {result}")


def test_search_rotated_array():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Target found in right part (smaller values)")
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    expected1 = 4
    result1 = solution.search(nums1, target1)
    print(f"  Input: nums = {nums1}, target = {target1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Target not found")
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    expected2 = -1
    result2 = solution.search(nums2, target2)
    print(f"  Input: nums = {nums2}, target = {target2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Target found in left part (larger values)")
    nums3 = [4, 5, 6, 7, 0, 1, 2]
    target3 = 6
    expected3 = 2
    result3 = solution.search(nums3, target3)
    print(f"  Input: nums = {nums3}, target = {target3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Single element array")
    nums4 = [1]
    target4 = 1
    expected4 = 0
    result4 = solution.search(nums4, target4)
    print(f"  Input: nums = {nums4}, target = {target4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: No rotation (regular sorted array)")
    nums5 = [1, 2, 3, 4, 5]
    target5 = 3
    expected5 = 2
    result5 = solution.search(nums5, target5)
    print(f"  Input: nums = {nums5}, target = {target5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests for additional verification
    test_search_rotated_array()

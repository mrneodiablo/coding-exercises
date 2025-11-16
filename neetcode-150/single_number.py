"""
Single Number
Given a non-empty array of integers nums,
every element appears twice except for one.
Find that single one.

You must implement a solution with
a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index = 0
        for num in nums:
            index ^= num
        return index


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Single element appears once at the end
    nums1 = [2, 2, 1]
    result1 = solution.singleNumber(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Result: {result1}")
    print("Expected: 1")
    print()

    # Test case 2: Single element in the middle
    nums2 = [4, 1, 2, 1, 2]
    result2 = solution.singleNumber(nums2)
    print(f"Test 2: nums={nums2}")
    print(f"Result: {result2}")
    print("Expected: 4")
    print()

    # Test case 3: Only one element in array
    nums3 = [1]
    result3 = solution.singleNumber(nums3)
    print(f"Test 3: nums={nums3}")
    print(f"Result: {result3}")
    print("Expected: 1")
    print()

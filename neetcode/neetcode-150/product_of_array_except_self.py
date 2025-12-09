"""
Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and
without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # First pass: store product of all elements to the left
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: multiply by product of all elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example
    nums1 = [1, 2, 3, 4]
    result1 = solution.productExceptSelf(nums1)
    print(f"Test 1 - Input: {nums1}")
    print(f"Test 1 - Output: {result1}")
    print("Test 1 - Expected: [24,12,8,6]")
    print(f"Test 1 - Correct: {result1 == [24, 12, 8, 6]}")
    print()

    # Test case 2: With zeros
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    print(f"Test 2 - Input: {nums2}")
    print(f"Test 2 - Output: {result2}")
    print("Test 2 - Expected: [0,0,9,0,0]")
    print(f"Test 2 - Correct: {result2 == [0, 0, 9, 0, 0]}")
    print()

    # Test case 3: Negative numbers
    nums3 = [-2, -3, 4, 5]
    result3 = solution.productExceptSelf(nums3)
    print(f"Test 3 - Input: {nums3}")
    print(f"Test 3 - Output: {result3}")
    print("Test 3 - Expected: [-60,-40,30,24]")
    print(f"Test 3 - Correct: {result3 == [-60, -40, 30, 24]}")
    print()

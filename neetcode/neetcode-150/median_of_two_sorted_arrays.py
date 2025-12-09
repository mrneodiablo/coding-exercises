"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

from typing import List


class Solution:
    """Solution for finding median of two sorted arrays."""

    # pylint: disable=too-many-return-statements
    def findKth(self, arr1, arr2, k):
        """Find kth element in two sorted arrays."""
        # Base cases
        if not arr1:
            return arr2[k]
        if not arr2:
            return arr1[k]
        if k == 0:
            return min(arr1[0], arr2[0])

        # Loại bỏ k/2 phần tử
        mid1 = len(arr1) // 2
        mid2 = len(arr2) // 2
        val1 = arr1[mid1]
        val2 = arr2[mid2]

        if mid1 + mid2 < k:
            # Loại bỏ nửa nhỏ hơn
            if val1 > val2:
                return self.findKth(arr1, arr2[mid2 + 1:], k - mid2 - 1)
            return self.findKth(arr1[mid1 + 1:], arr2, k - mid1 - 1)
        # Loại bỏ nửa lớn hơn
        if val1 > val2:
            return self.findKth(arr1[:mid1], arr2, k)
        return self.findKth(arr1, arr2[:mid2], k)

    def findMedianSortedArrays(self,
                               nums_1: List[int],
                               nums_2: List[int]) -> float:
        """Find median of two sorted arrays."""
        total = len(nums_1) + len(nums_2)

        if total % 2 == 1:
            return self.findKth(nums_1, nums_2, total // 2)
        return (
            self.findKth(nums_1, nums_2, total // 2 - 1)
            + self.findKth(nums_1, nums_2, total // 2)
        ) / 2.0

        # # Ensure nums1 is the smaller array for simplicity
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1
        # n1 = len(nums1)
        # n2 = len(nums2)

        # n = n1 + n2
        # left = (n1 + n2 + 1) // 2  # Calculate the left partition size
        # low = 0
        # high = n1

        # if debug:
        #     print(f"\n{'='*70}")
        #     print(f"INPUT: nums1 = {nums1}, nums2 = {nums2}")
        #     print(f"Tổng = {n}, Cần {left} phần tử bên trái")
        #     print(f"{'='*70}\n")

        # iteration = 0
        # while low <= high:
        #     iteration += 1
        #     mid1 = (low + high) // 2  # Calculate mid index for nums1
        #     mid2 = left - mid1  # Calculate mid index for nums2

        #     l1 = float("-inf")
        #     l2 = float("-inf")
        #     r1 = float("inf")
        #     r2 = float("inf")

        #     # Determine values of l1, l2, r1, and r2
        #     if mid1 < n1:
        #         r1 = nums1[mid1]
        #     if mid2 < n2:
        #         r2 = nums2[mid2]
        #     if mid1 - 1 >= 0:
        #         l1 = nums1[mid1 - 1]
        #     if mid2 - 1 >= 0:
        #         l2 = nums2[mid2 - 1]

        #     if l1 <= r2 and l2 <= r1:
        #         # The partition is correct, we found the median
        #         if debug:
        #             print(f"  ✓ Tìm được partition đúng!")
        #             print(f"  ")
        #         if n % 2 == 1:
        #             result = max(l1, l2)
        #             return result
        #         else:
        #             result = (max(l1, l2) + min(r1, r2)) / 2.0
        #             return result
        #     elif l1 > r2:
        #         # Move towards the left side of nums1
        #         high = mid1 - 1
        #     else:
        #         # Move towards the right side of nums1
        #         low = mid1 + 1

        # return 0


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example 1 from problem - odd total length
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.0, f"Test 1 failed: expected 2.0, got {result}"
    print(f"✓ Test 1 passed: {nums1} + {nums2} = {result}")

    # Test case 2: Example 2 from problem - even total length
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5, f"Test 2 failed: expected 2.5, got {result}"
    print(f"✓ Test 2 passed: {nums1} + {nums2} = {result}")

    # Test case 3: One empty array
    nums1 = []
    nums2 = [1]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1.0, f"Test 3 failed: expected 1.0, got {result}"
    print(f"✓ Test 3 passed: {nums1} + {nums2} = {result}")

    # Test case 4: Both arrays with one element
    nums1 = [1]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1.5, f"Test 4 failed: expected 1.5, got {result}"
    print(f"✓ Test 4 passed: {nums1} + {nums2} = {result}")

    # Test case 5: Arrays with different lengths
    nums1 = [1, 2]
    nums2 = [3, 4, 5, 6]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 3.5, f"Test 5 failed: expected 3.5, got {result}"
    print(f"✓ Test 5 passed: {nums1} + {nums2} = {result}")

    # Test case 6: Negative numbers
    nums1 = [-5, -3, -1]
    nums2 = [-2, 0, 2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == -1.5, f"Test 6 failed: expected -1.5, got {result}"
    print(f"✓ Test 6 passed: {nums1} + {nums2} = {result}")

    # Test case 7: First array empty
    nums1 = []
    nums2 = [2, 3]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 2.5, f"Test 7 failed: expected 2.5, got {result}"
    print(f"✓ Test 7 passed: {nums1} + {nums2} = {result}")

    # Test case 8: All same numbers
    nums1 = [1, 1, 1]
    nums2 = [1, 1]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 1.0, f"Test 8 failed: expected 1.0, got {result}"
    print(f"✓ Test 8 passed: {nums1} + {nums2} = {result}")

    # Test case 9: Large gap between arrays
    nums1 = [1, 2]
    nums2 = [100, 200]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 51.0, f"Test 9 failed: expected 51.0, got {result}"
    print(f"✓ Test 9 passed: {nums1} + {nums2} = {result}")

    # Test case 10: Single element in each array, same values
    nums1 = [5]
    nums2 = [5]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 5.0, f"Test 10 failed: expected 5.0, got {result}"
    print(f"✓ Test 10 passed: {nums1} + {nums2} = {result}")

    # Test case 11: Longer arrays - odd total length
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 5.0, f"Test 11 failed: expected 5.0, got {result}"
    print(f"✓ Test 11 passed: {nums1} + {nums2} = {result}")

    # Test case 12: Arrays with zeros
    nums1 = [0]
    nums2 = [0]
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert result == 0.0, f"Test 12 failed: expected 0.0, got {result}"
    print(f"✓ Test 12 passed: {nums1} + {nums2} = {result}")

    print("\n✅ All test cases passed!")

"""
Kth Largest Element in an Array
Given an integer array nums and an integer k,
return the kth largest element in the array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq
import unittest
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem description
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5  # 2nd largest element
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, but got {result}")

    def test_run_2(self):
        # Test case 2: Array with duplicates
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4  # 4th largest element
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, but got {result}")

    def test_run_3(self):
        # Test case 3: Find largest element (k=1)
        nums = [7, 10, 4, 3, 20, 15]
        k = 1
        expected = 20  # 1st largest element (maximum)
        result = self.solution.findKthLargest(nums, k)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, but got {result}")


def test_kth_largest():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Basic case [3,2,1,5,6,4], k=2")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = solution.findKthLargest(nums1, k1)
    print(f"  Input: nums = {nums1}, k = {k1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Array with duplicates [3,2,3,1,2,4,5,5,6], k=4")
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    print(f"  Input: nums = {nums2}, k = {k2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Find largest element [7,10,4,3,20,15], k=1")
    nums3 = [7, 10, 4, 3, 20, 15]
    k3 = 1
    expected3 = 20
    result3 = solution.findKthLargest(nums3, k3)
    print(f"  Input: nums = {nums3}, k = {k3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Find smallest element (k=len(nums))")
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5  # 5th largest = smallest element
    expected4 = 1
    result4 = solution.findKthLargest(nums4, k4)
    print(f"  Input: nums = {nums4}, k = {k4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Single element array")
    nums5 = [1]
    k5 = 1
    expected5 = 1
    result5 = solution.findKthLargest(nums5, k5)
    print(f"  Input: nums = {nums5}, k = {k5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "=" * 50)
    test_kth_largest()

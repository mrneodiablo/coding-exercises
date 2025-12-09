"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and
using only constant extra space.


Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3
"""

from typing import List
import unittest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = {}
        for n in nums:
            if check.get(n) is not None:
                return n
            check[n] = 1

        return None


# ============== TEST CASES ==============


class TestFindDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1_duplicate_at_end(self):
        """Test Case 1: Duplicate number appears at the end"""
        nums = [1, 3, 4, 2, 2]
        expected = 2
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, expected)
        print(f"✓ Test 1 passed: {nums} → {result}")

    def test_example_2_duplicate_at_beginning(self):
        """Test Case 2: Duplicate number appears early"""
        nums = [3, 1, 3, 4, 2]
        expected = 3
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, expected)
        print(f"✓ Test 2 passed: {nums} → {result}")

    def test_example_3_all_same_numbers(self):
        """Test Case 3: All elements are the same (edge case)"""
        nums = [3, 3, 3, 3, 3]
        expected = 3
        result = self.solution.findDuplicate(nums)
        self.assertEqual(result, expected)
        print(f"✓ Test 3 passed: {nums} → {result}")


if __name__ == "__main__":
    print("=" * 50)
    print("Testing Find the Duplicate Number")
    print("=" * 50)
    unittest.main(verbosity=2)

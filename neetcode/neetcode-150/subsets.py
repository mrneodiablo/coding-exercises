"""
Docstring for neetcode.neetcode-150.subsets
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(index, current_subset: List):
            if index == len(nums):
                ans.append(current_subset.copy())
                return

            current_subset.append(nums[index])
            dfs(index + 1, current_subset)

            current_subset.pop()
            dfs(index + 1, current_subset)

        dfs(0, [])
        return ans


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with array [1,2,3]"""
        nums = [1, 2, 3]
        result = self.solution.subsets(nums)
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        # Sort both lists of lists for comparison
        result_sorted = [sorted(subset) for subset in result]
        expected_sorted = [sorted(subset) for subset in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_example_2(self):
        """Test with single element [0]"""
        nums = [0]
        result = self.solution.subsets(nums)
        expected = [[], [0]]
        result_sorted = [sorted(subset) for subset in result]
        expected_sorted = [sorted(subset) for subset in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        result = self.solution.subsets(nums)
        expected = [[]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

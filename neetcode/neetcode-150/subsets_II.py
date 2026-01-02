"""
Docstring for neetcode.neetcode-150.subsets_II
90. Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List
import unittest


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort array in advance
        nums.sort()
        ans = []
        seen = set()  # use set and tuple for comparation in the future

        def dfs(index: int, subset: list):
            if index == len(nums):
                # Convert to tuple to hashable
                subset_tuple = tuple(subset)
                if subset_tuple not in seen:
                    seen.add(subset_tuple)
                    ans.append(subset)
                return

            # Include current element + [nums[index]]
            dfs(index + 1, subset + [nums[index]])

            dfs(index + 1, subset.copy())

        dfs(0, [])
        return ans


class TestSubsetsWithDup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with duplicates: [1,2,2]"""
        nums = [1, 2, 2]
        result = self.solution.subsetsWithDup(nums)
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        # Sort both result and expected for comparison since order doesn't matter
        result_sorted = [sorted(subset) for subset in result]
        expected_sorted = [sorted(subset) for subset in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_example_2(self):
        """Test with single element: [0]"""
        nums = [0]
        result = self.solution.subsetsWithDup(nums)
        expected = [[], [0]]
        result_sorted = [sorted(subset) for subset in result]
        expected_sorted = [sorted(subset) for subset in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_multiple_duplicates(self):
        """Test with multiple duplicates: [4,4,4,1,4]"""
        nums = [4, 4, 4, 1, 4]
        result = self.solution.subsetsWithDup(nums)
        # Check that there are no duplicate subsets
        result_as_tuples = [tuple(sorted(subset)) for subset in result]
        self.assertEqual(
            len(result_as_tuples),
            len(set(result_as_tuples)),
            "Result contains duplicate subsets",
        )
        # Check that empty subset and full set are included
        self.assertIn([], result)
        self.assertTrue(any(sorted(subset) == [1, 4, 4, 4, 4] for subset in result))


if __name__ == "__main__":
    unittest.main(verbosity=2)

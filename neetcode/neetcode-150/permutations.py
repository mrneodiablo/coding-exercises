"""
Docstring for neetcode.neetcode-150.permutations

Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

from typing import List
import unittest


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lenth_nums = len(nums)

        def dfs(combinition: list = [], remaining_nums: list = []):

            if len(combinition) == lenth_nums:
                ans.append(combinition.copy())
                return

            for i in range(len(remaining_nums)):
                new_combinition = combinition + [remaining_nums[i]]
                new_remaining_nums = remaining_nums[:i] + remaining_nums[i + 1:]
                dfs(new_combinition, new_remaining_nums)

            return

        dfs([], nums.copy())

        return ans


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with array [1,2,3]"""
        nums = [1, 2, 3]
        result = self.solution.permute(nums)
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
        # Sort both lists of lists for comparison
        self.assertEqual(len(result), len(expected))
        self.assertEqual(
            sorted([tuple(p) for p in result]), sorted([tuple(p) for p in expected])
        )

    def test_example_2(self):
        """Test with two elements [0,1]"""
        nums = [0, 1]
        result = self.solution.permute(nums)
        expected = [[0, 1], [1, 0]]
        self.assertEqual(len(result), len(expected))
        self.assertEqual(
            sorted([tuple(p) for p in result]), sorted([tuple(p) for p in expected])
        )

    def test_example_3(self):
        """Test with single element [1]"""
        nums = [1]
        result = self.solution.permute(nums)
        expected = [[1]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=3)

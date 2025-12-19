"""
Docstring for neetcode.neetcode-150.jump_game
55. Jump Game
Medium
Topics
premium lock icon
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List
import unittest


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


class TestFunctions(unittest.TestCase):
    def test_case_1_can_jump(self):
        """Test case where it is possible to reach the last index"""
        solution = Solution()
        nums = [2, 3, 1, 1, 4]
        expect = True
        self.assertEqual(
            solution.canJump(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_cannot_jump(self):
        """Test case where it is impossible to reach the last index"""
        solution = Solution()
        nums = [3, 2, 1, 0, 4]
        expect = False
        self.assertEqual(
            solution.canJump(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_single_element(self):
        """Test case with only one element (already at the end)"""
        solution = Solution()
        nums = [0]
        expect = True
        self.assertEqual(
            solution.canJump(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_4_large_gap(self):
        """Test case with a large gap that cannot be crossed"""
        solution = Solution()
        nums = [1, 2, 0, 0, 0, 0, 1]
        expect = False
        self.assertEqual(
            solution.canJump(nums),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_5_large_gap(self):
        """Test case with a large gap that cannot be crossed"""
        solution = Solution()
        nums = [0, 1]
        expect = False
        self.assertEqual(
            solution.canJump(nums),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

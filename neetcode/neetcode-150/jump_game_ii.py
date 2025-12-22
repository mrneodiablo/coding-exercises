"""
45. Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

"""

from typing import List
import unittest


class Solution:
    def jump(self, nums: List[int]) -> int:

        # backward greedy
        # jumps = 0
        # lenth_nums = len(nums)

        # if lenth_nums <= 1:
        #     return jumps

        # i = lenth_nums - 1
        # while i > 0:
        #     j = i - 1
        #     farthest = 0
        #     while j > -1:
        #         if i - j <= nums[j]:
        #             farthest = max(farthest, i - j)
        #         j -= 1

        #     if farthest != 0:
        #         i = i - farthest
        #         jumps += 1
        #     else:
        #         return jumps

        # return jumps

        # forward greedy
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early exit if we can reach the end
                if current_end >= len(nums) - 1:
                    break

        return jumps


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with first example from problem"""
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_example_2(self):
        """Test with second example from problem"""
        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_single_element(self):
        """Test with single element (already at target)"""
        nums = [0]
        self.assertEqual(self.solution.jump(nums), 0)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

"""
84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

import unittest
from typing import List


class Solution:
    def largestRectangleAreaBruteForce(self, heights: List[int]) -> int:

        lartest_area = 0

        for i in range(len(heights)):
            min_as = heights[i]
            for j in range(i, len(heights)):
                min_as = min(min_as, heights[j])
                lartest_area = max(lartest_area, min_as * (j + 1 - i))

        return lartest_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        max_area = 0
        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                _, height = stack.pop()
                left = stack[-1][0] if stack else -1
                right = i
                max_area = max(max_area, height * (right - left - 1))
            stack.append((i, h))

        while stack:
            _, height = stack.pop()
            left = stack[-1][0] if stack else -1
            max_area = max(max_area, height * (len(heights) - left - 1))

        return max_area


class TestLargestRectangleArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # bars [2,1,5,6,2,3] → largest rectangle = 5×2 = 10
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)

    def test_example2(self):
        # bars [2,4] → largest rectangle = 2×2 = 4
        self.assertEqual(self.solution.largestRectangleArea([2, 4]), 4)

    def test_single_bar(self):
        # only 1 bar → area = height × width = 5×1 = 5
        self.assertEqual(self.solution.largestRectangleArea([5]), 5)

    def test_descending(self):
        # [5,4,3,2,1] → largest is 3×3=9 (bars at index 0,1,2 with min height 3)
        self.assertEqual(self.solution.largestRectangleArea([5, 4, 3, 2, 1]), 9)


if __name__ == "__main__":
    unittest.main(verbosity=2)

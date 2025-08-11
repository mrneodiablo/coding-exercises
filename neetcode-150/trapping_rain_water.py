"""
Given n non-negative integers representing
an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.


Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is
represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1:
        # Two-pointer (your solution - optimal but harder to understand)
        # return self.trap_two_pointer(height)

        # Approach 2: Pre-compute left and
        # right max arrays (easier to understand)
        return self.trap_precompute(height)

    def trap_two_pointer(self, height: List[int]) -> int:
        """Your original solution - O(1) space, O(n) time"""
        if len(height) <= 2:
            return 0

        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        result = 0
        while left < right:
            if max_left < max_right:  # Fixed comparison
                left += 1
                max_left = max(max_left, height[left])
                result += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                result += max_right - height[right]
        return result

    def trap_precompute(self, height: List[int]) -> int:
        """
        Easier to understand approach:
        1. For each position, water level = min(max_left, max_right)
        2. Water trapped = max(0, water_level - height[i])

        Time: O(n), Space: O(n)
        """
        if len(height) <= 2:
            return 0

        n = len(height)

        # Step 1: Pre-compute max height to the left of each position
        max_left = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])

        # Step 2: Pre-compute max height to the right of each position
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])

        # Step 3: Calculate trapped water at each position
        total_water = 0
        for i in range(n):
            # Water level at position i is limited by the smaller wall
            water_level = min(max_left[i], max_right[i])
            # Water trapped = water_level - ground_level (but not negative)
            water_trapped = max(0, water_level - height[i])
            total_water += water_trapped

        return total_water


def test_trap():
    solution = Solution()

    # Test case 1: Simple example

    # Test case 2: Example from problem description
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print("Test 2 passed: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6")

    # # Test case 3: Second example from problem description
    # assert solution.trap([4, 2, 0, 3, 2, 5]) == 9
    # print("Test 3 passed: [4,2,0,3,2,5] -> 9")

    # # Test case 4: No water can be trapped (ascending)
    # assert solution.trap([1, 2, 3, 4, 5]) == 0
    # print("Test 4 passed: [1,2,3,4,5] -> 0")

    # # Test case 5: Simple valley
    # assert solution.trap([3, 0, 2]) == 2
    # print("Test 5 passed: [3,0,2] -> 2")

    # # Test case 6: Edge cases - empty and single element
    # assert solution.trap([]) == 0
    # assert solution.trap([5]) == 0
    # print("Test 6 passed: [] -> 0, [5] -> 0")

    # print("All test cases passed!")


if __name__ == "__main__":
    test_trap()

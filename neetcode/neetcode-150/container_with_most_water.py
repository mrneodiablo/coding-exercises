"""
You are given an integer array height of length n.
There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines
are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section)
the container can contain is 49.

"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # loop ping 2 loop got timeout
        # max_result = 0
        # if len(height) <= 1:
        #     return max_result

        # for i in range(len(height)-1):
        #     for j in range(i+1,len(height)):
        #         max_result = max(
        # max_result,
        # (j-i)*min(height[j],height[i])
        # )
        # return max_result

        # try to use 2 pointer
        max_result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            max_result = max(
                max_result, (right - left) * min(height[right], height[left])
            )
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_result


if __name__ == "__main__":
    solution = Solution()
    height_test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height_test))

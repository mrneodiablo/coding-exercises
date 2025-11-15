"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that
cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval

        merged.append(prev)

        return merged


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiple overlapping intervals
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = solution.merge(intervals1)
    print(f"Test 1: intervals={intervals1}")
    print(f"Result: {result1}")
    print("Expected: [[1, 6], [8, 10], [15, 18]]")
    print()

    # Test case 2: Adjacent intervals that touch (should merge)
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    print(f"Test 2: intervals={intervals2}")
    print(f"Result: {result2}")
    print("Expected: [[1, 5]]")
    print()

    # Test case 3: Unsorted intervals with complete overlap
    intervals3 = [[1, 4], [0, 2], [3, 5]]
    result3 = solution.merge(intervals3)
    print(f"Test 3: intervals={intervals3}")
    print(f"Result: {result3}")
    print("Expected: [[0, 5]]")
    print()

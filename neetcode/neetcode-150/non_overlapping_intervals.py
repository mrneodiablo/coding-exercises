"""
Docstring for neetcode-150.non_overlapping_intervals
Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping.
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and
    the rest of the intervals are non-overlapping.


    [[1,2],[1,3],[2,3],[3,4]]

Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2]
    to make the rest of the intervals non-overlapping.

Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any
    of the intervals since they're already non-overlapping.

"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if len(intervals) <= 1:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])
        previous = intervals[0]
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < previous[1]:
                ans += 1
            else:
                previous = intervals[i]
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiple overlapping intervals
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    result1 = solution.eraseOverlapIntervals(intervals1)
    print("Test 1:")
    print(f"Input:  {intervals1}")
    print(f"Output: {result1}")
    print("Expected: 1")
    print("Explanation: Remove [1,3] to make all intervals non-overlapping")
    print()

    # Test case 2: All intervals identical (maximum overlaps)
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    result2 = solution.eraseOverlapIntervals(intervals2)
    print("Test 2:")
    print(f"Input:  {intervals2}")
    print(f"Output: {result2}")
    print("Expected: 2")
    print("Explanation: Keep one [1,2], remove the other two")
    print()

    # Test case 3: No overlapping intervals
    intervals3 = [[1, 2], [2, 3]]
    result3 = solution.eraseOverlapIntervals(intervals3)
    print("Test 3:")
    print(f"Input:  {intervals3}")
    print(f"Output: {result3}")
    print("Expected: 0")
    print("Explanation: Already non-overlapping (touching at point 2 is OK)")
    print()

    # Test case 4: Chain of overlapping intervals
    intervals4 = [[1, 100], [11, 22], [1, 11], [2, 12]]
    result4 = solution.eraseOverlapIntervals(intervals4)
    print("Test 4:")
    print(f"Input:  {intervals4}")
    print(f"Output: {result4}")
    print("Expected: 2")
    print("Explanation: Remove [1,100] and [2,12], keep [1,11] and [11,22]")
    print()

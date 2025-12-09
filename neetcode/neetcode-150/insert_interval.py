"""
57. Insert Interval
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and
the end of the ith interval and intervals is
sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that
intervals is still sorted in ascending order by
starti and intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place.
You can make a new array and return it.



Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        for interval in intervals:
            # newInterval comes before interval (no overlap)
            # [ newInterval ]
            #                   [ interval ]
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval

            # interval comes before newInterval (no overlap)
            #                    [ newInterval ]
            #      [ interval ]
            elif interval[1] < newInterval[0]:
                ans.append(interval)

            # There's overlap, merge them
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        # Don't forget to append the final newInterval
        ans.append(newInterval)
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: newInterval non-overlaps with one interval
    intervals1 = [[6, 9]]
    newInterval1 = [2, 5]
    result1 = solution.insert(intervals1, newInterval1)
    print("Test 1:")
    print(f"Input:  intervals = {intervals1}, newInterval = {newInterval1}")
    print(f"Output: {result1}")
    print("Expected: [[2, 5], [6, 9]]")
    print()

    # Test case 2: newInterval non-overlaps with one interval
    intervals2 = [[6, 9]]
    newInterval2 = [10, 11]
    result2 = solution.insert(intervals2, newInterval2)
    print("Test 2:")
    print(f"Input:  intervals = {intervals2}, newInterval = {newInterval2}")
    print(f"Output: {result2}")
    print("Expected: [[6, 9], [10, 11]]")
    print()

    # Test case 3: newInterval non-overlaps with one interval
    intervals3 = [[6, 9]]
    newInterval3 = [4, 7]
    result3 = solution.insert(intervals3, newInterval3)
    print("Test 2:")
    print(f"Input:  intervals = {newInterval3}, newInterval = {newInterval3}")
    print(f"Output: {result3}")
    print("Expected: [[4, 9]")
    print()

    # Test case 3: newInterval non-overlaps with one interval
    intervals3 = [[6, 9]]
    newInterval3 = [9, 11]
    result3 = solution.insert(intervals3, newInterval3)
    print("Test 2:")
    print(f"Input:  intervals = {newInterval3}, newInterval = {newInterval3}")
    print(f"Output: {result3}")
    print("Expected: [[6, 11]")
    print()

    # Test case 3: newInterval non-overlaps with one interval
    intervals3 = [[6, 9]]
    newInterval3 = [4, 11]
    result3 = solution.insert(intervals3, newInterval3)
    print("Test 2:")
    print(f"Input:  intervals = {newInterval3}, newInterval = {newInterval3}")
    print(f"Output: {result3}")
    print("Expected: [[4, 11]")
    print()

    # Test case 1: newInterval overlaps with one interval
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    result1 = solution.insert(intervals1, newInterval1)
    print("Test 1:")
    print(f"Input:  intervals = {intervals1}, newInterval = {newInterval1}")
    print(f"Output: {result1}")
    print("Expected: [[1, 5], [6, 9]]")
    print("Explanation: [2,5] overlaps with [1,3], merge to [1,5]")
    print()

    # Test case 2: newInterval overlaps with multiple intervals
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    result2 = solution.insert(intervals2, newInterval2)
    print("Test 2:")
    print(f"Input:  intervals = {intervals2}, newInterval = {newInterval2}")
    print(f"Output: {result2}")
    print("Expected: [[1, 2], [3, 10], [12, 16]]")
    print("Exp: [4,8] overlaps with [3,5],[6,7],[8,10], merge to [3,10]")
    print()

    # Test case 3: newInterval doesn't overlap, insert at beginning
    intervals3 = [[5, 7], [8, 9]]
    newInterval3 = [1, 2]
    result3 = solution.insert(intervals3, newInterval3)
    print("Test 3:")
    print(f"Input:  intervals = {intervals3}, newInterval = {newInterval3}")
    print(f"Output: {result3}")
    print("Expected: [[1, 2], [5, 7], [8, 9]]")
    print("Explanation: [1,2] doesn't overlap, insert at beginning")
    print()

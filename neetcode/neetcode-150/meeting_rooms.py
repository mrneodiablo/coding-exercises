"""
Meeting Rooms Problem
Given an array of meeting time interval objects consisting
of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
determine if a person could add
all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        previous = intervals[0]
        for interval in intervals[1:]:
            if interval.start < previous.end:
                return False
            previous = interval

        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Overlapping meetings - should return False
    intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    result1 = solution.canAttendMeetings(intervals1)
    print("Test 1:")
    print("Input:  [(0,30), (5,10), (15,20)]")
    print(f"Output: {result1}")
    print("Expected: False")
    print("Explanation: (0,30) overlaps with (5,10) and (15,20)")
    print()

    # Test case 2: No overlapping meetings - should return True
    intervals2 = [Interval(5, 8), Interval(9, 15)]
    result2 = solution.canAttendMeetings(intervals2)
    print("Test 2:")
    print("Input:  [(5,8), (9,15)]")
    print(f"Output: {result2}")
    print("Expected: True")
    print("Explanation: No overlaps, can attend all meetings")
    print()

    # Test case 3: Adjacent meetings (touching at boundary)
    # should return True
    intervals3 = [Interval(0, 8), Interval(8, 10)]
    result3 = solution.canAttendMeetings(intervals3)
    print("Test 3:")
    print("Input:  [(0,8), (8,10)]")
    print(f"Output: {result3}")
    print("Expected: True")
    print("Explanation: (0,8) and (8,10) touch at 8 but don't overlap")
    print()

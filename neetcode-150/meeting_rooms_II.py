"""
Docstring for neetcode-150.meeting_rooms_II
Given an array of meeting time interval objects consisting
of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
find the minimum number of days required to schedule
all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

from typing import List
import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time - REQUIRED!
        intervals.sort(key=lambda x: x.start)

        # Min heap to track end times of meetings in use
        heap = []
        heapq.heappush(heap, intervals[0].end)

        # If earliest ending meeting finished, reuse that room
        for i in range(1, len(intervals)):

            if intervals[i].start >= heap[0]:
                heapq.heappop(heap)

            # Add current meeting's end time
            heapq.heappush(heap, intervals[i].end)

        return len(heap)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiple overlapping meetings - needs 2 rooms
    intervals1 = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    result1 = solution.minMeetingRooms(intervals1)
    print("Test 1:")
    print("Input:  [(0,40), (5,10), (15,20)]")
    print(f"Output: {result1}")
    print("Expected: 2")
    print(
        "Explanation: (0,40) conflicts with"
        "both (5,10) and (15,20), so need 2 rooms"
    )
    print()

    # Test case 2: All meetings overlap at same time - needs 3 rooms
    intervals2 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    result2 = solution.minMeetingRooms(intervals2)
    print("Test 2:")
    print("Input:  [(0,30), (5,10), (15,20)]")
    print(f"Output: {result2}")
    print("Expected: 2")
    print("Explanation: All 3 meetings overlap,"
          "maximum 2 concurrent at any point")
    print()

    # Test case 3: Adjacent meetings (no overlap) - needs 1 room
    intervals3 = [Interval(0, 8), Interval(8, 10), Interval(10, 15)]
    result3 = solution.minMeetingRooms(intervals3)
    print("Test 3:")
    print("Input:  [(0,8), (8,10), (10,15)]")
    print(f"Output: {result3}")
    print("Expected: 1")
    print(
        "Explanation: All meetings are"
        "back-to-back with no overlap, only need 1 room"
    )
    print()

    # Test case 3: Adjacent meetings (no overlap) - needs 1 room
    intervals4 = [
        Interval(5, 10),
        Interval(0, 40),
        Interval(15, 20),
        Interval(3, 20)
    ]
    result4 = solution.minMeetingRooms(intervals4)
    print("Test 4:")
    print("Input:  [(5, 10), (0, 40), (15, 20), (3, 20)]")
    print(f"Output: {result4}")
    print("Expected: 3")
    print(
        "Explanation: All meetings are"
        "back-to-back with no overlap, only need 1 room"
    )
    print()

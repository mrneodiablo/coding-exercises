"""
Docstring for neetcode.neetcode-150.minimum_interval_to_include_each_query
Minimum Interval to Include Each Query

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.



Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
"""

from typing import List
import heapq
import unittest


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # Sort intervals by left
        intervals.sort()

        # Sort queries but keep original index
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        ans = [-1] * len(queries)
        min_heap = []  # (size, right)

        i = 0
        for idx, q in sorted_queries:
            # Add intervals where left <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # Remove intervals where right < q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # Get smallest valid interval
            if min_heap:
                ans[idx] = min_heap[0][0]

        return ans


class TestFunctions(unittest.TestCase):

    def test_case_1_multiple_intervals(self):
        """Test case with multiple overlapping intervals"""
        solution = Solution()
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        expect = [3, 3, 1, 4]
        self.assertEqual(
            solution.minInterval(intervals, queries),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_query_not_in_any_interval(self):
        """Test case where some queries are not in any interval"""
        solution = Solution()
        intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
        queries = [2, 19, 5, 22]
        expect = [2, -1, 4, 6]
        self.assertEqual(
            solution.minInterval(intervals, queries),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_single_interval(self):
        """Test case with single interval and single query"""
        solution = Solution()
        intervals = [[1, 10]]
        queries = [5]
        expect = [10]
        self.assertEqual(
            solution.minInterval(intervals, queries),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

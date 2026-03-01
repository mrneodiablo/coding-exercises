"""
207. Course Schedule

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict, deque
import unittest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 0 not start
        # 1 visting
        # 2 visted
        state = [0] * numCourses

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(course: int) -> bool:
            if state[course] == 1:  # cycle deteted
                return False

            if state[course] == 2:  # course already processed, safe
                return True

            state[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        queue = deque(q for q in range(numCourses) if in_degree[q] == 0)

        finish = 0
        while queue:
            course = queue.popleft()
            finish += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return finish == numCourses


class TestCanFinish(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_no_cycle(self):
        # Example 1: linear dependency, should be possible
        self.assertTrue(self.solution.canFinish(2, [[1, 0]]))

    def test_simple_no_cycle_2(self):
        # Example 1: linear dependency, should be possible
        self.assertTrue(self.solution.canFinish(2, [[0, 1]]))

    def test_simple_cycle(self):
        # Example 2: cycle between course 0 and 1, impossible
        self.assertFalse(self.solution.canFinish(2, [[1, 0], [0, 1]]))

    def test_no_prerequisites(self):
        # No prerequisites at all, always possible
        self.assertTrue(self.solution.canFinish(5, []))

    def test_longer_cycle(self):
        # Cycle: 0 -> 1 -> 2 -> 0, impossible
        self.assertFalse(self.solution.canFinish(3, [[1, 0], [2, 1], [0, 2]]))

    def test_complicated(self):
        self.assertFalse(
            self.solution.canFinish(
                20,
                [
                    [0, 10],
                    [3, 18],
                    [5, 5],
                    [6, 11],
                    [11, 14],
                    [13, 1],
                    [15, 1],
                    [17, 4],
                ],
            )
        )

    # --- BFS tests ---
    def test_bfs_simple_no_cycle(self):
        self.assertTrue(self.solution.canFinishBFS(2, [[1, 0]]))

    def test_bfs_simple_no_cycle_2(self):
        self.assertTrue(self.solution.canFinishBFS(2, [[0, 1]]))

    def test_bfs_simple_cycle(self):
        self.assertFalse(self.solution.canFinishBFS(2, [[1, 0], [0, 1]]))

    def test_bfs_no_prerequisites(self):
        self.assertTrue(self.solution.canFinishBFS(5, []))

    def test_bfs_longer_cycle(self):
        self.assertFalse(self.solution.canFinishBFS(3, [[1, 0], [2, 1], [0, 2]]))

    def test_bfs_complicated(self):
        self.assertFalse(
            self.solution.canFinishBFS(
                20,
                [
                    [0, 10],
                    [3, 18],
                    [5, 5],
                    [6, 11],
                    [11, 14],
                    [13, 1],
                    [15, 1],
                    [17, 4],
                ],
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

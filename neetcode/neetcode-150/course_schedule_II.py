"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

from collections import defaultdict, deque
import unittest
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []

        graph = defaultdict(list)
        state = [0] * numCourses  # 1 in processing, 2 finish

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(course: int) -> bool:

            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            ans.append(course)

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return ans

    def findOrderTopologysort(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        ans = []

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        queue = deque(course for course in range(numCourses) if in_degree[course] == 0)

        while queue:
            course = queue.popleft()
            ans.append(course)
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return ans if len(ans) == numCourses else []


class TestFindOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _is_valid_order(
        self, order: List[int], numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        """Helper to check if the returned order satisfies all prerequisites."""
        if len(order) != numCourses:
            return False
        if sorted(order) != list(range(numCourses)):
            return False
        position = {course: i for i, course in enumerate(order)}
        return all(position[b] < position[a] for a, b in prerequisites)

    def test_single_prerequisite(self):
        """Example 1: simple linear dependency."""
        numCourses = 2
        prerequisites = [[1, 0]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))

    def test_multiple_prerequisites(self):
        """Example 2: diamond-shaped dependency graph."""
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertTrue(self._is_valid_order(result, numCourses, prerequisites))

    def test_no_prerequisites(self):
        """Example 3: single course with no prerequisites."""
        numCourses = 1
        prerequisites = []
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0])

    def test_cycle_returns_empty(self):
        """Cycle detected — should return an empty list."""
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        result = self.solution.findOrder(numCourses, prerequisites)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)

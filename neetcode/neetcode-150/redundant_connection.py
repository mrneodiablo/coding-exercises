"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

Example 1:
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

Example 2:
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

Constraints:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.
"""

from typing import List
import unittest


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        leader = list(range(n + 1))

        def find(x):
            while leader[x] != x:
                leader[x] = leader[leader[x]]  # compress
                x = leader[x]
            return leader[x]

        def union(x, y):
            lx, ly = find(x), find(y)
            if lx == ly:
                return False

            leader[ly] = lx
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


class TestRedundantConnection(unittest.TestCase):

    def test_example_1(self):
        edges = [[1, 2], [1, 3], [2, 3]]
        result = Solution().findRedundantConnection(edges)
        self.assertEqual(result, [2, 3])

    def test_example_2(self):
        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        result = Solution().findRedundantConnection(edges)
        self.assertEqual(result, [1, 4])

    def test_return_last_edge_if_multiple_answers(self):
        # [1,2] và [2,3] đều có thể remove
        # nhưng phải return edge xuất hiện cuối cùng → [2,3]
        edges = [[1, 2], [2, 3], [1, 3]]
        result = Solution().findRedundantConnection(edges)
        self.assertEqual(result, [1, 3])

    def test_larger_graph(self):
        edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]
        result = Solution().findRedundantConnection(edges)
        self.assertEqual(result, [5, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)

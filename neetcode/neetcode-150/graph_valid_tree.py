"""
Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input:
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
    true

Example 2:
Input:
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output:
    false
Note:

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

from typing import List
import unittest
from collections import defaultdict
from collections import deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # graph structure: {node: [list of neighbors]}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected graph

        visited = set()
        queue = deque()

        for node in range(n):
            if node not in visited:
                queue.append(node)
                visited.add(node)

                while queue:
                    current = queue.popleft()
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)

        # Check all nodes were visited (connected graph)
        return len(visited) == n

    def validTreeDFS(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # graph structure: {node: [list of neighbors]}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected graph

        visited = set()

        def DFS(node, prev):

            # cycle detected
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == prev:
                    continue  # skip the edge we came from (undirected)
                if not DFS(neighbor, node):
                    return False
            return True

        # Start DFS from node 0, check no cycle
        if not DFS(0, -1):
            return False

        # Check all nodes were visited (connected graph)
        return len(visited) == n


class TestGraphValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_tree(self):
        # 5 nodes, 4 edges forming a valid tree (connected, no cycle)
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        self.assertTrue(self.solution.validTree(n, edges))

    def test_invalid_tree_with_cycle(self):
        # 5 nodes, 5 edges — contains a cycle, so NOT a valid tree
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        self.assertFalse(self.solution.validTree(n, edges))

    def test_disconnected_graph(self):
        # 4 nodes, 2 edges — graph is not fully connected, so NOT a valid tree
        n = 4
        edges = [[0, 1], [2, 3]]
        self.assertFalse(self.solution.validTree(n, edges))


if __name__ == "__main__":
    unittest.main(verbosity=2)

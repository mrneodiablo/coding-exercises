"""
Docstring for neetcode.neetcode-150.number_of_connected_components_in_an_undirected_graph
Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

Example 1:
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1
Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.

"""

from typing import List
from collections import defaultdict
from collections import deque
import unittest


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list (graph) - O(E)
        # lookup neighbor takes only O(1)
        # graph structure: {node: [list of neighbors]}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected graph

        visited = set()  # Use set for O(1) lookup instead of list O(n)
        components = 0
        queue = deque()

        # Check each node
        for node in range(n):
            if node not in visited:
                # BFS using queue
                queue.append(node)
                visited.add(node)

                while queue:
                    current = queue.popleft()  # Remove from front (FIFO for BFS)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                components += 1

        return components

    def countComponentsWithDFS(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list (graph) - O(E)
        # lookup neighbor takes only O(1)
        # graph structure: {node: [list of neighbors]}
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)  # undirected graph

        visited = set()  # Use set for O(1) lookup instead of list O(n)
        components = 0

        def dfs(node):
            """Visit all nodes in the current component"""
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Check each node
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components


class TestCountComponents(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.solution = Solution()

    def test_example_1_two_components(self):
        """Test with two separate components"""
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        self.assertEqual(self.solution.countComponents(n, edges), 2)

    def test_example_2_single_component(self):
        """Test with all nodes connected in one component"""
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_no_edges_all_isolated(self):
        """Test with no edges - each node is its own component"""
        n = 5
        edges = []
        self.assertEqual(self.solution.countComponents(n, edges), 5)

    def test_single_node(self):
        """Test with only one node and no edges"""
        n = 1
        edges = []
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_two_nodes_connected(self):
        """Test with two nodes connected"""
        n = 2
        edges = [[0, 1]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_two_nodes_disconnected(self):
        """Test with two nodes not connected"""
        n = 2
        edges = []
        self.assertEqual(self.solution.countComponents(n, edges), 2)

    def test_three_components(self):
        """Test with three separate components"""
        n = 7
        edges = [[0, 1], [2, 3], [4, 5], [5, 6]]
        # Components: {0,1}, {2,3}, {4,5,6}
        self.assertEqual(self.solution.countComponents(n, edges), 3)

    def test_star_graph(self):
        """Test with star-shaped graph (one center connected to all others)"""
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [0, 4]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)

    def test_complex_graph_multiple_components(self):
        """Test with complex graph having multiple components"""
        n = 10
        edges = [[0, 1], [1, 2], [2, 0], [3, 4], [5, 6], [6, 7], [8, 9]]
        # Components: {0,1,2}, {3,4}, {5,6,7}, {8,9}
        self.assertEqual(self.solution.countComponents(n, edges), 4)

    def test_fully_connected_graph(self):
        """Test with a fully connected small graph"""
        n = 4
        edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        self.assertEqual(self.solution.countComponents(n, edges), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

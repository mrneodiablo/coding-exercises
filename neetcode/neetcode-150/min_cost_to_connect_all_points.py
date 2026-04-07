"""
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
|xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

"""

import unittest
from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # implemement Kruskal's algorithm
        n = len(points)
        total_cost = 0
        # create a list of edges with their costs
        edges = {}

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i, j) not in edges and (j, i) not in edges:
                    cost = abs(points[i][0] - points[j][0]) + abs(
                        points[i][1] - points[j][1]
                    )
                    edges[(i, j)] = cost
        # sort edges by cost
        # [((B,C), 2), ((A,B), 5), ((A,C), 8)]
        sorted_edges = sorted(edges.items(), key=lambda x: x[1])

        # union-find data structure
        parent = list(range(n))

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find_root(x), find_root(y)
            if root_y != root_x:
                parent[root_y] = root_x
                return True
            return False

        for edge, cost in sorted_edges:
            if union(edge[0], edge[1]):
                total_cost += cost
        return total_cost

    def minCostConnectPointsPrim(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        visited = set()
        total_costs = 0

        # min heap is (cost , index point)
        min_heap = [(0, 0)]

        while min_heap:
            cost, index_point = heapq.heappop(min_heap)

            if index_point in visited:
                continue

            total_costs += cost
            visited.add(index_point)
            for next_point in range(len(points)):
                if next_point not in visited:
                    tmp_cost = abs(
                        points[index_point][0] - points[next_point][0]
                    ) + abs(points[index_point][1] - points[next_point][1])
                    heapq.heappush(min_heap, (tmp_cost, next_point))

        return total_costs


class TestMinCostConnectPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example from problem: expected output is 20
        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 20)

    def test_example2(self):
        # Example from problem: expected output is 18
        points = [[3, 12], [-2, 5], [-4, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 18)

    def test_single_point(self):
        # Only one point, no connections needed, cost is 0
        points = [[0, 0]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 0)

    def test_two_points(self):
        # Two points: manhattan distance = |0-1| + |0-1| = 2
        points = [[0, 0], [1, 1]]
        self.assertEqual(self.solution.minCostConnectPoints(points), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)

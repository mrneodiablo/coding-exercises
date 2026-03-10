"""
743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n.
You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

Example 2:
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1
Example 3:
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
onstraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from collections import defaultdict
from typing import List
import heapq
import unittest


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {i: float("inf") for i in range(1, n + 1)}
        dist[k] = 0

        for _ in range(n - 1):  # lặp n-1 lần
            for u, v, w in times:  # relax tất cả edges
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return -1 if float("inf") in dist.values() else max(dist.values())

    def networkDelayTimeDijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra algorithm
        dist = {}

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        heap = []
        heapq.heapify(heap)

        for i in range(1, n + 1):
            if i == k:
                dist[i] = 0
            else:
                dist[i] = float("inf")
        heapq.heappush(heap, (0, k))

        while heap:
            current_node = heapq.heappop(heap)
            weight = current_node[0]
            if weight > dist[current_node[1]]:
                continue

            for neighbor in graph[current_node[1]]:
                if neighbor[0] + weight < dist[neighbor[1]]:
                    dist[neighbor[1]] = neighbor[0] + weight
                    heapq.heappush(heap, (neighbor[0] + weight, neighbor[1]))

        return -1 if float("inf") in dist.values() else max(dist.values())


class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_basic_network(self):
        """Test basic network from example 1"""
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, 2)

    def test_case_2_simple_two_nodes(self):
        """Test simple two-node network"""
        times = [[1, 2, 1]]
        n = 2
        k = 1
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, 1)

    def test_case_3_unreachable_nodes(self):
        """Test when not all nodes can be reached"""
        times = [[1, 2, 1]]
        n = 2
        k = 2
        result = self.solution.networkDelayTime(times, n, k)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

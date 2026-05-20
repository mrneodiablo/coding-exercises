"""
Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""

import unittest
from typing import List
from collections import defaultdict


class Solution:
    def findItinerarA(self, tickets: List[List[str]]) -> List[str]:

        # write tree as disk
        # "departure" --> "arrival"
        graph = defaultdict(list)
        for d, a in sorted(tickets, reverse=True):
            graph[d].append(a)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_ap = graph[airport].pop()
                dfs(next_ap)
            result.append(airport)  # ← post-order

        dfs("JFK")
        return result[::-1]

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # write tree as disk
        # "departure" --> "arrival"
        graph = defaultdict(list)
        for d, a in sorted(tickets):
            graph[d].append(a)

        result = ["JFK"]

        # Test DFS + Backtracking
        def dfs(airpod) -> List[str]:

            if len(result) == len(tickets) + 1:
                return True

            for i, next_airpod in enumerate(graph[airpod]):
                graph[airpod].pop(i)
                result.append(next_airpod)
                if dfs(next_airpod):
                    return True

                graph[airpod].insert(i, next_airpod)
                result.pop()

            return False

        dfs("JFK")
        return result


class TestFindItinerary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        self.assertEqual(
            self.solution.findItinerary(tickets), ["JFK", "MUC", "LHR", "SFO", "SJC"]
        )

    def test_example2(self):
        # multiple valid paths, must return lexically smallest
        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        self.assertEqual(
            self.solution.findItinerary(tickets),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )

    def test_single_ticket(self):
        tickets = [["JFK", "LGA"]]
        self.assertEqual(self.solution.findItinerary(tickets), ["JFK", "LGA"])

    def test_lexical_order(self):
        # From JFK: ATL or SFO. Going SFO first gets stuck; ATL < SFO so must pick ATL
        tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "SFO"]]
        self.assertEqual(
            self.solution.findItinerary(tickets), ["JFK", "ATL", "JFK", "SFO"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

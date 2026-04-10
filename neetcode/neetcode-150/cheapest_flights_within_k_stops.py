"""
Cheapest Flights Within K Stops

There are n cities connected by some number of flights.
You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

"""

from typing import List
from collections import defaultdict
import unittest


class Solution:

    def findCheapestPriceBellmanFord(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices.copy()
            for frm, to, price in flights:
                if prices[frm] != float("inf"):
                    tmp[to] = min(tmp[to], prices[frm] + price)
            prices = tmp

        return prices[dst] if prices[dst] != float("inf") else -1

    # pylint: disable=unused-argument
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        flight_map = defaultdict(list)
        memory = {}

        for from_city, to_city, price in flights:
            flight_map[from_city].append((to_city, price))

        def dfsmemo(city, stop_remains):
            if city == dst:
                return 0

            if stop_remains < 0:
                return float("infinity")

            if (city, stop_remains) in memory:
                return memory[(city, stop_remains)]

            min_cost = float("infinity")

            for to_city, price in flight_map[city]:
                min_cost = min(min_cost, price + dfsmemo(to_city, stop_remains - 1))

            memory[(city, stop_remains)] = min_cost
            return min_cost

        def dfs(city, stops, cost, visited):
            if city == dst:
                return cost

            if stops > k:
                return float("infinity")

            if city in visited:
                return float("infinity")

            min_cost = float("infinity")

            for to_city, price in flight_map[city]:
                min_cost = min(
                    min_cost, dfs(to_city, stops + 1, cost + price, visited + [city])
                )

            return min_cost

        result = dfsmemo(src, k)  # dfs(src, 0, 0, [])
        return result if result != float("infinity") else -1


class TestFindCheapestPrice(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Optimal path: 0->1->3, cost = 100 + 600 = 700
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        self.assertEqual(self.solution.findCheapestPrice(n, flights, 0, 3, 1), 700)

    def test_example2(self):
        # Optimal path: 0->1->2, cost = 100 + 100 = 200
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        self.assertEqual(self.solution.findCheapestPrice(n, flights, 0, 2, 1), 200)

    def test_example3_no_stops(self):
        # k=0, only direct flight: 0->2, cost = 500
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        self.assertEqual(self.solution.findCheapestPrice(n, flights, 0, 2, 0), 500)

    def test_no_route(self):
        # No path from 0 to 3 within k=1 stops
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100]]
        self.assertEqual(self.solution.findCheapestPrice(n, flights, 0, 3, 1), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

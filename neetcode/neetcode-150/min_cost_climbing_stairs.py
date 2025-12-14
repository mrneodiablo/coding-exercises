"""
Docstring for neetcode.neetcode-150.min_cost_climbing_stairs
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

# how to recognize this problem as a dynamic programming problem
1: problem --> observer taht  it ask "min/max/count"
2: There are multiple options at each step
3: The result depends on sub-results
4: YES → 99% DP! 🎉
5: NO -> try Greedy/Two Pointers/Hash Map
"""

from typing import List
import unittest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] = min(dp[i-1], dp[i-2])
        # call dp[i] is min cost to reach place i

        # dp0 = 0 # Start from index 0 → FREE
        # dp1 = 0 # Start from index 1 → FREE
        # dp2 = min(dp[0]], dp[1])
        # dp3 = min(dp[1]], dp[2])
        # dp4 = min(dp[2]], dp[3])
        # dp(n) = min(dp[n-2]], dp[n-1])

        n = len(cost)

        # cache dp as array
        dp = [0] * (n + 1)

        # Base case: since we can start from step 0 or step 1 without cost
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            # Reach i from i-1: pay cost[i-1]
            # that means we get dp[i-1] and pay cost[i-1] staying at i-1
            from_prev = dp[i - 1] + cost[i - 1]

            # Reach i from i-2: pay cost[i-2]
            # that means we get dp[i-2] and pay cost[i-2] staying at i-2
            from_prev2 = dp[i - 2] + cost[i - 2]

            # Choose the cheaper way
            dp[i] = min(from_prev, from_prev2)

        # Return dp[n] b/c we want to reach the top which is after the last step
        return dp[n]


class TestFunctions(unittest.TestCase):

    def test_case_1_simple_stairs(self):
        """Test case with simple 3-step staircase"""
        solution = Solution()
        cost = [10, 15, 20]
        expect = 15
        self.assertEqual(
            solution.minCostClimbingStairs(cost),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_longer_stairs(self):
        """Test case with longer staircase requiring optimal path"""
        solution = Solution()
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expect = 6
        self.assertEqual(
            solution.minCostClimbingStairs(cost),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_two_steps(self):
        """Test case with minimum 2 steps"""
        solution = Solution()
        cost = [1, 2]
        expect = 1
        self.assertEqual(
            solution.minCostClimbingStairs(cost),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

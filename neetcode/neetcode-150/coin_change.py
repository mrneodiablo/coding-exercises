"""
Docstring for neetcode.neetcode-150.coin_change
322. Coin Change

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List
import unittest


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # this session dp is represent each dp[amount] = min number of coins can use
        # for example we coins = [1,2,5], amount = 11,
        # 11(amount)-5(coin value| amount 5)=6(amount), 6-5=1, 1-1=0
        # so dp[11] = dp[11-5] + 1
        #    dp[6]  = dp[6-5] + 1
        # .   dp[1]  = min(dp[1], dp[1-1] + 1)
        # so we have to find min number of coin of each amount ?

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # coin = 1
        # dp = [0, 1, 2, 3 ,4 ,5, 6, 7, 8, 8, 9, 10, 11]
        # coin = 2
        # dp = [0, 1, 1, 2 ,2 ,3, 3, 4, 4, 5, 5, 6, 6]
        # coin = 5
        # dp = [0, 1, 1, 2 ,2 ,1, 2, 3, 3, 4, 4, 5, 3]
        for coin_value in coins:
            for am in range(coin_value, amount + 1):
                dp[am] = min(dp[am], dp[am - coin_value] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.solution = Solution()

    def test_example_1_basic_case(self):
        """Test with coins [1,2,5] and amount 11"""
        coins = [1, 2, 5]
        amount = 11
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 3, "Expected 3 coins (5+5+1=11)")

    def test_example_2_impossible_case(self):
        """Test impossible case with coins [2] and amount 3"""
        coins = [2]
        amount = 3
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, -1, "Expected -1 as amount cannot be made")

    def test_example_3_zero_amount(self):
        """Test with amount 0"""
        coins = [1]
        amount = 0
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 0, "Expected 0 coins for amount 0")

    def test_larger_amount_multiple_coins(self):
        """Test with coins [1,3,4,5] and amount 7"""
        coins = [1, 3, 4, 5]
        amount = 7
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, 2, "Expected 2 coins (3+4=7)")


if __name__ == "__main__":
    unittest.main(verbosity=2)

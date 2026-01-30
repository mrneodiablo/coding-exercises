"""
Docstring for neetcode.neetcode-150.coin_change_II

You are given an integer array coins representing coins of different denominations and
an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""

from typing import List
import unittest


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(index_coin, remaining_amount):

            # base case
            if remaining_amount < 0 or index_coin >= len(coins):
                return 0

            if remaining_amount == 0:
                return 1

            if (index_coin, remaining_amount) in cache:
                return cache[(index_coin, remaining_amount)]

            count = 0

            # using current coint
            count += dfs(index_coin, remaining_amount - coins[index_coin])

            # Skip current coin using the next coins
            count += dfs(index_coin + 1, remaining_amount)

            cache[(index_coin, remaining_amount)] = count

            return count

        return dfs(0, amount)


class TestCoinChangeII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1_multiple_combinations(self):
        """Test case with multiple ways to make the amount"""
        amount = 5
        coins = [1, 2, 5]
        expected = 4
        result = self.solution.change(amount, coins)
        self.assertEqual(
            result,
            expected,
            f"Expected {expected} ways to make amount {amount} with coins {coins}",
        )

    # def test_example_2_impossible_amount(self):
    #     """Test case where amount cannot be made with given coins"""
    #     amount = 3
    #     coins = [2]
    #     expected = 0
    #     result = self.solution.change(amount, coins)
    #     self.assertEqual(result, expected,
    #                     f"Expected {expected} ways (impossible) to make amount {amount} with coins {coins}")

    # def test_example_3_exact_match(self):
    #     """Test case with exact coin match"""
    #     amount = 10
    #     coins = [10]
    #     expected = 1
    #     result = self.solution.change(amount, coins)
    #     self.assertEqual(result, expected,
    #                     f"Expected {expected} way to make amount {amount} with coins {coins}")


if __name__ == "__main__":
    unittest.main()

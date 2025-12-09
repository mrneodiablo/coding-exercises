"""
You are given an array prices where prices[i] is
the price of a given stock on the ith day.

You want to maximize your profit by choosing
a single day to buy one stock and choosing a different day
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and
sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1
is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Original O(n²) brute force approach
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     j = len(prices)-1
        #     while i < j:
        #         max_profit = max(max_profit, prices[j]-prices[i])
        #         j -= 1
        # return max_profit

        # Optimized O(n) approach (your current solution)
        # min_price = prices[0]
        # max_profit = 0
        # for i in range(len(prices)):
        #     min_price = min(min_price, prices[i])
        #     max_profit = max(max_profit, prices[i] - min_price)
        # return max_profit

        # Sliding Window Approach - Explicit implementation
        if len(prices) <= 1:
            return 0

        left = 0  # Buy pointer (start of window)
        right = 1  # Sell pointer (end of window)
        max_profit = 0

        while right < len(prices):
            # If current window is profitable
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                # Shrink window: move buy pointer to current position
                # because we found a better (lower) buy price
                left = right

            # Expand window: move sell pointer
            right += 1

        return max_profit


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic example from problem
    test1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(test1)
    print(f"Test 1: {test1} -> {result1} (Expected: 5)")

    # Test Case 2: Decreasing prices (no profit possible)
    test2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(test2)
    print(f"Test 2: {test2} -> {result2} (Expected: 0)")

    # Test Case 3: Single element
    test3 = [5]
    result3 = solution.maxProfit(test3)
    print(f"Test 3: {test3} -> {result3} (Expected: 0)")

    # Test Case 4: Two elements - profit possible
    test4 = [1, 5]
    result4 = solution.maxProfit(test4)
    print(f"Test 4: {test4} -> {result4} (Expected: 4)")

    # Test Case 5: Two elements - no profit
    test5 = [5, 1]
    result5 = solution.maxProfit(test5)
    print(f"Test 5: {test5} -> {result5} (Expected: 0)")

    # Test Case 6: Maximum profit at the end
    test6 = [1, 2, 3, 4, 5]
    result6 = solution.maxProfit(test6)
    print(f"Test 6: {test6} -> {result6} (Expected: 4)")

    # Test Case 7: Buy at minimum, sell at maximum
    test7 = [3, 2, 1, 4, 8, 2]
    result7 = solution.maxProfit(test7)
    print(f"Test 7: {test7} -> {result7} (Expected: 7)")

    # Test Case 8: All same prices
    test8 = [5, 5, 5, 5, 5]
    result8 = solution.maxProfit(test8)
    print(f"Test 8: {test8} -> {result8} (Expected: 0)")

    # Test Case 9: Large numbers
    test9 = [100, 200, 50, 300, 25, 400]
    result9 = solution.maxProfit(test9)
    print(f"Test 9: {test9} -> {result9} (Expected: 375)")

    # Test Case 10: Early peak then valley and recovery
    test10 = [10, 1, 2, 15, 5, 20]
    result10 = solution.maxProfit(test10)
    print(f"Test 10: {test10} -> {result10} (Expected: 19)")

    print("\n" + "=" * 50)
    print("Note: Your current solution has O(n²) complexity.")
    print("Consider optimizing to O(n) using single pass approach.")

"""
338. Counting Bits
Given an integer n, return an array ans of
length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.


Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Small number
    n1 = 2
    result1 = solution.countBits(n1)
    print(f"Test 1: n={n1}")
    print(f"Result: {result1}")
    print("Expected: [0, 1, 1]")
    print("Explanation: 0→0, 1→1, 2→10")
    print()

    # Test case 2: Medium number
    n2 = 5
    result2 = solution.countBits(n2)
    print(f"Test 2: n={n2}")
    print(f"Result: {result2}")
    print("Expected: [0, 1, 1, 2, 1, 2]")
    print("Explanation: 0→0, 1→1, 2→10, 3→11, 4→100, 5→101")
    print()

    # Test case 3: Larger number
    n3 = 8
    result3 = solution.countBits(n3)
    print(f"Test 3: n={n3}")
    print(f"Result: {result3}")
    print("Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1]")
    print()

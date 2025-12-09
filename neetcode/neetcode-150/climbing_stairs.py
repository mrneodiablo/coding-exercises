"""
Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
"""

import math
import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        for k in range(0, n // 2 + 1):
            # math.comb(a, b) tính tổ hợp C(a, b)
            total += math.comb(n - k, k)
        return total


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem description
        n = 2
        expected = 2  # Ways: (1+1), (2)
        result = self.solution.climbStairs(n)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Larger example
        n = 3
        expected = 3  # Ways: (1+1+1), (1+2), (2+1)
        result = self.solution.climbStairs(n)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: Single step
        n = 1
        expected = 1  # Only one way: (1)
        result = self.solution.climbStairs(n)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_climbing_stairs():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: n = 2 (example from problem)")
    n1 = 2
    expected1 = 2  # Ways: (1+1), (2)
    result1 = solution.climbStairs(n1)
    print(f"  Input: n = {n1}")
    print(f"  Expected: {expected1} ways: (1+1), (2)")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: n = 3")
    n2 = 3
    expected2 = 3  # Ways: (1+1+1), (1+2), (2+1)
    result2 = solution.climbStairs(n2)
    print(f"  Input: n = {n2}")
    print(f"  Expected: {expected2} ways: (1+1+1), (1+2), (2+1)")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: n = 1 (base case)")
    n3 = 1
    expected3 = 1  # Only one way: (1)
    result3 = solution.climbStairs(n3)
    print(f"  Input: n = {n3}")
    print(f"  Expected: {expected3} way: (1)")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: n = 4")
    n4 = 4
    expected4 = 5  # Ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
    result4 = solution.climbStairs(n4)
    print(f"  Input: n = {n4}")
    print(f"  Expected: {expected4} ways")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: n = 5")
    n5 = 5
    expected5 = 8
    result5 = solution.climbStairs(n5)
    print(f"  Input: n = {n5}")
    print(f"  Expected: {expected5} ways (Fibonacci sequence)")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClimbingStairs)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_climbing_stairs()

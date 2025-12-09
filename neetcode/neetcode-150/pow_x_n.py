"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Cách lặp - DỄ HIỂU NHẤT!
        # Ví dụ: 2^7 = 2 * (2^2) * (2^4)
        #        Chỉ lấy các số mũ tương ứng với bit 1 trong binary của 7

        # Xử lý số mũ âm
        if n < 0:
            x = 1 / x
            n = -n

        # Base case
        if n == 0:
            return 1.0

        result = 1.0

        # Ví dụ: 2^7
        # n=7: lẻ → result = 1 * 2 = 2,     x = 2*2 = 4,    n = 3
        # n=3: lẻ → result = 2 * 4 = 8,     x = 4*4 = 16,   n = 1
        # n=1: lẻ → result = 8 * 16 = 128,  x = 16*16,      n = 0
        # n=0: STOP → return 128

        while n > 0:
            # Nếu n lẻ: cần nhân thêm x vào kết quả
            if n % 2 == 1:
                result = result * x

            # Bình phương x cho vòng lặp tiếp theo
            x = x * x

            # Chia n cho 2
            n = n // 2

        return result


class TestPow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_positive_exponent(self):
        """Test case 1: Positive exponent from problem description"""
        x = 2.0
        n = 10
        expected = 1024.0
        result = self.solution.myPow(x, n)
        self.assertAlmostEqual(result, expected, places=5)

    def test_case_2_decimal_base(self):
        """Test case 2: Decimal base with small exponent"""
        x = 2.1
        n = 3
        expected = 9.261
        result = self.solution.myPow(x, n)
        self.assertAlmostEqual(result, expected, places=5)

    def test_case_3_negative_exponent(self):
        """Test case 3: Negative exponent"""
        x = 2.0
        n = -2
        expected = 0.25
        result = self.solution.myPow(x, n)
        self.assertAlmostEqual(result, expected, places=5)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("POW(X, N) - TEST CASES")
    print("=" * 50)

    # Test 1: Positive exponent
    print("Test 1: Positive exponent (2^10)")
    x1, n1 = 2.0, 10
    expected1 = 1024.0
    result1 = solution.myPow(x1, n1)
    print(f"  Input: x = {x1}, n = {n1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    passed1 = abs(result1 - expected1) < 0.00001
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Decimal base
    print("Test 2: Decimal base (2.1^3)")
    x2, n2 = 2.1, 3
    expected2 = 9.261
    result2 = solution.myPow(x2, n2)
    print(f"  Input: x = {x2}, n = {n2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    passed2 = abs(result2 - expected2) < 0.00001
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Negative exponent
    print("Test 3: Negative exponent (2^-2)")
    x3, n3 = 2.0, -2
    expected3 = 0.25
    result3 = solution.myPow(x3, n3)
    print(f"  Input: x = {x3}, n = {n3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print("  Explanation: 2^-2 = 1/(2^2) = 1/4 = 0.25")
    passed3 = abs(result3 - expected3) < 0.00001
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Zero exponent
    print("Test 4: Zero exponent (5^0)")
    x4, n4 = 5.0, 0
    expected4 = 1.0
    result4 = solution.myPow(x4, n4)
    print(f"  Input: x = {x4}, n = {n4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print("  Explanation: Any number^0 = 1")
    passed4 = abs(result4 - expected4) < 0.00001
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: Exponent of 1
    print("Test 5: Exponent of 1 (7.5^1)")
    x5, n5 = 7.5, 1
    expected5 = 7.5
    result5 = solution.myPow(x5, n5)
    print(f"  Input: x = {x5}, n = {n5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print("  Explanation: Any number^1 = itself")
    passed5 = abs(result5 - expected5) < 0.00001
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()

    s = Solution()
    s.myPow(2, 3)

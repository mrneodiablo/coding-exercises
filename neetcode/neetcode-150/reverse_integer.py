"""
7. Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed
32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

"""

import unittest


class Solution:
    def reverse(self, x: int) -> int:
        # Lưu dấu của số ban đầu
        sign = 1 if x >= 0 else -1

        # Làm việc với giá trị tuyệt đối
        x = abs(x)

        # Đảo ngược số
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10

        # Thêm dấu trở lại
        result *= sign

        # Kiểm tra overflow: [-2^31, 2^31 - 1]
        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result


class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_positive_number(self):
        """Test case 1: Positive number"""
        x = 123
        expected = 321
        result = self.solution.reverse(x)
        self.assertEqual(result, expected)

    def test_case_2_negative_number(self):
        """Test case 2: Negative number"""
        x = -123
        expected = -321
        result = self.solution.reverse(x)
        self.assertEqual(result, expected)

    def test_case_3_trailing_zeros(self):
        """Test case 3: Number with trailing zeros"""
        x = 120
        expected = 21
        result = self.solution.reverse(x)
        self.assertEqual(result, expected)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("REVERSE INTEGER - TEST CASES")
    print("=" * 50)

    # Test 1: Positive number
    print("Test 1: Positive number (123)")
    x1 = 123
    expected1 = 321
    result1 = solution.reverse(x1)
    print(f"  Input: {x1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    # Test 2: Negative number
    print("Test 2: Negative number (-123)")
    x2 = -123
    expected2 = -321
    result2 = solution.reverse(x2)
    print(f"  Input: {x2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    # Test 3: Trailing zeros
    print("Test 3: Number with trailing zeros (120)")
    x3 = 120
    expected3 = 21
    result3 = solution.reverse(x3)
    print(f"  Input: {x3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    # Test 4: Overflow case
    print("Test 4: Overflow case (1534236469)")
    x4 = 1534236469
    expected4 = 0  # Reversed would be 9646324351 > 2^31-1
    result4 = solution.reverse(x4)
    print(f"  Input: {x4}")
    print("  Reversed: 9646324351 (exceeds 2^31-1 = 2147483647)")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    # Test 5: Zero
    print("Test 5: Zero (0)")
    x5 = 0
    expected5 = 0
    result5 = solution.reverse(x5)
    print(f"  Input: {x5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()

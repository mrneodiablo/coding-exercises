"""
43. Multiply Strings
Solved
Medium
Topics
premium lock icon
Companies
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the
inputs to integer directly.


Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # convert num1
        int_num1 = 0
        for i1 in range(len(num1)):
            int_num1 += (ord(num1[len(num1) - i1 - 1]) - 48) * (10**i1)

        # convert num2
        int_num2 = 0
        for i2 in range(len(num2)):
            int_num2 += (ord(num2[len(num2) - 1 - i2]) - 48) * (10**i2)

        return str(int_num1 * int_num2)


def test_multiply_strings():
    """Test cases for the multiply strings function."""
    solution = Solution()

    # Test case 1: Basic multiplication from examples
    assert solution.multiply("2", "3") == "6"
    assert solution.multiply("123", "456") == "56088"

    # Test case 2: Edge cases with zero
    assert solution.multiply("0", "0") == "0"
    assert solution.multiply("0", "123") == "0"
    assert solution.multiply("456", "0") == "0"

    # Test case 3: Large numbers and single digits
    assert solution.multiply("999", "999") == "998001"
    assert solution.multiply("9", "9") == "81"
    assert solution.multiply("12345", "67890") == "838102050"

    print("All test cases passed!")


if __name__ == "__main__":
    test_multiply_strings()

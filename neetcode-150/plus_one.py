"""
66. Plus One
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in
left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""

from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
                break
        if carry == 1:
            digits = [1] + digits

        return digits


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_normal_increment(self):
        """Test case 1: Normal increment without carry propagation"""
        digits = [1, 2, 3]
        expected = [1, 2, 4]
        result = self.solution.plusOne(digits)
        self.assertEqual(result, expected)

    def test_case_2_carry_propagation(self):
        """Test case 2: Increment with carry propagation (all 9s)"""
        digits = [9, 9, 9]
        expected = [1, 0, 0, 0]
        result = self.solution.plusOne(digits)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

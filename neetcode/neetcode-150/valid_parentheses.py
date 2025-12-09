"""
Valid Parentheses
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true
"""

import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for open in s:
            if open in pair.values():
                stack.append(open)
            else:
                if len(stack) > 0:
                    if pair[open] == stack[-1]:
                        stack.pop()
                        continue
                    return False

                return False
        return len(stack) == 0


class TestFunctions(unittest.TestCase):

    def test_simple_valid(self):
        solution = Solution()
        self.assertEqual(solution.isValid("()"), True, "Simple valid parentheses")

    def test_multiple_types_valid(self):
        solution = Solution()
        self.assertEqual(solution.isValid("()[]{}"), True, "Multiple valid bracket types")

    def test_nested_valid(self):
        solution = Solution()
        self.assertEqual(solution.isValid("([{}])"), True, "Nested valid brackets")

    def test_invalid_wrong_order(self):
        solution = Solution()
        self.assertEqual(solution.isValid("([)]"), False, "Invalid wrong closing order")

    def test_invalid_unmatched(self):
        solution = Solution()
        self.assertEqual(solution.isValid("(("), False, "Invalid unmatched opening bracket")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

"""
Docstring for neetcode.neetcode-150.valid_parenthesis_string
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
"""

import unittest


class Solution:
    def checkValidStringWithDP(self, s: str) -> bool:
        # Using memoization to cache state already calculated
        # Key: (index, open_count), Value: True/False
        memo = {}

        def backtracking(index, open_count):
            # Base case:
            if index == len(s):
                return open_count == 0

            # if it calculated in priod step ,
            if (index, open_count) in memo:
                return memo[(index, open_count)]

            # Nếu open_count < 0, to many ')' → invalid
            if open_count < 0:
                return False

            result = False

            if s[index] == "(":
                # '(': increase open_count
                result = backtracking(index + 1, open_count + 1)
            elif s[index] == ")":
                # Gặp ')': reduce open parentheses
                result = backtracking(index + 1, open_count - 1)
            else:  # s[index] == '*'
                result = (
                    backtracking(index + 1, open_count + 1) or backtracking(index + 1, open_count - 1) or backtracking(index + 1, open_count)
                )

            # store value in cache cache
            memo[(index, open_count)] = result
            return result

        return backtracking(0, 0)

    def checkValidString(self, s: str) -> bool:
        if s[0] == ")":
            return False

        def backtracking(index, stack: list = []):

            if index == len(s):
                if len(stack) == 0:
                    return True
                return False

            if s[index] == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    return backtracking(index + 1, stack[:-1])
                return backtracking(index + 1, stack + [")"])
            if s[index] == "(":
                return backtracking(index + 1, stack + ["("])
            return (
                backtracking(index + 1, stack[:-1]) or backtracking(index + 1, stack + ["("]) or backtracking(index + 1, stack.copy())
            )

        return backtracking(0, [])


class TestValidParenthesisString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_unvalid_parenthesis(self):
        """Test case 0: Simple valid parenthesis"""
        self.assertFalse(self.solution.checkValidStringWithDP("("))

    def test_simple_valid_parenthesis(self):
        """Test case 1: Simple valid parenthesis"""
        self.assertTrue(self.solution.checkValidStringWithDP("()"))

    def test_wildcard_as_left_parenthesis(self):
        """Test case 2: Wildcard can be treated as left parenthesis"""
        self.assertTrue(self.solution.checkValidStringWithDP("(*)"))

    def test_wildcard_as_empty_string(self):
        """Test case 3: Wildcard can be treated as empty string"""
        self.assertTrue(self.solution.checkValidStringWithDP("(*))"))

    def test_wildcard_as_long_string(self):
        """Test case 3: Wildcard can be treated as long string"""
        self.assertFalse(
            self.solution.checkValidStringWithDP(
                "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

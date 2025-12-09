"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens
that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression.
Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in
a reverse polish notation.
The answer and all the intermediate calculations can be represented
in a 32-bit integer.


Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in "+-*/":
                second = stack.pop()
                first = stack.pop()
                if s == "+":
                    stack.append(first + second)
                if s == "-":
                    stack.append(first - second)
                if s == "*":
                    stack.append(first * second)
                if s == "/":
                    stack.append(int(first / second))
            else:
                stack.append(int(s))
        return stack[0]


s_test = Solution()
print(s_test.evalRPN(["6", "-112", "/"]))

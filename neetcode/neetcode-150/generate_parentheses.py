"""
Generate Parentheses
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List


class Solution:
    def __backtracking(self, string, number_open, number_close, n, output):

        if number_open == n and number_close == n:
            output.append(string)
            return

        if number_open < n:
            self.__backtracking(string + "(",
                                number_open + 1,
                                number_close,
                                n,
                                output)

        if number_close < number_open:
            self.__backtracking(string + ")",
                                number_open,
                                number_close + 1,
                                n,
                                output)

    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.__backtracking("", 0, 0, n, output)

        return output


s = Solution()
print(s.generateParenthesis(3))

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


# Test cases
def test_valid_parentheses():
    solution = Solution()

    # Test case 1: Simple valid case - single type of brackets
    # Basic parentheses that are properly matched
    assert solution.isValid("()")
    print("Test case 1 passed: Simple valid parentheses")

    # Test case 2: Multiple types valid - all bracket types mixed
    # All three types of brackets in correct order
    assert solution.isValid("()[]{}")
    print("Test case 2 passed: Multiple valid bracket types")

    # Test case 3: Nested valid case - brackets inside brackets
    # Properly nested structure
    assert solution.isValid("([{}])")
    print("Test case 3 passed: Nested valid brackets")

    # Test case 4: Invalid case - wrong closing order
    # Opening bracket but wrong type of closing bracket
    assert not solution.isValid("([)]")
    print("Test case 4 passed: Invalid wrong closing order")

    # Test case 5: Invalid case - unmatched opening bracket
    # Extra opening bracket without matching closing
    assert not solution.isValid("((")
    print("Test case 5 passed: Invalid unmatched opening bracket")

    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_parentheses()

"""
Docstring for neetcode.neetcode-150.decode_ways
91. Decode Ways
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
In this case, the string is not a valid encoding, so return 0.
"""

import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [-1] * (len(s))

        def backtracking(pointer):

            # base case
            if pointer == len(s):
                return 1

            if s[pointer] == "0":
                return 0

            if cache[pointer] != -1:
                return cache[pointer]

            # one digital
            count = backtracking(pointer + 1)

            # two digital
            if pointer + 1 < len(s):
                two_digit = int(s[pointer: pointer + 2])
                if 10 <= two_digit <= 26:
                    count += backtracking(pointer + 2)

            cache[pointer] = count

            return cache[pointer]

        return backtracking(0)


class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case: '12' can be decoded as 'AB' or 'L'"""
        self.assertEqual(self.solution.numDecodings("12"), 2)

    def test_example_2(self):
        """Test case: '226' can be decoded as 'BZ', 'VF', or 'BBF'"""
        self.assertEqual(self.solution.numDecodings("226"), 3)

    def test_example_3(self):
        """Test case: '06' has leading zero and is invalid"""
        self.assertEqual(self.solution.numDecodings("06"), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

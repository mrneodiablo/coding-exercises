"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"
"""

import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) <= 1:
        #     return s
        # else:
        #     output = s[0]
        #     for i in range(len(s)):
        #         for j in range(i+1, len(s)):
        #             if s[i:j+1] == s[i:j+1][::-1]:
        #                 if len(s[i:j+1]) > len(output):
        #                     output = s[i:j+1]
        # return output

        # loop all element
        n = len(s)
        if n == 0:
            return ""

        best_start = 0
        best_len = 1

        # helper: expand around (left, right), trả về (start, length)
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # khi vòng while dừng: s[left] != s[right] hoặc out of bounds
            start = left + 1
            length = right - left - 1
            return (start, length)

        for i in range(n):
            # odd-length palindromes (center at i)
            (start1, len1) = expand(i, i)
            if len1 > best_len:
                best_start = start1
                best_len = len1

            # even-length palindromes (center between i and i+1)
            (start2, len2) = expand(i, i + 1)
            if len2 > best_len:
                best_start = start2
                best_len = len2

        return s[best_start: best_start + best_len]


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1_odd_length_palindrome(self):
        """Test case 1: Odd-length palindrome from problem description"""
        s = "babad"
        result = self.solution.longestPalindrome(s)
        # Both "bab" and "aba" are valid answers
        self.assertIn(result, ["bab", "aba"])
        self.assertEqual(len(result), 3)

    def test_case_2_even_length_palindrome(self):
        """Test case 2: Even-length palindrome from problem description"""
        s = "cbbd"
        expected = "bb"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)

    def test_case_3_single_character(self):
        """Test case 3: Single character string (edge case)"""
        s = "a"
        expected = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, expected)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("LONGEST PALINDROMIC SUBSTRING - TEST CASES")
    print("=" * 50)

    # Test 1: Odd-length palindrome
    print("Test 1: Odd-length palindrome from problem description")
    s1 = "babad"
    result1 = solution.longestPalindrome(s1)
    valid_answers = ["bab", "aba"]

    print(f"  Input: '{s1}'")
    print("  Expected: 'bab' or 'aba' (length 3)")
    print(f"  Got:      '{result1}'")
    passed1 = result1 in valid_answers
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Even-length palindrome
    print("Test 2: Even-length palindrome from problem description")
    s2 = "cbbd"
    expected2 = "bb"
    result2 = solution.longestPalindrome(s2)

    print(f"  Input: '{s2}'")
    print(f"  Expected: '{expected2}'")
    print(f"  Got:      '{result2}'")
    passed2 = result2 == expected2
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Single character
    print("Test 3: Single character string (edge case)")
    s3 = "a"
    expected3 = "a"
    result3 = solution.longestPalindrome(s3)

    print(f"  Input: '{s3}'")
    print(f"  Expected: '{expected3}'")
    print(f"  Got:      '{result3}'")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Entire string is palindrome
    print("Test 4: Entire string is palindrome")
    s4 = "racecar"
    expected4 = "racecar"
    result4 = solution.longestPalindrome(s4)

    print(f"  Input: '{s4}'")
    print(f"  Expected: '{expected4}'")
    print(f"  Got:      '{result4}'")
    passed4 = result4 == expected4
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: No palindrome longer than 1
    print("Test 5: No palindrome longer than single character")
    s5 = "abcdef"
    result5 = solution.longestPalindrome(s5)

    print(f"  Input: '{s5}'")
    print("  Expected: Any single character (length 1)")
    print(f"  Got:      '{result5}'")
    passed5 = len(result5) == 1 and result5 in s5
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()

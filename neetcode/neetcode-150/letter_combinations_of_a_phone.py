"""
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons)
is given below.
Note that 1 does not map to any letters.
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

from typing import List
from collections import deque
import unittest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # Handle empty string case
            return []

        queue = deque()
        i = 0
        previous_number_combination = 1
        mapping_key = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        while i < len(digits):
            if previous_number_combination == 1:
                for letter in mapping_key[digits[i]]:
                    queue.append(letter)
            else:
                for _ in range(previous_number_combination):
                    combining_letter = queue.popleft()

                    for letter in mapping_key[digits[i]]:
                        queue.append(combining_letter + letter)

            previous_number_combination = previous_number_combination * len(
                mapping_key[digits[i]]
            )
            i += 1

        return list(queue)


class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem description
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        result = self.solution.letterCombinations(digits)
        result_list = list(result)  # Convert deque to list
        self.assertEqual(
            sorted(result_list),
            sorted(expected),
            f"Expected {expected}, got {result_list}",
        )

    def test_run_2(self):
        # Test case 2: Empty input
        digits = ""
        expected = []
        result = self.solution.letterCombinations(digits)
        result_list = list(result)
        self.assertEqual(
            result_list, expected, f"Expected {expected}, got {result_list}"
        )

    def test_run_3(self):
        # Test case 3: Single digit
        digits = "2"
        expected = ["a", "b", "c"]
        result = self.solution.letterCombinations(digits)
        result_list = list(result)
        self.assertEqual(
            sorted(result_list),
            sorted(expected),
            f"Expected {expected}, got {result_list}",
        )


def test_letter_combinations():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Two digits '23'")
    digits1 = "23"
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result1 = solution.letterCombinations(digits1)
    result1_list = list(result1)
    print(f"  Input: digits = '{digits1}'")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1_list}")
    passed1 = sorted(result1_list) == sorted(expected1)
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    print("Test 2: Empty string ''")
    digits2 = ""
    expected2 = []
    result2 = solution.letterCombinations(digits2)
    result2_list = list(result2)
    print(f"  Input: digits = '{digits2}'")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2_list}")
    print(f"  ✅ {'PASSED' if result2_list == expected2 else 'FAILED'}")
    print()

    print("Test 3: Single digit '2'")
    digits3 = "2"
    expected3 = ["a", "b", "c"]
    result3 = solution.letterCombinations(digits3)
    result3_list = list(result3)
    print(f"  Input: digits = '{digits3}'")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3_list}")
    passed3 = sorted(result3_list) == sorted(expected3)
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    print("Test 4: Three digits '234'")
    digits4 = "234"
    # Should have 3 * 3 * 3 = 27 combinations
    result4 = solution.letterCombinations(digits4)
    result4_list = list(result4)
    expected_count4 = 27
    print(f"  Input: digits = '{digits4}'")
    print(f"  Expected count: {expected_count4} combinations")
    print(f"  Got count:      {len(result4_list)} combinations")
    print(f"  Sample results: {result4_list[:5]}... (showing first 5)")
    passed4 = len(result4_list) == expected_count4
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    print("Test 5: Digits with 4 letters '7' (pqrs)")
    digits5 = "7"
    expected5 = ["p", "q", "r", "s"]
    result5 = solution.letterCombinations(digits5)
    result5_list = list(result5)
    print(f"  Input: digits = '{digits5}'")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5_list}")
    passed5 = sorted(result5_list) == sorted(expected5)
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLetterCombinations)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "=" * 50)
    test_letter_combinations()

"""
Docstring for neetcode.neetcode-150.letter_combinations_of_a_phone_number

Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]
"""

from typing import List
import unittest


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        ans = []
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

        def dfs(index, path):
            if index == len(digits):
                ans.append("".join(path))  # join when finish
                return

            for letter in mapping_key[digits[index]]:
                path.append(letter)  # add to path
                dfs(index + 1, path)  # go deeper
                path.pop()  # Backtrack: pop remove try another letter

        dfs(0, [])
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test with two digits '23'"""
        digits = "23"
        result = self.solution.letterCombinations(digits)
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        """Test with single digit '2'"""
        digits = "2"
        result = self.solution.letterCombinations(digits)
        expected = ["a", "b", "c"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_string(self):
        """Test with empty string"""
        digits = ""
        result = self.solution.letterCombinations(digits)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

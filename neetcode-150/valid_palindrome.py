"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome,
or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after
removing non-alphanumeric characters.
Since an empty string reads the same forward and backward,
it is a palindrome.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()

        length_s = len(s)
        for i in range(length_s // 2):
            if s[i] != s[length_s - 1 - i]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Classic palindrome with mixed case and punctuation
    test1 = "A man, a plan, a canal: Panama"
    print(f"Test 1: '{test1}' -> {solution.isPalindrome(test1)}")
    # Expected: True

    # Test case 2: Non-palindrome
    test2 = "race a car"
    print(f"Test 2: '{test2}' -> {solution.isPalindrome(test2)}")
    # Expected: False

    # Test case 3: Empty string after removing non-alphanumeric
    test3 = " "
    print(f"Test 3: '{test3}' -> {solution.isPalindrome(test3)}")
    # Expected: True

    # Test case 4: String with numbers and special characters
    test4 = "Was it a car or a cat I saw?"
    print(f"Test 4: '{test4}' -> {solution.isPalindrome(test4)}")
    # Expected: True

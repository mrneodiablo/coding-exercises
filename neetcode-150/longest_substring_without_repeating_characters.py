"""
Given a string s,
find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        # Optimized Sliding Window with Hash Map
        char_index = {}  # Track last seen index of each character
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If character seen before and within current window
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1  # Move left past the duplicate

            char_index[s[right]] = right  # Update character's latest index
            max_len = max(max_len, right - left + 1)  # Simple arithmetic

        return max_len

    def lengthOfLongestSubstring_YourApproach(self, s: str) -> int:
        # Your original approach (for comparison)
        if len(s) <= 1:
            return len(s)

        window_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] not in window_set:
                window_set.add(s[right])
            else:
                while left <= right:
                    if s[right] == s[left]:
                        left += 1
                        break
                    window_set.remove(s[left])
                    left += 1
                window_set.add(s[right])  # Add the duplicate character back

            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic example from problem
    test1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(test1)
    print(f"Test 1: '{test1}' -> {result1} (Expected: 3)")
    print("  Explanation: 'abc' has length 3")

    testx = "dvdf"
    resultx = solution.lengthOfLongestSubstring(testx)
    print(f"Test x: '{testx}' -> {resultx} (Expected: 3)")
    print("  Explanation: 'abc' has length 3")

    # Test Case 2: All same characters
    test2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(test2)
    print(f"\nTest 2: '{test2}' -> {result2} (Expected: 1)")
    print("  Explanation: 'b' has length 1")

    # Test Case 3: Mixed pattern
    test3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(test3)
    print(f"\nTest 3: '{test3}' -> {result3} (Expected: 3)")
    print("  Explanation: 'wke' has length 3")

    # Test Case 4: Empty string
    test4 = ""
    result4 = solution.lengthOfLongestSubstring(test4)
    print(f"\nTest 4: '{test4}' -> {result4} (Expected: 0)")
    print("  Explanation: Empty string has length 0")

    # Test Case 5: Single character
    test5 = "a"
    result5 = solution.lengthOfLongestSubstring(test5)
    print(f"\nTest 5: '{test5}' -> {result5} (Expected: 1)")
    print("  Explanation: Single character 'a' has length 1")

    # Test Case 6: No repeating characters
    test6 = "abcdef"
    result6 = solution.lengthOfLongestSubstring(test6)
    print(f"\nTest 6: '{test6}' -> {result6} (Expected: 6)")
    print("  Explanation: Entire string 'abcdef' has no duplicates")

    # Test Case 7: Two characters alternating
    test7 = "abab"
    result7 = solution.lengthOfLongestSubstring(test7)
    print(f"\nTest 7: '{test7}' -> {result7} (Expected: 2)")
    print("  Explanation: 'ab' has length 2")

    # # Test Case 8: Complex pattern
    # test8 = "dvdf"
    # result8 = solution.lengthOfLongestSubstring(test8)
    # print(f"\nTest 8: '{test8}' -> {result8} (Expected: 3)")
    # print("  Explanation: 'vdf' has length 3")

    # # Test Case 9: Longer string with multiple patterns
    # test9 = "abcdefghijklmnopqrstuvwxyz"
    # result9 = solution.lengthOfLongestSubstring(test9)
    # print(f"\nTest 9: '{test9}' -> {result9} (Expected: 26)")
    # print("  Explanation: All 26 lowercase letters, no duplicates")

    # # Test Case 10: String with spaces and special characters
    # test10 = "a b c a b c"
    # result10 = solution.lengthOfLongestSubstring(test10)
    # print(f"\nTest 10: '{test10}' -> {result10} (Expected: 3)")
    # print("  Explanation: 'a b' or ' bc' has length 3")

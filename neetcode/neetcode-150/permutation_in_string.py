"""
Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of
s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create arrays to count each letter (a-z)
        # Index 0 = 'a', Index 1 = 'b', ..., Index 25 = 'z'
        s1Count = [0] * 26  # [0,0,0,...,0] (26 zeros)
        s2Count = [0] * 26  # [0,0,0,...,0] (26 zeros)

        # HOW ord(char) - ord('a') WORKS:
        # ord('a') = 97, ord('b') = 98, ord('c') = 99, etc.
        # ord('a') - ord('a') = 97 - 97 = 0 → index 0
        # ord('b') - ord('a') = 98 - 97 = 1 → index 1
        # ord('c') - ord('a') = 99 - 97 = 2 → index 2
        # So each letter maps to its position in alphabet!

        # Initialize frequency counts for s1 and the first window in s2
        for i in range(len(s1)):
            # Count letters in s1
            letter_index = ord(s1[i]) - ord("a")
            s1Count[letter_index] += 1

            # Count letters in first window of s2 (same size as s1)
            letter_index = ord(s2[i]) - ord("a")
            s2Count[letter_index] += 1

        # Slide the window over s2
        for i in range(len(s2) - len(s1)):
            if s1Count == s2Count:
                return True

            # SLIDING WINDOW EXPLANATION:
            # When we slide the window, we need to:
            # 1. REMOVE the character that's leaving the window (leftmost)
            # 2. ADD the character that's entering the window (rightmost)

            # s2[i] = character LEAVING the window (leftmost character)
            s2Count[ord(s2[i]) - ord("a")] -= 1  # Remove from count

            # s2[i + len(s1)] = character ENTERING
            # the window (rightmost character)
            s2Count[ord(s2[i + len(s1)]) - ord("a")] += 1  # Add to count

        # Check the last window
        return s1Count == s2Count


"""
WHY USE ARRAYS FOR COUNTING CHARACTERS?

Method 1 - Dictionary (what you might think of first):
char_count = {'a': 1, 'b': 1, 'c': 0, ...}

Method 2 - Array (what we're using):
char_count = [1, 1, 0, 0, 0, ...]  # index 0='a', 1='b', 2='c'...

WHY ARRAYS ARE BETTER HERE:
1. FASTER: Array access is O(1), dictionary is slightly slower
2. SIMPLER: No need to handle missing keys
3. EASY COMPARISON: Can compare entire arrays with ==
4. FIXED SIZE: We know there are exactly 26 lowercase letters

THE MAPPING TRICK:
ord('a') = 97, ord('b') = 98, ord('c') = 99...
So: ord(letter) - ord('a') gives us the alphabet position!
'a' → 97-97 = 0
'b' → 98-97 = 1
'c' → 99-97 = 2
...
'z' → 122-97 = 25

This maps each letter to an array index from 0-25!
"""


# Test cases
def test_permutation_in_string():
    solution = Solution()

    # Test case 1: Basic positive case - permutation exists
    # s2 contains "ba" which is a permutation of "ab"
    assert solution.checkInclusion("ab", "eidbaooo")
    print("Test case 1 passed: Basic permutation found")

    # Test case 2: Basic negative case - no permutation exists
    # s2 doesn't contain any permutation of "ab"
    assert not solution.checkInclusion("ab", "eidboaoo")
    print("Test case 2 passed: No permutation found")

    # Test case 3: Single character strings
    # Simple case with single characters
    assert solution.checkInclusion("a", "ab")
    print("Test case 3 passed: Single character permutation")

    # Test case 4: Repeated characters in s1
    # s1 has repeated characters, s2 contains the permutation
    assert solution.checkInclusion("adc", "dcda")
    print("Test case 4 passed: Repeated characters permutation")

    # Test case 5: s1 longer than s2
    # Impossible case - s1 is longer than s2
    assert not solution.checkInclusion("abcd", "abc")
    print("Test case 5 passed: s1 longer than s2")

    print("All test cases passed!")


if __name__ == "__main__":
    test_permutation_in_string()

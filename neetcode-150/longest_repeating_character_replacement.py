"""
You are given a string s and an integer k.
You can choose any character of the string and change
it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing
the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window approach
        # Key insight: We need to find the longest substring where
        # (length - most_frequent_char_count) <= k

        char_count = {}  # Count of each character in current window
        left = 0
        max_length = 0
        max_freq = 0  # Count of most frequent character in current window

        for right in range(len(s)):
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Update max frequency in current window
            max_freq = max(max_freq, char_count[s[right]])

            # Current window size
            window_size = right - left + 1

            # If we need more than k replacements, shrink window
            if window_size - max_freq > k:
                # Remove leftmost character
                char_count[s[left]] -= 1
                left += 1
                # Recalculate max_freq (expensive!)
                max_freq = max(char_count.values()) if char_count else 0

            # Update maximum length found
            max_length = max(max_length, right - left + 1)

        return max_length


def test_character_replacement():
    solution = Solution()

    # Test case 1: Basic example from problem description
    assert solution.characterReplacement("ABAB", 2) == 4
    print("Test 1 passed: ABAB with k=2 -> 4")

    # Test case 2: Second example from problem description
    assert solution.characterReplacement("AABABBA", 1) == 4
    print("Test 2 passed: AABABBA with k=1 -> 4")

    # Test case 3: All same characters (no replacements needed)
    assert solution.characterReplacement("AAAA", 2) == 4
    print("Test 3 passed: AAAA with k=2 -> 4")

    # Test case 4: Single character string
    assert solution.characterReplacement("A", 1) == 1
    print("Test 4 passed: A with k=1 -> 1")

    # Test case 5: Longer string with optimal replacement strategy
    assert solution.characterReplacement("AABABCBA", 2) == 5
    print("Test 5 passed: AABABCBA with k=2 -> 5")

    print("All test cases passed!")


if __name__ == "__main__":
    test_character_replacement()

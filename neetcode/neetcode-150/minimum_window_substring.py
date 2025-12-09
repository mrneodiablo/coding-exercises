"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of
s such that every character in t (including duplicates)
is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC"
includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

"""

import time


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Use 58 to cover 'A' to 'z' (uppercase and lowercase)
        checker_t = [0] * 58
        checker_s = [0] * 58

        # Count all characters in t
        for i in range(len(t)):
            checker_t[ord(t[i]) - ord("A")] += 1

        # Start with empty window
        left_s = 0
        right_s = 0
        min_len = float("inf")
        output = ""

        while right_s < len(s):
            # Add current character to window
            right_char_idx = ord(s[right_s]) - ord("A")
            checker_s[right_char_idx] += 1

            # Try to shrink window from left while it's valid
            while self.isValidWindow(checker_s, checker_t):
                # Update minimum window if current is smaller
                current_len = right_s - left_s + 1
                if current_len < min_len:
                    min_len = current_len
                    output = s[left_s:right_s + 1]

                # Remove leftmost character and shrink window
                left_char_idx = ord(s[left_s]) - ord("A")
                checker_s[left_char_idx] -= 1
                left_s += 1

            # Expand window
            right_s += 1

        return output

    def isValidWindow(self, window_count, target_count):
        """Check if current window contains all required characters"""
        for i in range(len(target_count)):
            if window_count[i] < target_count[i]:
                return False
        return True


class OptimizedSolution:
    """
    More efficient solution using the 'formed' counter optimization.

    Key improvements:
    1. Uses dictionary instead of large arrays (only stores chars that exist)
    2. Tracks 'formed' count to avoid checking entire array every time
    3. Only checks validity when we have the right number of unique chars

    Time Complexity: O(|s| + |t|) instead of O(|s| * 58) for array comparison
    """

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Count characters in t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        required = len(dict_t)  # Number of unique characters in t
        formed = 0  # Number of unique chars in current window
        # with correct frequency

        window_counts = {}

        # Left and right pointers
        left = right = 0

        # Answer: (window length, left, right)
        ans = float("inf"), None, None

        while right < len(s):
            # Add one character from right to the window
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1

            # Check if this character's frequency
            # matches the required frequency in t
            if character in dict_t and (
                    window_counts[character] == dict_t[character]):
                formed += 1

            # Try to contract the window until it's no longer valid
            while left <= right and formed == required:
                character = s[left]

                # Save the smallest window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove from left of our window
                window_counts[character] -= 1
                if (character in dict_t) and (
                        window_counts[character] < dict_t[character]):
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# Test cases
def test_minimum_window_substring():
    print("=== Testing Original Solution ===")
    solution = Solution()

    # Test case 1: Basic example - multiple valid windows, return shortest
    result1 = solution.minWindow("ADOBECODEBANC", "ABC")
    assert result1 == "BANC", f"Expected 'BANC', got '{result1}'"
    print("Test case 1 passed: Basic multiple windows case")

    # Test case 2: Single character - exact match
    result2 = solution.minWindow("a", "a")
    assert result2 == "a", f"Expected 'a', got '{result2}'"
    print("Test case 2 passed: Single character match")

    # Test case 3: Impossible case - not enough characters
    result3 = solution.minWindow("a", "aa")
    assert result3 == "", f"Expected '', got '{result3}'"
    print("Test case 3 passed: Impossible case")

    # Test case 4: Duplicate characters in t
    result4 = solution.minWindow("aa", "aa")
    assert result4 == "aa", f"Expected 'aa', got '{result4}'"
    print("Test case 4 passed: Duplicate characters")

    # Test case 5: Complex case - entire string is minimum window
    result5 = solution.minWindow("abc", "abc")
    assert result5 == "abc", f"Expected 'abc', got '{result5}'"
    print("Test case 5 passed: Entire string as window")

    print("All original solution test cases passed!")
    print()

    print("=== Testing Optimized Solution ===")
    optimized_solution = OptimizedSolution()

    # Test the same cases with optimized solution
    opt_result1 = optimized_solution.minWindow("ADOBECODEBANC", "ABC")
    assert opt_result1 == "BANC", f"Expected 'BANC', got '{opt_result1}'"
    print("Optimized Test case 1 passed: Basic multiple windows case")

    opt_result2 = optimized_solution.minWindow("a", "a")
    assert opt_result2 == "a", f"Expected 'a', got '{opt_result2}'"
    print("Optimized Test case 2 passed: Single character match")

    opt_result3 = optimized_solution.minWindow("a", "aa")
    assert opt_result3 == "", f"Expected '', got '{opt_result3}'"
    print("Optimized Test case 3 passed: Impossible case")

    opt_result4 = optimized_solution.minWindow("aa", "aa")
    assert opt_result4 == "aa", f"Expected 'aa', got '{opt_result4}'"
    print("Optimized Test case 4 passed: Duplicate characters")

    opt_result5 = optimized_solution.minWindow("abc", "abc")
    assert opt_result5 == "abc", f"Expected 'abc', got '{opt_result5}'"
    print("Optimized Test case 5 passed: Entire string as window")

    print("All optimized solution test cases passed!")
    print()

    # Performance comparison test
    print("=== Performance Comparison (Large Input) ===")
    # Large string with target at the end
    large_s = "a" * 10000 + "bc" + "a" * 10000
    large_t = "abc"

    # Test original solution
    start_time = time.time()
    original_result = solution.minWindow(large_s, large_t)
    original_time = time.time() - start_time

    # Test optimized solution
    start_time = time.time()
    optimized_result = optimized_solution.minWindow(large_s, large_t)
    optimized_time = time.time() - start_time

    print(f"Original solution time: {original_time:.4f} seconds")
    print(f"Optimized solution time: {optimized_time:.4f} seconds")
    print(
        f"Speedup: {original_time/optimized_time:.2f}x faster"
        if optimized_time > 0
        else "Optimized is much faster"
    )

    assert original_result == optimized_result, "Results should be the same!"
    print("Both solutions produce the same result!")


if __name__ == "__main__":
    test_minimum_window_substring()

"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encode using length-prefixed format: "length#string"
        Example: ["abc", "de"] -> "3#abc2#de"
        """
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        """
        Decode length-prefixed strings using two pointers
        Format: "length#string"
        """
        result = []
        slow = 0  # Start of current segment
        fast = 0  # Scanning pointer

        while fast < len(s):
            # Move fast pointer until we find '#'
            if s[fast] != "#":
                fast += 1
            else:
                # Extract the length from slow to fast
                length = int(s[slow:fast])

                # Calculate string boundaries
                string_start = fast + 1  # After the '#'
                string_end = string_start + length

                # Extract the actual string
                result.append(s[string_start:string_end])

                # Move both pointers to start of next segment
                slow = string_end
                fast = slow

        return result


if __name__ == "__main__":
    # Test case 1: Normal strings
    string1 = ["neet", "code", "love", "you"]

    solution = Solution()
    encoded1 = solution.encode(string1)
    decoded1 = solution.decode(encoded1)
    print(f"Test 1 - Original: {string1}")
    print(f"Test 1 - Encoded: {encoded1}")
    print(f"Test 1 - Decoded: {decoded1}")
    print(f"Test 1 - Correct: {string1 == decoded1}")
    print()

    # Test case 2: Strings containing the delimiter '#'
    string2 = ["we", "say", ":", "yes", "#problem"]
    encoded2 = solution.encode(string2)
    decoded2 = solution.decode(encoded2)
    print(f"Test 2 - Original: {string2}")
    print(f"Test 2 - Encoded: {encoded2}")
    print(f"Test 2 - Decoded: {decoded2}")
    print(f"Test 2 - Correct: {string2 == decoded2}")
    print()

    # Test case 3: Empty strings
    string3 = ["", "hello", "", "world", ""]
    encoded3 = solution.encode(string3)
    decoded3 = solution.decode(encoded3)
    print(f"Test 3 - Original: {string3}")
    print(f"Test 3 - Encoded: {encoded3}")
    print(f"Test 3 - Decoded: {decoded3}")
    print(f"Test 3 - Correct: {string3 == decoded3}")

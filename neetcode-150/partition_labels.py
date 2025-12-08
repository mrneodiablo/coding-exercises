"""
Partition Labels

You are given a string s.
We want to partition the string into as many parts
as possible so that each letter appears in at most one part.
For example, the string "ababcc" can be partitioned into
["abab", "cc"],
but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after
concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect,
because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []

        if len(s) <= 1:
            return [1]

        char_ranges: dict[str, list] = {}
        # char_ranges = {
        #     'a': [0, 8],   # 'a' xuất hiện từ index 0 đến 8
        #     'b': [1, 5],   # 'b' xuất hiện từ index 1 đến 5
        #     'c': [4, 7],   # 'c' xuất hiện từ index 4 đến 7
        #     'd': [9, 14],  # 'd' xuất hiện từ index 9 đến 14
        #     'e': [11, 15], # 'e' xuất hiện từ index 11 đến 15
        # }

        for i in range(len(s)):
            if s[i] not in char_ranges:
                char_ranges[s[i]] = [i, i]
            else:
                char_ranges[s[i]][1] = i

        intervals: list[int, int] = []
        for _, v in char_ranges.items():
            intervals.append(v)

        intervals.sort(key=lambda x: x[0])
        # intervals = [
        #     [0, 8],   # a
        #     [1, 5],   # b
        #     [4, 7],   # c
        #     [9, 14],  # d
        #     [11, 15], # e
        # ]
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        for element in merged:
            ans.append(element[1] - element[0] + 1)

        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiple partitions with different lengths
    s1 = "ababcbacadefegdehijhklij"
    result1 = solution.partitionLabels(s1)
    print("Test 1:")
    print(f"Input:  '{s1}'")
    print(f"Output: {result1}")
    print("Expected: [9, 7, 8]")
    print("Explanation: 'ababcbaca' (9), 'defegde' (7), 'hijhklij' (8)")
    print()

    # Test case 2: Single partition (all letters interleaved)
    s2 = "eccbbbbdec"
    result2 = solution.partitionLabels(s2)
    print("Test 2:")
    print(f"Input:  '{s2}'")
    print(f"Output: {result2}")
    print("Expected: [10]")
    print(
        "Explanation: 'e' appears at index 0 and 9,"
        "so all must be in one partition"
    )
    print()

    # Test case 3: Each character appears only once
    s3 = "abcdef"
    result3 = solution.partitionLabels(s3)
    print("Test 3:")
    print(f"Input:  '{s3}'")
    print(f"Output: {result3}")
    print("Expected: [1, 1, 1, 1, 1, 1]")
    print(
        "Explanation: Each letter appears once,"
        "so each can be its own partition")
    print()

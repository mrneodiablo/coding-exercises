"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as
they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as
they can be rearranged to form each other.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = {}
        for element in strs:
            key = "".join(sorted(element))
            if checker.get(key):
                checker[key].append(element)
            else:
                checker[key] = [element]

        return [values for _, values in checker.items()]


if __name__ == "__main__":
    strs_test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs_test))

"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        checker = {}
        for s_check in s:
            if checker.get(s_check):
                checker[s_check] += 1
            else:
                checker[s_check] = 1

        for t_check in t:
            if checker.get(t_check) is None:
                return False

            if checker.get(t_check) > 1:
                checker[t_check] -= 1
            else:
                del checker[t_check]
        if len(checker) > 0:
            return False

        return True


s_tmp = "anagram"
t_tmp = "nagaram"
solution = Solution()
print(solution.isAnagram(s_tmp, t_tmp))

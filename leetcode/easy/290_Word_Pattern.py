class Solution:
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a = {}
        check = []
        if len(pattern) != len(s.split(" ")):
            return False

        for i in range(0, len(pattern)):
            if a.get(pattern[i]) is None:
                if s.split(" ")[i] not in check:
                    a[pattern[i]] = s.split(" ")[i]
                    check.append(s.split(" ")[i])
                else:
                    return False
            else:
                if a.get(pattern[i]) != s.split(" ")[i]:
                    return False
        return True

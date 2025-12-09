class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        if n == 0:
            return 0
        while n / 2 > 0:
            if n % 2 == 1:
                res += 1
            n = n / 2
        return res + 1

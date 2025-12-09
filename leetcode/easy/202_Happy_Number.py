class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        break_loop = set()
        while n != 1:
            if n in break_loop:
                return False
            tmp = 0
            break_loop.add(n)
            for i in str(n):
                tmp += int(i)**2
            n = tmp
        return True

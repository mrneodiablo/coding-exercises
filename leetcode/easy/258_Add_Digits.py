class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            tmp = 0
            for i in str(num):
                tmp += int(i)
            num = tmp

        return num

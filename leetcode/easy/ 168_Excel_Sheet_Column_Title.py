class Solution:
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        answer = ""
        while columnNumber != 0:
            index = columnNumber % 26
            if index == 0:
                index = 26
            answer = chr(64 + int(index)) + answer
            columnNumber -= index
            columnNumber = columnNumber / 26
        return answer

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows+1):
            if i == 1:
                res.append([1])
            elif i == 2:
                res.append([1, 1])
            else:
                tmp = []
                for x in range(0, i):
                    if x == 0:
                        tmp.append(1)
                    elif x == i-1:
                        tmp.append(1)
                    else:
                        tmp.append(res[i-2][x-1]+res[i-2][x])
                res.append(tmp)
        return res

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex+1)[rowIndex]

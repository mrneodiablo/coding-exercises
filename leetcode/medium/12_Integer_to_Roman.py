class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        out = ""
        mapp = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        tmp = mapp.keys()
        tmp.sort(reverse=True)
        while num > 0:
            for i in tmp:
                if num >= i:
                    num = num - i
                    out = out + mapp[i]
                    break

        return out

class Solution:
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(nums)
        mx = 0
        for i in range(0, len(tmp) / 2):
            a = tmp[i] + tmp[len(tmp) - i - 1]
            mx = max(mx, a)
        return mx

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tmp = []
        out = []
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        i = 1
        start = nums[0]
        end = nums[0]

        while i <= (len(nums) - 1):

            if nums[i] != nums[i - 1] + 1:
                tmp.append([start, end])
                start = nums[i]
                end = nums[i]
            else:
                end = nums[i]

            if i == len(nums) - 1:
                tmp.append([start, end])
            i += 1

        for i in tmp:
            if i[0] == i[1]:
                out.append(str(i[0]))
            else:
                out.append(str(i[0]) + "->" + str(i[1]))
        return out

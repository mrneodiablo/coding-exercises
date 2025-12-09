class Solution:
    def moveZeroes(self, nums):
        """
        :type nw`ums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tmp = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                tmp.append(i)

        for i in range(len(tmp)):
            nums.pop(tmp[i] - i)
            nums.append(0)
        return nums

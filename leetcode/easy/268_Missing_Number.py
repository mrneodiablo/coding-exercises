class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if 0 != nums[0]:
            return 0

        if len(nums) != nums[-1]:
            return len(nums)

        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1] - 1:
                return nums[i] + 1

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapp = {}
        for i in range(len(nums)):  # O(n)
            value = nums[i]  # O(1)
            if value in mapp:
                if abs(i - mapp[value]) <= k:
                    return True
            mapp[value] = i
        return False

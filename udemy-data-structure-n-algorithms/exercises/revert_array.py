def revert(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) // 2):
        nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
    return nums


# [3,2,1]
print(revert([1, 2, 3]))


# [4,3,2,1]
print(revert([1, 2, 3, 4]))


# [4,3,2,1]
print(revert([5, 1, 2, 3, 4]))

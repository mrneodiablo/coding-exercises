def rotate(nums, k):
    k = k % len(nums)  # Handle cases where k > len(nums)
    nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


test_nums = [1, 2, 3, 4, 4, 5, 6, 7]

test_k = 3
rotate(test_nums, test_k)
print("Rotated array:", test_nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""

def insertion_sort(nums) -> list:
    for i in range(1, len(nums)):
        tmp = i
        while tmp > 0:
            if nums[tmp] < nums[tmp - 1]:
                nums[tmp], nums[tmp - 1] = nums[tmp - 1], nums[tmp]
                tmp = tmp - 1
            else:
                break
    return nums


if __name__ == "__main__":
    test = [3, 2, 4, 1, 6, 8, 3, 6]
    insertion_sort(test)
    print(test)

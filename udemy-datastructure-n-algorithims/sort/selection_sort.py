def selection_sort(nums) -> list:
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j

        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


if __name__ == "__main__":
    test = [4, 2, 6, 5, 1, 3]
    tmp = selection_sort(test)
    print(tmp)

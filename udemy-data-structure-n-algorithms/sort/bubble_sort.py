def bubble_sort(nums) -> list:
    # Bubble Sort: Compare adjacent pairs and swap if left > right
    # Larger elements "bubble up" to the end after each complete pass
    # Time: O(n²) worst/average case, O(n) best case (already sorted)
    # Space: O(1) - sorts in-place
    # After each outer loop iteration,
    # the largest unsorted element is in its final position
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == "__main__":
    test = [3, 2, 4, 1, 6, 8, 3, 6]
    bubble_sort(test)
    print(test)

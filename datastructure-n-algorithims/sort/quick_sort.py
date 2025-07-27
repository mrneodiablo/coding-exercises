def quick_sort_pivot(my_list, pivot_index, end_index) -> int:
    if len(my_list) <= 1:
        return None

    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            if swap_index != i:
                my_list[swap_index], my_list[i] = (
                    my_list[i], my_list[swap_index]
                )

    my_list[swap_index], my_list[pivot_index] = (
        my_list[pivot_index],
        my_list[swap_index],
    )
    return swap_index


def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot = quick_sort_pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot - 1)
        quick_sort_helper(my_list, pivot + 1, right)


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)


a = [4, 1, 3, 2, 6, 7, 5]
quick_sort(a)
print(a)

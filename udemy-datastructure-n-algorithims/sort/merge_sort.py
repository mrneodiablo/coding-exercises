def merge_sort(my_list) -> list:
    if len(my_list) == 1:
        return my_list
    midle_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:midle_index])
    right = merge_sort(my_list[midle_index:])

    return merge_list(left, right)


def merge_list(sorted_list_a: list, sorted_list_b: list) -> list:
    combine_list = []
    i = 0
    j = 0
    while i < len(sorted_list_a) and j < len(sorted_list_b):
        if sorted_list_a[i] < sorted_list_b[j]:
            combine_list.append(sorted_list_a[i])
            i += 1
        else:
            combine_list.append(sorted_list_b[j])
            j += 1

    while i < len(sorted_list_a):
        combine_list.append(sorted_list_a[i])
        i += 1

    while j < len(sorted_list_b):
        combine_list.append(sorted_list_b[j])
        j += 1

    return combine_list


a = merge_sort([1, 6, 2, 6])
print(a)

from typing import List


def remove_duplicates(array: List) -> List:
    tmp = set()
    output = []
    for el in array:
        if el not in tmp:
            tmp.add(el)
            output.append(el)
    return output


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
    new_list = remove_duplicates(my_list)
    print(new_list)

    """
        EXPECTED OUTPUT:
        ----------------
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

        (Order may be different as sets are unordered)

    """

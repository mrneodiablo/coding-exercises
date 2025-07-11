from typing import List


def find_pairs(arr1: List, arr2: List, target: int) -> List:
    output = []
    set_arr1 = set(arr1)
    for num in arr2:
        if (target - num) in set_arr1:
            output.append((target - num, num))
    return output


if __name__ == "__main__":
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 4, 6, 8, 10]
    tg = 7

    pairs = find_pairs(a1, a2, tg)
    print(pairs)

    """
        EXPECTED OUTPUT:
        ----------------
        [(5, 2), (3, 4), (1, 6)]

    """

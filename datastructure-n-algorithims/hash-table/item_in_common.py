from typing import List


def item_in_common(list1: List, list2: List) -> List:
    tmp = {}
    output = []
    for i in list1:
        tmp[i] = 1

    for i in list2:
        if tmp.get(i) is not None:
            output.append(i)
    return output


def item_in_common_o_n_n(list1: List, list2: List) -> List:
    output = []
    for i in list1:
        for j in list2:
            if i == j:
                output.append(i)
    return output


if __name__ == "__main__":
    l1 = [1, 3, 5]
    l2 = [2, 4, 5]
    common = item_in_common(list1=l1, list2=l2)
    print(common)

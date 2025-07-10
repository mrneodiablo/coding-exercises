from typing import List


def find_duplicates(nums: List) -> List:
    output = []
    checker = {}
    for num in nums:
        if checker.get(num) is not None:
            checker[num] += 1
            if checker[num] == 2:
                output.append(num)
        else:
            checker[num] = 1
    return output


def first_non_repeating_char(string: str) -> str:
    tmp = {}

    for c in string:
        if tmp.get(c) is not None:
            tmp[c] += 1
        else:
            tmp[c] = 1

    for c in string:
        if tmp.get(c) == 1:
            return c
    return None


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 4, 5]))
    print(find_duplicates([1, 1, 2, 2, 3]))
    print(find_duplicates([1, 1, 1, 1, 1]))
    print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
    print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
    print(find_duplicates([]))

    print(first_non_repeating_char("leetcode"))
    print(first_non_repeating_char("hello"))
    print(first_non_repeating_char("aabbcc"))


"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

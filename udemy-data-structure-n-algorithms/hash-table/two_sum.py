from typing import List


def two_sum(nums: List, target: int) -> List:
    checker = {}
    output = []
    for i in range(len(nums)):

        if checker.get(target - nums[i]) is not None:
            output.append(checker.get(target - nums[i]))
            output.append(i)
            break
        checker[nums[i]] = i
    return output


if __name__ == "__main__":

    # print(two_sum([5, 1, 7, 2, 9, 3], 10))
    print(two_sum([3, 3], 6))

    # print(two_sum([4, 2, 11, 7, 6, 3], 9))
    # print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    # print(two_sum([1, 3, 5, 7, 9], 10))
    # print(two_sum([1, 2, 3, 4, 5], 10))
    # print(two_sum([1, 2, 3, 4, 5], 7))
    # print(two_sum([1, 2, 3, 4, 5], 3))
    # print(two_sum([], 0))

    """
        EXPECTED OUTPUT:
        ----------------
        [1, 4]
        [1, 3]
        [0, 3]
        [1, 3]
        []
        [2, 3]
        [0, 1]
        []

    """

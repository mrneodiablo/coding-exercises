from typing import List


def subarray_sum_o_n_n(nums: List, target: int) -> List:
    output = []
    for i in range(0, len(nums)):
        tmp = nums[i]
        if tmp == target:
            output = [i, i]
            return output

        for j in range(i + 1, len(nums)):
            tmp += nums[j]

            if tmp != target:
                continue

            output = [i, j]
            return output
    return output


def subarray_sum(nums: List, target: int) -> List:
    # the idea to gain complexity is O(n):
    # current_accumalate_sum = target + previous_accumalate_sum
    # ==> target = current_accumalate_sum - previous_accumalate_sum
    checker = {0: -1}
    current_accumulate = 0
    output = []
    for index, value in enumerate(nums):
        current_accumulate += value
        if checker.get(current_accumulate - target) is None:
            checker[current_accumulate] = index
        else:
            index_prev = checker.get(current_accumulate - target)
            output.append(index_prev + 1)
            output.append(index)
            return output
    return []


nu = [1, 2, 3, 4, 5]
tg = 9
print(subarray_sum(nu, tg))

nu = [-1, 2, 3, -4, 5]
tg = 0
print(subarray_sum(nu, tg))

nu = [2, 3, 4, 5, 6]
tg = 3
print(subarray_sum(nu, tg))

nu = []
tg = 0
print(subarray_sum(nu, tg))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

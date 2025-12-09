from typing import List


def longest_consecutive_sequence_not_optimal(nums: List) -> int:
    if len(nums) < 1:
        return 0
    nums.sort()
    max_len = 1
    max_out = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue

        if nums[i] == nums[i - 1] + 1:
            max_len += 1
        else:
            max_out = max(max_len, max_out)
            max_len = 1

    return max(max_len, max_out)


def longest_consecutive_sequence(nums: List) -> int:
    longest_sequence = 0
    num_set = set(nums)
    # assume current is min in the longest list
    for num in nums:
        if (num - 1) not in num_set:
            current_sequent = 1
            current_num = num
            while (current_num + 1) in num_set:
                current_sequent += 1
                current_num = current_num + 1
            longest_sequence = max(current_sequent, longest_sequence)

    return longest_sequence


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive_sequence([1, 1, 2, 2, 3, 4]))

    print(longest_consecutive_sequence([100]))
    print(longest_consecutive_sequence([100, 102, 104]))

    """
        EXPECTED OUTPUT:
        ----------------
        4

    """

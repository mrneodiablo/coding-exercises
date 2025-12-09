"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3

"""

from typing import List

# assume max long is len(nums)
# biggest is max of nums
# smallest is min of nums
# [0, 3, 7, 2, ]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using sort approach
        # if len(nums) < 1:
        #     return 0
        # nums.sort()
        # max_length = 1
        # tmp_max = 1
        # for i in range(len(nums) - 1):
        #     if nums[i] + 1 == nums[i + 1]:
        #         tmp_max += 1

        #     if nums[i] + 1 < nums[i + 1]:
        #         tmp_max = 1

        #     max_length = max(max_length, tmp_max)

        # return max_length

        # using hashtable approach
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in num_set:
                current_num = n
                tmp_longest = 1

                while current_num + 1 in num_set:
                    tmp_longest += 1
                    current_num += 1

                longest = max(longest, tmp_longest)
        return longest


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example 1 from problem
    test_1 = [100, 4, 200, 1, 3, 2]
    result_1 = solution.longestConsecutive(test_1)
    print(f"Test 1 - Input: {test_1}")
    print(f"Test 1 - Output: {result_1}")
    print("Test 1 - Expected: 4 (sequence: [1,2,3,4])")
    print(f"Test 1 - Correct: {result_1 == 4}")
    print()

    # Test case 2: Example 2 from problem
    test_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result_2 = solution.longestConsecutive(test_2)
    print(f"Test 2 - Input: {test_2}")
    print(f"Test 2 - Output: {result_2}")
    print("Test 2 - Expected: 9 (sequence: [0,1,2,3,4,5,6,7,8])")
    print(f"Test 2 - Correct: {result_2 == 9}")
    print()

    # Test case 3: Example 3 from problem
    test_3 = [1, 0, 1, 2]
    result_3 = solution.longestConsecutive(test_3)
    print(f"Test 3 - Input: {test_3}")
    print(f"Test 3 - Output: {result_3}")
    print("Test 3 - Expected: 3 (sequence: [0,1,2])")
    print(f"Test 3 - Correct: {result_3 == 3}")
    print()

"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # Create frequency buckets (index = frequency,
        # value = list of numbers with that frequency)
        # Maximum possible frequency is len(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        # Place numbers in their frequency buckets
        for num, freq in counter.items():
            freq_buckets[freq].append(num)

        # Collect the k most frequent elements
        # starting from highest frequency
        result = []
        for freq in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


# nums_test = [-1, -1]
nums_test = [1, 1, 1, 2, 2, 3]

k_test = 2
# [1,2]

solution = Solution()
print(solution.topKFrequent(nums_test, k_test))

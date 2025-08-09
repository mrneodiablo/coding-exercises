"""
Given an integer array nums and an integer k,
return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Old approach: 2 loop
        # first = 0
        # if k >= len(nums):
        #     last = len(nums)-1
        # else:
        #     last = first + k

        # while last < len(nums):
        #     checker = {}
        #     for i in range(first,last+1):
        #         if checker.get(nums[i]):
        #             return True
        #         checker[nums[i]] = [i]

        #     first += 1
        #     last += 1
        # return False

        # Alternative: Hash Map approach (commented out)
        # hset = {}
        # for i in range(len(nums)):
        #     if nums[i] in hset and abs(i - hset[nums[i]]) <= k:
        #         return True
        #     else:
        #         hset[nums[i]] = i
        # return False

        # Alternative: Implement Sliding
        # Window after this line don't change anything above

        # Sliding Window Approach
        if k == 0:
            return False

        window_set = set()
        left = 0

        for right in range(len(nums)):
            # If window size exceeds k+1, shrink from left
            if right - left > k:
                window_set.remove(nums[left])
                left += 1

            # Check if current element already exists in window
            if nums[right] in window_set:
                return True

            # Add current element to window
            window_set.add(nums[right])

        return False


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic example from problem - duplicates within range
    test1_nums = [1, 2, 3, 1]
    test1_k = 3
    result1 = solution.containsNearbyDuplicate(test1_nums, test1_k)
    print("(Expected: True)")
    print("Explanation: nums[0]=1 and nums[3]=1, distance=|3-0|=3 <= k=3")

    # Test Case 2: Duplicates very close together
    test2_nums = [1, 0, 1, 1]
    test2_k = 1
    result2 = solution.containsNearbyDuplicate(test2_nums, test2_k)
    print("(Expected: True)")
    print("Explanation: nums[2]=1 and nums[3]=1, distance=|3-2|=1 <= k=1")

    # Test Case 3: Duplicates exist but too far apart
    test3_nums = [1, 2, 3, 1, 2, 3]
    test3_k = 2
    result3 = solution.containsNearbyDuplicate(test3_nums, test3_k)
    print(f"\nTest 3: nums={test3_nums}, k={test3_k} -> {result3} " +
          "(Expected: False)")
    print("Explanation: Closest duplicates are nums[0]=1 and nums[3]=1, " +
          "distance=3 > k=2")

    # Test Case 4: No duplicates at all
    test4_nums = [99, 99]
    test4_k = 1
    result4 = solution.containsNearbyDuplicate(test4_nums, test4_k)
    print(f"\nTest 4: nums={test4_nums}, k={test4_k} -> {result4} " +
          "(Expected: True)")
    print("Explanation: nums[0]=99 and nums[1]=99, distance=|1-0|=1 <= k=1")

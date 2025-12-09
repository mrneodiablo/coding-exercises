"""
2859. Sum of Values at Indices With K Set Bits
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums
whose corresponding indices have exactly
k set bits in their binary representation.

The set bits in an integer are
the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
Example 1:
Input: nums = [5,10,1,5,2], k = 1
Output: 13
Explanation: The binary representation of the indices are:
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002
Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
Hence, the answer is nums[1] + nums[2] + nums[4] = 13.

Example 2:
Input: nums = [4,3,2,1], k = 2
Output: 1
Explanation: The binary representation of the indices are:
0 = 002
1 = 012
2 = 102
3 = 112
Only index 3 has k = 2 set bits in its binary representation.
Hence, the answer is nums[3] = 1.
"""

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        output = 0
        dp = [0] * len(nums)
        for i, v in enumerate(nums):
            dp[i] = dp[i // 2] + (i & 1)

            if dp[i] == k:
                output += v

        return output


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: k = 1 set bit
    nums1 = [5, 10, 1, 5, 2]
    k1 = 1
    result1 = solution.sumIndicesWithKSetBits(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Result: {result1}")
    print("Expected: 13")
    print("Explanation:")
    print("  Index 0 (0000) = 0 set bits")
    print("  Index 1 (0001) = 1 set bit ✓ → nums[1] = 10")
    print("  Index 2 (0010) = 1 set bit ✓ → nums[2] = 1")
    print("  Index 3 (0011) = 2 set bits")
    print("  Index 4 (0100) = 1 set bit ✓ → nums[4] = 2")
    print("  Sum = 10 + 1 + 2 = 13")
    print()

    # Test case 2: k = 2 set bits
    nums2 = [4, 3, 2, 1]
    k2 = 2
    result2 = solution.sumIndicesWithKSetBits(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Result: {result2}")
    print("Expected: 1")
    print("Explanation:")
    print("  Index 0 (00) = 0 set bits")
    print("  Index 1 (01) = 1 set bit")
    print("  Index 2 (10) = 1 set bit")
    print("  Index 3 (11) = 2 set bits ✓ → nums[3] = 1")
    print("  Sum = 1")
    print()

    # Test case 3: k = 0 (only index 0)
    nums3 = [7, 2, 3, 4, 5]
    k3 = 0
    result3 = solution.sumIndicesWithKSetBits(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Result: {result3}")
    print("Expected: 7")
    print("Explanation:")
    print("  Index 0 (000) = 0 set bits ✓ → nums[0] = 7")
    print("  Index 1 (001) = 1 set bit")
    print("  Index 2 (010) = 1 set bit")
    print("  Index 3 (011) = 2 set bits")
    print("  Index 4 (100) = 1 set bit")
    print("  Sum = 7")
    print()

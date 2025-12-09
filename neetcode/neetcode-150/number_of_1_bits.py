"""
191. Number of 1 Bits
Given a positive integer n, write a function that returns
the number of set bits in its binary representation
(also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:

The input binary string 10000000 has a total of one set bit.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:

            if n & 1 == 1:
                count += 1
            n >>= 1

        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Multiple 1 bits
    n1 = 11
    result1 = solution.hammingWeight(n1)
    print(f"Test 1: n={n1}")
    print(f"Binary: {bin(n1)} = {bin(n1)[2:]}")
    print(f"Result: {result1}")
    print("Expected: 3 (three 1s in 1011)")
    print()

    # Test case 2: Single 1 bit
    n2 = 128
    result2 = solution.hammingWeight(n2)
    print(f"Test 2: n={n2}")
    print(f"Binary: {bin(n2)} = {bin(n2)[2:]}")
    print(f"Result: {result2}")
    print("Expected: 1 (one 1 in 10000000)")
    print()

    # Test case 3: All 1 bits (max value for 8 bits)
    n3 = 255
    result3 = solution.hammingWeight(n3)
    print(f"Test 3: n={n3}")
    print(f"Binary: {bin(n3)} = {bin(n3)[2:]}")
    print(f"Result: {result3}")
    print("Expected: 8 (eight 1s in 11111111)")
    print()

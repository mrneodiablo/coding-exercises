"""
Given a 1-indexed array of integers numbers
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and
numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9.
Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6.
Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1.
Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if (target - numbers[left]) < numbers[right]:
                right -= 1
            elif (target - numbers[left]) > numbers[right]:
                left += 1
            else:
                return [left + 1, right + 1]
        return None


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example from problem description
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: numbers={numbers1}, target={target1}")
    print(f"Expected: [1, 2], Got: {solution.twoSum(numbers1, target1)}")
    print()

    # Test case 2: Another example from problem description
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"Test 2: numbers={numbers2}, target={target2}")
    print(f"Expected: [1, 3], Got: {solution.twoSum(numbers2, target2)}")
    print()

    # Test case 3: Negative numbers
    numbers3 = [-1, 0]
    target3 = -1
    print(f"Test 3: numbers={numbers3}, target={target3}")
    print(f"Expected: [1, 2], Got: {solution.twoSum(numbers3, target3)}")
    print()

    # Test case 4: Larger array with solution at the ends
    numbers4 = [1, 2, 3, 4, 4, 9, 56, 90]
    target4 = 91
    print(f"Test 4: numbers={numbers4}, target={target4}")
    print(f"Expected: [1, 8], Got: {solution.twoSum(numbers4, target4)}")
    print()

    # Test case 5: Negative and positive numbers
    numbers5 = [-3, -1, 0, 2, 3]
    target5 = 0
    print(f"Test 5: numbers={numbers5}, target={target5}")
    print(f"Expected: [1, 5], Got: {solution.twoSum(numbers5, target5)}")
    print()

    # Test case 6: Same numbers (duplicates)
    numbers6 = [1, 2, 3, 4, 4, 5]
    target6 = 8
    print(f"Test 6: numbers={numbers6}, target={target6}")
    print(f"Expected: [3, 6], Got: {solution.twoSum(numbers6, target6)}")
    print()

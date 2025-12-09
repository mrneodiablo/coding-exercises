"""
Given an integer array nums,
return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and
the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

"""

from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # the idea is fixed i. and check j k , with j and k is dynamic
        # for j and k if we build checker as
        # dict that will take n^3 time complexity
        # let dev with dict first
        # result = []
        # check_result = {}
        # for i in range(len(nums) - 2):
        #     checker = {}
        #     target = 0 - nums[i]
        #     for temp in range(i + 1, len(nums)):
        #         if not checker.get(nums[temp]):
        #             checker[nums[temp]] = [temp]
        #         else:
        #             checker[nums[temp]].append(temp)

        #         second_number = checker.get(target - nums[temp])
        #         if second_number and second_number[0] != temp:
        #             tmp = [nums[i], target - nums[temp], nums[temp]]
        #             tmp.sort()
        #             if not check_result.get(str(tmp)):
        #                 check_result[str(tmp)] = 1
        #                 result.append(tmp)
        # return result

        # using 2 pointers and sort the list first, the idea is after sort,
        # we should remove doublicated number
        # Skip duplicate values for the first element
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if target - nums[j] > nums[k]:
                    j += 1
                elif target - nums[j] < nums[k]:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return result


class TestFunctions(unittest.TestCase):

    def test_case_1(self):
        solution = Solution()
        nums_test = [-1, 0, 1, 2, -1, -4]
        expect = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(
            solution.threeSum(nums_test),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2(self):
        solution = Solution()
        nums_test = [0, 1, 1]
        expect = []
        self.assertEqual(
            solution.threeSum(nums_test),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3(self):
        solution = Solution()
        nums_test = [0, 0, 0]
        expect = [[0, 0, 0]]
        self.assertEqual(
            solution.threeSum(nums_test),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

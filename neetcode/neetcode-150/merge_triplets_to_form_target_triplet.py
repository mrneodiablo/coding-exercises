"""
Docstring for neetcode.neetcode-150.merge_triplets_to_form_target_triplet

1899. Merge Triplets to Form Target Triplet
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.



Example 1:

Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.
Example 2:

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
Example 3:

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
"""

from typing import List
import unittest


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        found = [False, False, False]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                # remove all triplet having any value greater than target
                continue

            if t[0] == target[0]:
                found[0] = True
            if t[1] == target[1]:
                found[1] = True
            if t[2] == target[2]:
                found[2] = True

        return all(found)


class TestFunctions(unittest.TestCase):

    def test_case_1_can_form_target(self):
        """Test case where target can be formed by merging triplets"""
        solution = Solution()
        triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
        target = [2, 7, 5]
        expect = True
        self.assertEqual(
            solution.mergeTriplets(triplets, target),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_cannot_form_target(self):
        """Test case where target cannot be formed - missing value"""
        solution = Solution()
        triplets = [[3, 4, 5], [4, 5, 6]]
        target = [3, 2, 5]
        expect = False
        self.assertEqual(
            solution.mergeTriplets(triplets, target),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_multiple_merges(self):
        """Test case requiring multiple merge operations"""
        solution = Solution()
        triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
        target = [5, 5, 5]
        expect = True
        self.assertEqual(
            solution.mergeTriplets(triplets, target),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_4_missing_value(self):
        """Test case where a target value doesn't exist in any triplet"""
        solution = Solution()
        triplets = [[1, 3, 1]]
        target = [1, 3, 2]
        expect = False
        self.assertEqual(
            solution.mergeTriplets(triplets, target),
            expect,
            f"incorrect, expect is {expect} - cannot reach target[2]=2",
        )

    def test_case_5_missing_value(self):
        solution = Solution()
        triplets = [[3, 1, 7], [1, 5, 10]]
        target = [3, 5, 7]
        expect = False
        self.assertEqual(
            solution.mergeTriplets(triplets, target),
            expect,
            f"incorrect, expect is {expect} ",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

"""
39. Combination Sum
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates
where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of
at least one of the chosen numbers is different.

The test cases are generated such that the number
of unique combinations that sum up to target is
less than 150 combinations for the given input.


Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7.
 Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

"""

from typing import List
import unittest


class Solution:
    def combinationSum(self,
                       candidates: List[int],
                       target: int) -> List[List[int]]:
        output = []
        candidates = sorted(candidates)

        def backtracking(b_candidates, b_target, current_combination, start):
            for i in range(start, len(b_candidates)):
                if b_candidates[i] < b_target:
                    backtracking(
                        b_candidates,
                        b_target - b_candidates[i],
                        current_combination + [b_candidates[i]], i
                    )
                if b_candidates[i] == b_target:
                    output.append(current_combination + [b_candidates[i]])
                if b_candidates[i] > b_target:
                    return

        backtracking(candidates, target, [], 0)
        return output


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description"""
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        result = self.solution.combinationSum(candidates, target)

        # Sort both result and expected for comparison
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]

        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_run_2(self):
        """Test case 2: Multiple combinations with small numbers"""
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        result = self.solution.combinationSum(candidates, target)

        # Sort both result and expected for comparison
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]

        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_run_3(self):
        """Test case 3: No solution possible"""
        candidates = [2]
        target = 1
        expected = []
        result = self.solution.combinationSum(candidates, target)

        self.assertEqual(result, expected)


def manual_test():
    """Manual test function for combination sum"""
    solution = Solution()

    print("==================================================")
    print("Test 1: Example from problem description")
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[2, 2, 3], [7]]
    result1 = solution.combinationSum(candidates1, target1)
    result1_sorted = [sorted(combo) for combo in result1]
    expected1_sorted = [sorted(combo) for combo in expected1]

    print(f"  Input: candidates = {candidates1}, target = {target1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    passed1 = sorted(result1_sorted) == sorted(expected1_sorted)
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    print("Test 2: Multiple combinations with small numbers")
    candidates2 = [2, 3, 5]
    target2 = 8
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result2 = solution.combinationSum(candidates2, target2)
    result2_sorted = [sorted(combo) for combo in result2]
    expected2_sorted = [sorted(combo) for combo in expected2]

    print(f"  Input: candidates = {candidates2}, target = {target2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    passed2 = sorted(result2_sorted) == sorted(expected2_sorted)
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    print("Test 3: No solution possible")
    candidates3 = [2]
    target3 = 1
    expected3 = []
    result3 = solution.combinationSum(candidates3, target3)

    print(f"  Input: candidates = {candidates3}, target = {target3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    print("Test 4: Single element that equals target")
    candidates4 = [1]
    target4 = 2
    expected4 = [[1, 1]]
    result4 = solution.combinationSum(candidates4, target4)
    result4_sorted = [sorted(combo) for combo in result4]
    expected4_sorted = [sorted(combo) for combo in expected4]

    print(f"  Input: candidates = {candidates4}, target = {target4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    passed4 = sorted(result4_sorted) == sorted(expected4_sorted)
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    print("Test 5: Larger numbers requiring fewer combinations")
    candidates5 = [7, 3, 2]
    target5 = 18
    expected_count5 = (
        4
    )
    result5 = solution.combinationSum(candidates5, target5)

    print(f"  Input: candidates = {candidates5}, target = {target5}")
    print(f"  Expected combinations count: >= {expected_count5}")
    print(f"  Got combinations count: {len(result5)}")
    print(f"  Sample results: {result5[:3] if result5 else []}...")
    passed5 = len(result5) >= expected_count5
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    unittest.main(verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("Manual Test Results:")
    print("=" * 50)

    # Run manual tests
    manual_test()

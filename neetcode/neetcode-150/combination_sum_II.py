"""
40. Combination Sum II
Given a collection of candidate numbers (candidates)
and a target number (target),
find all unique combinations in candidates where
the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

from typing import List
import unittest


class Solution:
    def combinationSum2(self,
                        candidates: List[int],
                        target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort để có thể skip duplicates

        def backtrack(
            start: int, current_combination: List[int], remaining_target: int
        ):
            # Base case: nếu target = 0, tìm được combination hợp lệ
            if remaining_target == 0:
                result.append(current_combination)
                return

            # Base case: nếu target < 0, không hợp lệ
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates: nếu candidates[i] == candidates[i-1]
                # và i > start (không phải first element trong level này)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Nếu candidate hiện tại > remaining target thì break
                # (vì array đã được sort)
                if candidates[i] > remaining_target:
                    break

                # Recursive call với combination
                # mới = current + [candidates[i]]
                # start = i+1 (mỗi element chỉ dùng 1 lần)
                backtrack(
                    i + 1,
                    current_combination + [candidates[i]],
                    remaining_target - candidates[i],
                )

        backtrack(0, [], target)
        return result


class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description"""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        result = self.solution.combinationSum2(candidates, target)
        # Sort both lists for comparison (order doesn't matter)
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_run_2(self):
        """Test case 2: Multiple duplicates with small target"""
        candidates = [2, 5, 2, 1, 2]
        target = 5
        expected = [[1, 2, 2], [5]]
        result = self.solution.combinationSum2(candidates, target)
        # Sort both lists for comparison (order doesn't matter)
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]
        self.assertEqual(sorted(result_sorted), sorted(expected_sorted))

    def test_run_3(self):
        """Test case 3: No solution possible"""
        candidates = [1]
        target = 2
        expected = []
        result = self.solution.combinationSum2(candidates, target)
        self.assertEqual(result, expected)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("COMBINATION SUM II - TEST CASES")
    print("=" * 50)

    # Test 1: Example from problem description
    print("Test 1: Example from problem description")
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    expected1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    result1 = solution.combinationSum2(candidates1, target1)
    result1_sorted = [sorted(combo) for combo in result1]
    expected1_sorted = [sorted(combo) for combo in expected1]

    print(f"  Input: candidates = {candidates1}, target = {target1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    passed1 = sorted(result1_sorted) == sorted(expected1_sorted)
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Multiple duplicates with small target
    print("Test 2: Multiple duplicates with small target")
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    expected2 = [[1, 2, 2], [5]]
    result2 = solution.combinationSum2(candidates2, target2)
    result2_sorted = [sorted(combo) for combo in result2]
    expected2_sorted = [sorted(combo) for combo in expected2]

    print(f"  Input: candidates = {candidates2}, target = {target2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    passed2 = sorted(result2_sorted) == sorted(expected2_sorted)
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: No solution possible
    print("Test 3: No solution possible")
    candidates3 = [1]
    target3 = 2
    expected3 = []
    result3 = solution.combinationSum2(candidates3, target3)

    print(f"  Input: candidates = {candidates3}, target = {target3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Single element that equals target
    print("Test 4: Single element that equals target")
    candidates4 = [1, 1, 1, 1]
    target4 = 2
    expected4 = [[1, 1]]
    result4 = solution.combinationSum2(candidates4, target4)
    result4_sorted = [sorted(combo) for combo in result4]
    expected4_sorted = [sorted(combo) for combo in expected4]

    print(f"  Input: candidates = {candidates4}, target = {target4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    passed4 = sorted(result4_sorted) == sorted(expected4_sorted)
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: Larger example with more duplicates
    print("Test 5: Larger example with more duplicates")
    candidates5 = [1, 1, 1, 1, 1, 1, 1]
    target5 = 3
    expected5 = [[1, 1, 1]]
    result5 = solution.combinationSum2(candidates5, target5)
    result5_sorted = [sorted(combo) for combo in result5]
    expected5_sorted = [sorted(combo) for combo in expected5]

    print(f"  Input: candidates = {candidates5}, target = {target5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    passed5 = sorted(result5_sorted) == sorted(expected5_sorted)
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    # manual_test()

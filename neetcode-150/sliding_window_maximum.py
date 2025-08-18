import collections
from typing import List

"""
🎯 WHEN TO USE DEQUE: Key Patterns & Signals

The deque pattern is perfect when you need to:
1. Track extremes (min/max) in a sliding window
2. Maintain candidates in sorted order while elements enter/leave
3. Efficiently remove elements from both ends

🔍 PROBLEM SIGNALS THAT SUGGEST DEQUE:
"""


class OptimizedSolution:
    """
    Cleaner version of the deque approach with better variable names
    Still O(n) time but much easier to understand
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque stores indices of elements in decreasing order of their values
        # Front of deque always contains index of maximum element
        # in current window
        q = collections.deque()
        result = []

        for i in range(len(nums)):
            # Remove indices whose values are smaller than current value
            # (they can never be maximum while current value is in window)
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add current index to deque
            q.append(i)

            # Remove indices that are outside current window
            # Window starts at (i - k + 1)
            if q[0] < i - k + 1:
                q.popleft()

            # If we have a complete window, add maximum to result
            if i >= k - 1:  # We have at least k elements
                result.append(nums[q[0]])

        return result


class SuperOptimizedSolution:
    """
    Further optimized version with early termination
    and better memory usage
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        if k == 1:
            return nums

        if k >= len(nums):
            return [max(nums)]

        # Use deque to store indices in decreasing order of values
        window = collections.deque()
        result = []

        for i, num in enumerate(nums):
            # Remove indices of elements smaller than current element
            # They can never be maximum while current element is in window
            while window and nums[window[-1]] < num:
                window.pop()

            # Add current index
            window.append(i)

            # Remove indices outside current window
            while window[0] <= i - k:
                window.popleft()

            # Add maximum to result when window is complete
            if i >= k - 1:
                result.append(nums[window[0]])

        return result


class MonotonicDequeSolution:
    """
    Most optimized version with detailed explanations of
    monotonic deque concept
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic Deque Approach:
        - Maintain a deque of indices in decreasing order of their values
        - This creates a "monotonic decreasing deque"
        - Front always contains the maximum element's index
        Time: O(n) - each element added and removed at most once
        Space: O(k) - deque size never exceeds window size
        """
        n = len(nums)
        if n == 0 or k == 0:
            return []

        # Edge cases for efficiency
        if k == 1:
            return nums
        if k >= n:
            return [max(nums)]

        # Monotonic decreasing deque storing indices
        dq = collections.deque()
        result = []

        for i in range(n):
            # Maintain monotonic property: remove smaller elements
            # Why? If nums[j] < nums[i] and j < i, then nums[j] can never
            # be maximum while nums[i] is still in any future window
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Remove elements outside current window [i-k+1, i]
            if dq[0] <= i - k:
                dq.popleft()

            # Add result when we have a complete window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Original complex solution (for comparison)
class OriginalSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out.append(nums[d[0]])
        return out


def test_optimized_solution():
    """
    4 focused test cases for all OptimizedSolution versions
    """
    print("🧪 Testing All Optimized Solutions - 4 Key Test Cases")
    print("=" * 60)

    # Test all three optimized solutions
    solutions = [
        ("OptimizedSolution", OptimizedSolution()),
        ("SuperOptimizedSolution", SuperOptimizedSolution()),
        ("MonotonicDequeSolution", MonotonicDequeSolution())
    ]

    test_cases = [
        {
            "name": "Basic sliding window example",
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
            "expected": [3, 3, 5, 5, 6, 7]
        },
        {
            "name": "Window size of 1 (edge case)",
            "nums": [1, -1, 3, -3, 5],
            "k": 1,
            "expected": [1, -1, 3, -3, 5]
        },
        {
            "name": "Decreasing array (worst case)",
            "nums": [9, 7, 5, 3, 1],
            "k": 3,
            "expected": [9, 7, 5]
        },
        {
            "name": "Array with negative numbers",
            "nums": [-7, -8, 7, 5, 7, 1, 6, 0],
            "k": 4,
            "expected": [7, 7, 7, 7, 7]
        }
    ]

    for sol_name, solution in solutions:
        print(f"\n🔍 Testing {sol_name}")
        print("-" * 40)

        passed = 0
        total = len(test_cases)

        for i, test_case in enumerate(test_cases, 1):
            nums = test_case["nums"]
            k = test_case["k"]
            expected = test_case["expected"]
            name = test_case["name"]

            try:
                result = solution.maxSlidingWindow(nums, k)

                if result == expected:
                    print(f"  ✅ Test {i}: PASSED - {name}")
                    passed += 1
                else:
                    print(f"  ❌ Test {i}: FAILED - {name}")
                    print(f"     Expected: {expected}")
                    print(f"     Got:      {result}")
            except Exception as e:
                print(f"  💥 Test {i}: ERROR - {name}")
                print(f"     Error: {str(e)}")

        print(f"  📊 {sol_name}: {passed}/{total} tests passed")

        if passed == total:
            print(f"  🎉 {sol_name} works perfectly!")
        else:
            print(f"  � {sol_name} needs fixes.")

    print(f"\n{'='*60}")
    print("� OPTIMIZATION COMPARISON:")
    print("• OptimizedSolution: Clean and readable")
    print("• SuperOptimizedSolution: Added edge case handling")
    print("• MonotonicDequeSolution: Most detailed with theory")
    print("• All have O(n) time complexity and O(k) space complexity")


if __name__ == "__main__":
    test_optimized_solution()

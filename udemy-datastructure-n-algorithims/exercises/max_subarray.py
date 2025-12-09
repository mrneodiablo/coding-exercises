def max_subarray(nums):
    """
    Kadane's algorithm to find maximum subarray sum in O(n) time.

        The algorithm works by:
        1. Keep track of the maximum sum ending at current position
        2. At each element, decide whether to extend
        the previous subarray or start a new one
        3. Choose to start new subarray
        if current element alone is better than extending
        4. Keep track of the overall maximum seen so far

        Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        - At index 0: current_sum = -2, max_sum = -2
        - At index 1: current_sum = max(1, -2+1) = 1, max_sum = 1
        - At index 2: current_sum = max(-3, 1-3) = -2, max_sum = 1
        - At index 3: current_sum = max(4, -2+4) = 4, max_sum = 4
        - And so on...
    """
    max_sum_array = float("-inf")
    summarize = 0
    for i in range(len(nums)):
        if (summarize + nums[i]) > nums[i]:
            summarize = summarize + nums[i]
        else:
            summarize = nums[i]
        max_sum_array = max(max_sum_array, summarize)
    return max_sum_array


# Example 1: Simple case with positive and negative numbers
input_case_1 = [1, 2, 3, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)

# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2)

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3)


# # """
# #     EXPECTED OUTPUT:
# #     ----------------
# #     Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# #     Result: 6
# #     Example 2: Input: [1, 2, 3, -4, 5, 6]
# #     Result: 13
# #     Example 3: Input: [-1, -2, -3, -4, -5]
# #     Result: -1

# # """

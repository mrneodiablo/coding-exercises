"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.



Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        current_summarization = 0
        for num in nums:
            current_summarization += num

        # to sum from 0-10 without for loop we use (max*(max+1))/2
        # then we minus for current_summarization
        return ((max_num * (max_num + 1)) // 2) - current_summarization


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # GIẢI THÍCH CÔNG THỨC
    print("=" * 70)
    print("GIẢI THÍCH CÔNG THỨC: Tìm số thiếu bằng TỔNG GAUSS")
    print("=" * 70)

    print("\n🎯 BÀI TOÁN:")
    print("  • Có mảng n số, chứa các số KHÁC NHAU trong khoảng [0, n]")
    print("  • Thiếu đúng 1 số trong khoảng đó")
    print("  • Tìm số thiếu\n")

    print("💡 Ý TƯỞNG:")
    print("  Tổng đầy đủ - Tổng hiện tại = Số thiếu\n")

    print("📐 CÔNG THỨC GAUSS - Tổng từ 0 đến n:")
    print("  S = 0 + 1 + 2 + 3 + ... + n = n × (n + 1) / 2\n")

    print("🔍 CHỨNG MINH công thức:")
    print("  Ví dụ: Tính tổng từ 0 đến 5")
    print("  S = 0 + 1 + 2 + 3 + 4 + 5")
    print("  S = 5 + 4 + 3 + 2 + 1 + 0  (viết ngược lại)")
    print("  ─────────────────────────")
    print("  2S = 5 + 5 + 5 + 5 + 5 + 5 = 6 × 5 = 30")
    print("  → S = 30 / 2 = 15")
    print("  → S = 6 × 5 / 2 = n × (n + 1) / 2  (với n = 5)")
    print()

    print("📝 VÍ DỤ CỤ THỂ:")
    demo_nums = [0, 1, 3, 4]
    print(f"  Mảng: {demo_nums}")
    print(f"  → n = {len(demo_nums)} (có 4 số)")
    print(f"  → Khoảng đúng: [0, 1, 2, 3, 4] (từ 0 đến {len(demo_nums)})")
    print()

    n = len(demo_nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(demo_nums)
    missing = expected_sum - actual_sum

    print("  BƯỚC 1: Tính tổng ĐẦY ĐỦ (nếu không thiếu số nào)")
    print("    Tổng đầy đủ = n × (n + 1) / 2")
    print(f"                = {n} × ({n} + 1) / 2")
    print(f"                = {n} × {n + 1} / 2")
    print(f"                = {n * (n + 1)} / 2")
    print(f"                = {expected_sum}")
    print()

    print("  BƯỚC 2: Tính tổng HIỆN TẠI (trong mảng)")
    print(f"    Tổng hiện tại = 0 + 1 + 3 + 4 = {actual_sum}")
    print()

    print("  BƯỚC 3: Tìm số thiếu")
    print("    Số thiếu = Tổng đầy đủ - Tổng hiện tại")
    print(f"             = {expected_sum} - {actual_sum}")
    print(f"             = {missing}")
    print(f"    ✅ Đáp án: {missing}")
    print()

    print("🚀 ƯU ĐIỂM:")
    print("  • Time: O(n) - chỉ duyệt 1 lần")
    print("  • Space: O(1) - không dùng thêm bộ nhớ")
    print("  • Không cần sắp xếp, không cần hash table")
    print("=" * 70)
    print()

    # Test case 1: Missing number in the middle
    nums1 = [3, 0, 1]
    result1 = solution.missingNumber(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Result: {result1}")
    print("Expected: 2")
    print("Explanation: n=3, range [0,3], missing 2")
    print()

    # Test case 2: Missing the last number
    nums2 = [0, 1]
    result2 = solution.missingNumber(nums2)
    print(f"Test 2: nums={nums2}")
    print(f"Result: {result2}")
    print("Expected: 2")
    print("Explanation: n=2, range [0,2], missing 2")
    print()

    # Test case 3: Larger array with missing number
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    result3 = solution.missingNumber(nums3)
    print(f"Test 3: nums={nums3}")
    print(f"Result: {result3}")
    print("Expected: 8")
    print("Explanation: n=9, range [0,9], missing 8")
    print()

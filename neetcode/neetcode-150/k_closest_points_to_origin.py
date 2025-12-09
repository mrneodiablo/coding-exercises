"""
K Closest Points to Origin
Given an array of points where points[i] = [xi, yi]
represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane
is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order.
The answer is guaranteed to be unique
(except for the order that it is in).
"""

from math import sqrt
from typing import List
import heapq


class Solution:
    def kClosest(self,
                 points_data: List[List[int]],
                 k: int) -> List[List[int]]:
        max_heap_data = []
        for x, y in points_data:
            distance = x**2 + y**2
            if len(max_heap_data) < k:
                heapq.heappush(max_heap_data, (-distance, [x, y]))
            elif distance < -max_heap_data[0][0]:
                heapq.heapreplace(max_heap_data, (-distance, [x, y]))
        return [point for _, point in max_heap_data]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic example with k=1
    points1 = [[1, 3], [-2, 2]]
    k1 = 1
    result1 = solution.kClosest(points1, k1)
    print(f"Test 1: points={points1}, k={k1}")
    print(f"Result: {result1}")
    print("Expected: [[-2, 2]] (distance ≈ 2.83 vs 3.16)")
    print()

    # Test case 2: Multiple points with k=2
    points2 = [[3, 3], [5, -1], [-2, 4]]
    k2 = 2
    result2 = solution.kClosest(points2, k2)
    print(f"Test 2: points={points2}, k={k2}")
    print(f"Result: {result2}")
    print(
        "Expected: [[3, 3], [-2, 4]] in any order "
        "(distances ≈ 4.24, 4.47)"
    )
    print()

    # Test case 3: Origin point included
    points3 = [[0, 1], [1, 0], [0, 0]]
    k3 = 2
    result3 = solution.kClosest(points3, k3)
    print(f"Test 3: points={points3}, k={k3}")
    print(f"Result: {result3}")
    print(
        "Expected: [[0, 0], [0, 1]] or [[0, 0], [1, 0]] "
        "(distances 0, 1, 1)"
    )
    print()

    # GIẢI THÍCH: Tại sao không cần sqrt?
    print("=" * 60)
    print(
        "GIẢI THÍCH: Tại sao x² + y² cho kết quả giống √(x² + y²)?"
    )
    print("=" * 60)

    # Ví dụ: So sánh 3 điểm
    points = [[1, 1], [2, 2], [3, 0]]
    print(f"\nCho 3 điểm: {points}")
    print("\nCách 1: Dùng SQRT (căn bậc 2)")
    for p in points:
        dist_sqrt = sqrt(p[0] ** 2 + p[1] ** 2)
        print(
            f"  {p}: √({p[0]}² + {p[1]}²) = "
            f"√{p[0]**2 + p[1]**2} = {dist_sqrt:.3f}"
        )

    print("\nCách 2: Chỉ dùng x² + y² (KHÔNG căn)")
    for p in points:
        dist_squared = p[0] ** 2 + p[1] ** 2
        print(f"  {p}: {p[0]}² + {p[1]}² = {dist_squared}")

    print("\nThứ tự sắp xếp:")
    with_sqrt = sorted(points, key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))
    without_sqrt = sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)
    print(f"  Với sqrt:    {with_sqrt}")
    print(f"  Không sqrt:  {without_sqrt}")
    print("  => KẾT QUẢ GIỐNG NHAU! ✓")

    print("\nLÝ DO:")
    print("  • Hàm f(x) = √x là hàm TĂNG (monotonic increasing)")
    print("  • Nếu a < b thì √a < √b")
    print("  • Ví dụ: 2 < 8 → √2 < √8 (1.41 < 2.83)")
    print("  • Vậy nên: x₁² + y₁² < x₂² + y₂²")
    print("           ↕ (tương đương)")
    print("           √(x₁² + y₁²) < √(x₂² + y₂²)")
    print("\n  => Không cần tính sqrt, tiết kiệm thời gian tính toán!")
    print("=" * 60)

    # GIẢI THÍCH 2: Tại sao KHÔNG dùng abs(x) + abs(y)?
    print("\n" + "=" * 60)
    print(
        "Tại sao KHÔNG dùng abs(x) + abs(y) (Manhattan distance)?"
    )
    print("=" * 60)

    test_points = [[3, 4], [5, 0], [1, 1]]
    print(f"\nCho 3 điểm: {test_points}\n")

    print(
        "EUCLIDEAN (đề bài yêu cầu) - khoảng cách đường chim bay:"
    )
    euclidean_results = []
    for p in test_points:
        dist = sqrt(p[0] ** 2 + p[1] ** 2)
        euclidean_results.append((p, dist))
        print(f"  {p}: √({p[0]}² + {p[1]}²) = {dist:.3f}")

    print("\nMANHATTAN - khoảng cách đi theo lưới (như taxi):")
    manhattan_results = []
    for p in test_points:
        dist = abs(p[0]) + abs(p[1])
        manhattan_results.append((p, dist))
        print(f"  {p}: |{p[0]}| + |{p[1]}| = {dist}")

    print("\n📊 THỨ TỰ SẮP XẾP:")
    euclidean_sorted = sorted(
        test_points, key=lambda p: p[0] ** 2 + p[1] ** 2
    )
    manhattan_sorted = sorted(
        test_points, key=lambda p: abs(p[0]) + abs(p[1])
    )

    print(f"  Euclidean:  {euclidean_sorted}")
    print(f"  Manhattan:  {manhattan_sorted}")
    print("  => KHÁC NHAU! ❌")

    print("\n🎯 VÍ DỤ CỤ THỂ:")
    print("  Điểm [3, 4]:")
    print("    • Euclidean: √(3² + 4²) = √25 = 5.0")
    print("    • Manhattan: |3| + |4| = 7")
    print("  Điểm [5, 0]:")
    print("    • Euclidean: √(5² + 0²) = √25 = 5.0")
    print("    • Manhattan: |5| + |0| = 5")
    print(
        "\n  Với Euclidean: [3,4] và [5,0] BẰNG NHAU (cùng 5.0)"
    )
    print("  Với Manhattan: [5,0] < [3,4] (5 < 7) - SAI!")

    print("\n💡 KẾT LUẬN:")
    print("  • Đề bài yêu cầu: Euclidean distance (đường thẳng)")
    print("  • Manhattan chỉ đúng khi đi theo lưới (như bàn cờ)")
    print("  • Công thức đúng: x² + y² (không cần sqrt)")
    print("=" * 60)

    # GIẢI THÍCH 3: Tại sao dùng MAX HEAP với size k?
    print("\n" + "=" * 60)
    print("Tại sao dùng MAX HEAP để tìm K điểm GẦN NHẤT?")
    print("=" * 60)

    demo_points = [[1, 1], [5, 5], [2, 2], [4, 4], [3, 3]]
    k_demo = 3
    print(f"\nVí dụ: Tìm {k_demo} điểm gần nhất từ {demo_points}")
    print(
        "Khoảng cách: [√2≈1.4, √50≈7.1, √8≈2.8, "
        "√32≈5.7, √18≈4.2]"
    )
    print("Đáp án: 3 điểm gần nhất là [1,1], [2,2], [3,3]\n")

    print("🔴 CÁCH 1: MIN HEAP (code hiện tại) - O(n log n)")
    print("  1. Thêm TẤT CẢ n điểm vào min heap")
    print("  2. Pop k lần để lấy k điểm nhỏ nhất")
    print("  → Phải lưu TẤT CẢ n điểm trong heap!")
    print("  → Space: O(n), Time: O(n log n)")

    print(
        "\n🟢 CÁCH 2: MAX HEAP với size k - "
        "O(n log k) - NHANH HƠN!"
    )
    print("  Ý tưởng: Chỉ giữ k điểm GẦN NHẤT, loại bỏ điểm XA")
    print()

    # Simulate max heap approach
    max_heap = []
    print("  Duyệt từng điểm:")
    for i, p in enumerate(demo_points):
        dist = p[0] ** 2 + p[1] ** 2

        if len(max_heap) < k_demo:
            heapq.heappush(max_heap, (-dist, p))
            print(
                f"  {i+1}. {p} (dist={dist:2d}): "
                f"Heap chưa đủ {k_demo} → THÊM VÀO"
            )
            print(f"     Heap: {[pt for _, pt in sorted(max_heap)]}")
        elif dist < -max_heap[0][0]:
            old_max = heapq.heapreplace(max_heap, (-dist, p))
            print(
                f"  {i+1}. {p} (dist={dist:2d}): "
                f"GẦN HƠN đỉnh heap ({int(-old_max[0])}) → THAY THẾ"
            )
            print(
                f"     Loại bỏ: {old_max[1]}, "
                f"Heap: {[pt for _, pt in sorted(max_heap)]}"
            )
        else:
            print(
                f"  {i+1}. {p} (dist={dist:2d}): "
                f"XA HƠN đỉnh heap ({int(-max_heap[0][0])}) → BỎ QUA"
            )
            print(
                f"     Heap không đổi: "
                f"{[pt for _, pt in sorted(max_heap)]}"
            )

    print(f"\n  ✅ KẾT QUẢ: {[pt for _, pt in max_heap]}")

    print("\n🎯 TẠI SAO DÙNG MAX HEAP?")
    print("  • Đỉnh heap = điểm XA NHẤT trong k điểm hiện tại")
    print("  • Điểm mới < đỉnh heap → điểm mới GẦN HƠN → THAY THẾ")
    print("  • Điểm mới > đỉnh heap → điểm mới XA HƠN → BỎ QUA")
    print("  • Luôn giữ k điểm GẦN NHẤT, loại bỏ điểm XA!")

    print("\n📊 SO SÁNH:")
    print(
        f"  • Min heap (n={len(demo_points)}): O(n log n) = "
        f"O({len(demo_points)} log {len(demo_points)}) ≈ "
        f"{len(demo_points) * 2.3}"
    )
    print(
        f"  • Max heap (k={k_demo}):           O(n log k) = "
        f"O({len(demo_points)} log {k_demo}) ≈ "
        f"{len(demo_points) * 1.6}"
    )
    print(
        "  • Khi n=1000, k=10: Min heap ≈10000 vs "
        "Max heap ≈3300 (3x nhanh hơn!)"
    )
    print("=" * 60)

    # GIẢI THÍCH 4: Python không có Max Heap - dùng số âm!
    print("\n" + "=" * 60)
    print("Python chỉ có MIN HEAP - làm thế nào tạo MAX HEAP?")
    print("=" * 60)

    print("\n🎯 TRICK: Dùng SỐ ÂM để biến Min Heap → Max Heap!\n")

    print("VÍ DỤ: Giữ 3 số LỚN NHẤT từ [1, 5, 2, 4, 3]")
    print(
        "(Tương tự: giữ 3 điểm GẦN NHẤT = "
        "giữ 3 khoảng cách NHỎ NHẤT)\n"
    )

    # Demo với min heap thông thường
    numbers = [1, 5, 2, 4, 3]
    k_num = 3

    print("❌ MIN HEAP thông thường (SAI):")
    min_heap = []
    for num in numbers:
        if len(min_heap) < k_num:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:  # Nếu số mới lớn hơn min
            heapq.heapreplace(min_heap, num)
        print(
            f"  Thêm {num}: heap = {sorted(min_heap)}, "
            f"đỉnh = {min_heap[0] if min_heap else 'N/A'}"
        )
    print(
        f"  → Lưu 3 số NHỎ NHẤT: {sorted(min_heap)} "
        "(SAI! Ta cần 3, 4, 5)\n"
    )

    print("✅ MAX HEAP bằng SỐ ÂM (ĐÚNG):")
    max_heap = []
    for num in numbers:
        if len(max_heap) < k_num:
            heapq.heappush(max_heap, -num)  # Push SỐ ÂM
            print(
                f"  Thêm {num} (push -{num}): "
                f"heap = {sorted([-x for x in max_heap])}, "
                f"đỉnh = {-max_heap[0] if max_heap else 'N/A'}"
            )
        elif num > -max_heap[0]:  # Nếu số mới LỚN HƠN đỉnh max
            old = heapq.heapreplace(max_heap, -num)
            print(
                f"  Thêm {num} (push -{num}): thay {-old}, "
                f"heap = {sorted([-x for x in max_heap])}, "
                f"đỉnh = {-max_heap[0]}"
            )
        else:
            print(f"  Thêm {num}: BỎ QUA (nhỏ hơn đỉnh {-max_heap[0]})")
    result = sorted([-x for x in max_heap])
    print(f"  → Lưu 3 số LỚN NHẤT: {result} (ĐÚNG! ✓)\n")

    print("💡 TẠI SAO HOẠT ĐỘNG?")
    print("  Min Heap: Đỉnh = phần tử NHỎ NHẤT")
    print("           [1, 2, 3] → đỉnh = 1")
    print()
    print("  Max Heap (dùng -x): Đỉnh = phần tử LỚN NHẤT")
    print("           Push -1, -2, -3 → heap = [-3, -2, -1]")
    print("           Đỉnh = -3 → số thực = -(-3) = 3 (LỚN NHẤT!) ✓")
    print()
    print("🔧 IMPLEMENTATION cho bài K Closest:")
    print("```python")
    print("max_heap = []")
    print("for x, y in points:")
    print("    dist = x**2 + y**2")
    print("    if len(max_heap) < k:")
    print("        heapq.heappush(max_heap, (-dist, [x, y]))  # Push -dist")
    print("    elif dist < -max_heap[0][0]:  # So sánh với -(-dist)")
    print("        heapq.heapreplace(max_heap, (-dist, [x, y]))")
    print("return [point for _, point in max_heap]")
    print("```")
    print("=" * 60)

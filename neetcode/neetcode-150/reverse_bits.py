"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596, so return 964176192 which its
binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101
represents the unsigned integer 4294967293, so return 3221225471 which its
binary representation is 10111111111111111111111111111111.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(32):
            bit = n & 1  # Extract the least significant bit
            output = (output << 1) | bit  # Append the bit to the output
            n >>= 1  # Right-shift n to process next bit
        return output


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem
    n1 = 0b00000010100101000001111010011100  # 43261596
    result1 = solution.reverseBits(n1)
    print(f"Test 1: n={n1}")
    print(f"Binary input:  {bin(n1)[2:].zfill(32)}")
    print(f"Binary output: {bin(result1)[2:].zfill(32)}")
    print(f"Result: {result1}")
    print("Expected: 964176192")
    print()

    # Test case 2: All 1s except last bit
    n2 = 0b11111111111111111111111111111101  # 4294967293
    result2 = solution.reverseBits(n2)
    print(f"Test 2: n={n2}")
    print(f"Binary input:  {bin(n2)[2:].zfill(32)}")
    print(f"Binary output: {bin(result2)[2:].zfill(32)}")
    print(f"Result: {result2}")
    print("Expected: 3221225471")
    print()

    # Test case 3: Simple pattern
    n3 = 0b00000000000000000000000000000001  # 1
    result3 = solution.reverseBits(n3)
    print(f"Test 3: n={n3}")
    print(f"Binary input:  {bin(n3)[2:].zfill(32)}")
    print(f"Binary output: {bin(result3)[2:].zfill(32)}")
    print(f"Result: {result3}")
    print("Expected: 2147483648 (1 becomes leftmost bit)")
    print()

    # GIẢI THÍCH CHI TIẾT
    print("=" * 70)
    print("GIẢI THÍCH: Cách REVERSE BITS hoạt động")
    print("=" * 70)

    print("\n🎯 BÀI TOÁN:")
    print("  Đảo ngược thứ tự các bit trong số 32-bit")
    print("  Bit đầu tiên → Bit cuối cùng")
    print("  Bit cuối cùng → Bit đầu tiên\n")

    print("💡 Ý TƯỞNG:")
    print("  1. Lấy bit cuối cùng của n (dùng n & 1)")
    print("  2. Thêm bit đó vào output (dùng output << 1 | bit)")
    print("  3. Bỏ bit cuối cùng của n (dùng n >>= 1)")
    print("  4. Lặp lại 32 lần\n")

    print("📝 VÍ DỤ ĐƠN GIẢN: Reverse 8 bit (dễ hiểu hơn)")
    demo_n = 0b00001101  # Số 13 trong 8 bit
    print(f"  Input:  {bin(demo_n)[2:].zfill(8)} = {demo_n}")
    print("  Output: 10110000 = 176 (sau khi đảo ngược)\n")

    print("🔍 CHI TIẾT TỪNG BƯỚC (với 8 bit):")
    demo_output = 0
    demo_input = demo_n
    print(f"  Ban đầu: n = {bin(demo_input)[2:].zfill(8)}, output = 0\n")

    for step in range(8):
        bittest = demo_input & 1
        demo_output = (demo_output << 1) | bittest
        demo_input >>= 1

        print(f"  Bước {step + 1}:")
        print(f"   • Lấy bit cuối: {bittest}")
        print(f"   • Output shift left + bit: {bin(demo_output)[2:].zfill(8)}")
        print(f"   • n shift right: {bin(demo_input)[2:].zfill(8)}")
        print()

    print(f"  ✅ Kết quả: {bin(demo_output)[2:].zfill(8)} = {demo_output}\n")

    print("🔧 PHÉP TOÁN BIT:")
    print("  • n & 1: Lấy bit cuối cùng")
    print("    Ví dụ: 1101 & 0001 = 0001 → bit = 1")
    print()
    print("  • output << 1: Dịch trái 1 bit (nhân 2, thêm 0 vào cuối)")
    print("    Ví dụ: 0011 << 1 = 0110")
    print()
    print("  • (output << 1) | bit: Thêm bit vào cuối")
    print("    Ví dụ: 0110 | 0001 = 0111")
    print()
    print("  • n >>= 1: Dịch phải 1 bit (chia 2, bỏ bit cuối)")
    print("    Ví dụ: 1101 >> 1 = 0110")
    print()

    print("🎨 HÌNH ẢNH HOÁ:")
    print("  Input:  0 0 0 0 1 1 0 1")
    print("          ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")
    print("  Output: 1 0 1 1 0 0 0 0")
    print("          (đọc ngược lại)")
    print()

    print("💻 CODE:")
    print("  output = 0")
    print("  for _ in range(32):           # Lặp 32 lần")
    print("      bit = n & 1               # Lấy bit cuối của n")
    print("      output = (output << 1) | bit  # Thêm bit vào output")
    print("      n >>= 1                   # Bỏ bit cuối của n")
    print("  return output")
    print()

    print("🚀 TẠI SAO HOẠT ĐỘNG?")
    print("  • Mỗi lần lặp: lấy bit từ PHẢI của n")
    print("  • Thêm bit đó vào PHẢI của output")
    print("  • Kết quả: thứ tự bit bị đảo ngược!")
    print("=" * 70)

    # GIẢI THÍCH PHÉP TOÁN OR (|)
    print("\n" + "=" * 70)
    print("TẠI SAO DÙNG | (OR) ĐỂ APPEND BIT VÀO CUỐI?")
    print("=" * 70)

    print("\n🔧 PHÉP TOÁN OR (|) - Bitwise OR:")
    print("  • 0 | 0 = 0")
    print("  • 0 | 1 = 1")
    print("  • 1 | 0 = 1")
    print("  • 1 | 1 = 1")
    print("  → Kết quả = 1 nếu ÍT NHẤT 1 BÊN là 1\n")

    print("📝 VÍ DỤ CỤ THỂ: Append bit vào cuối")
    print("\n  Bước 1: output = 0")
    print("          Binary: 00000000")
    print()

    print("  Muốn thêm bit 1 vào cuối:")
    print("    • Shift left: output << 1 = 00000000 (vẫn 0)")
    print("    • OR với bit:  00000000 | 1 = 00000001 ✓")
    print()

    print("  Bước 2: output = 1")
    print("          Binary: 00000001")
    print()

    print("  Muốn thêm bit 0 vào cuối:")
    print("    • Shift left: output << 1 = 00000010")
    print("    • OR với bit:  00000010 | 0 = 00000010 ✓")
    print()

    print("  Bước 3: output = 2")
    print("          Binary: 00000010")
    print()

    print("  Muốn thêm bit 1 vào cuối:")
    print("    • Shift left: output << 1 = 00000100")
    print("    • OR với bit:  00000100 | 1 = 00000101 ✓")
    print()

    print("🎯 TẠI SAO OR HOẠT ĐỘNG?")
    print("  Sau khi shift left, bit cuối LUÔN là 0")
    print("  Vị trí cuối: 0 | bit = bit")
    print()
    print("  • Nếu bit = 0: 0 | 0 = 0 (giữ nguyên)")
    print("  • Nếu bit = 1: 0 | 1 = 1 (thêm 1 vào)")
    print()

    print("💡 SO SÁNH VỚI CÁCH KHÁC:")
    print("\n  Cách 1: Dùng OR (NHANH)")
    print("    output = (output << 1) | bit")
    print()
    print("  Cách 2: Dùng cộng (CŨNG ĐƯỢC)")
    print("    output = (output << 1) + bit")
    print()
    print("  Cách 3: Dùng if/else (CHẬM HƠN)")
    print("    output = output << 1")
    print("    if bit == 1:")
    print("        output = output + 1")
    print()

    print("✅ KẾT LUẬN:")
    print("  OR (|) là cách TỐI ƯU NHẤT để set bit cuối")
    print("  • Nhanh (1 phép toán bit)")
    print("  • Rõ ràng (thể hiện ý nghĩa set bit)")
    print("  • Thường dùng trong bit manipulation")
    print("=" * 70)

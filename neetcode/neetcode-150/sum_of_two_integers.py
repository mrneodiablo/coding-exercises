class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep numbers in 32-bit range
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF  # 2^31 - 1

        step = 0
        print(f"Start: a={a}, b={b}")

        while b != 0:
            step += 1
            # Calculate sum without carry and carry
            sum_without_carry = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK

            print(f"Step {step}:")
            print(f"  a       = {a} ({bin(a & MASK)})")
            print(f"  b       = {b} ({bin(b & MASK)})")
            print("  sum without carry ")
            print(
                f"  a ^ b   = {sum_without_carry} ({bin(sum_without_carry)})"
            )
            print(f"  (a&b)<<1= {carry} ({bin(carry)})  # carry shifted left")

            a = sum_without_carry
            b = carry

        # Convert to signed integer if needed
        # If result > MAX_INT, it's negative in 32-bit
        if a > MAX_INT:
            a = ~(a ^ MASK)  # Convert to negative

        print(f"Result: {a}")
        return a


s = Solution()
s.getSum(1, -1)
s.getSum(1, 4)

class Solution:
    def isHappy(self, n: int) -> bool:

        break_loop = set()
        while n != 1:
            if n in break_loop:
                return False

            tmp = 0
            break_loop.add(n)
            while n > 0:
                tmp += (n % 10) ** 2
                n = n // 10
            n = tmp
        return True


# Test cases
def test_happy_numbers():
    solution = Solution()

    # Test case 1: Happy number (classic example)
    # 1 -> 1^2 = 1 (happy)
    assert solution.isHappy(1), "Test case 1 failed: 1 should be happy"

    # Test case 2: Happy number (another example)
    # 7 -> 49 -> 97 -> 130 -> 10 -> 1 (happy)
    assert solution.isHappy(7), "Test case 2 failed: 7 should be happy"

    # Test case 3: Not happy number (enters cycle)
    # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (cycle)
    assert not solution.isHappy(2), "Test case 3 failed: 2 should not be happy"

    print("All test cases passed!")


# Run the tests
test_happy_numbers()

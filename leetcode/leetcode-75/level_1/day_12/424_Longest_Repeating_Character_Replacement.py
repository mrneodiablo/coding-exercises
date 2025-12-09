import unittest

"""
0   1   2   3   4   5   6   7   8   9   10  11  12
C   A   B   A   A   A   A   B   B   B   B   B   A,  k,  Replacement Cost,  max len
l^r                                                  2   1 - 1 = 0 <=k       1    => increase r
l^  ^r                                               2   2 - 1 = 1 <=k       2    => increase r
l^       ^r                                          2   3 - 1 = 2 <=k       3    => increase r
l^           ^r                                      2   4 - 2 = 2 <=k       4    => increase r
l^               ^r                                  2   5 - 3 = 2 <=k       5    => increase r
l^                   ^r                              2   6 - 4 = 2 <=k       6    => increase r
l^                      r^                           2   7 - 5 = 2 <=k       7    => increase r
l^                          r^                       2   8 - 5 = 3 > k       7    => increase l,r
   l^                          r^                    2   8 - 5 = 3 > k       7    => increase l,r
       l^                           r^               2   8 - 4 = 4 > k       7    => increase l,r
           l^                           r^           2   8 - 4 = 4 > k       7    => increase l,r
               l^                           r^       2   8 - 5 = 3 > k       7    => increase l,r
                    l^                          r^   2   8 - 4 = 4 > k       7
"""  # noqa: E501


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):

            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1

            # Replacements cost = cells count between left and right - highest frequency # noqa: E501
            cells_count = r - left + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)

            else:
                c_frequency[s[left]] -= 1
                if not c_frequency[s[left]]:
                    c_frequency.pop(s[left])
                left += 1

        return longest_str_len


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        s = "ABAB"
        k = 2
        expect = 4
        self.assertEqual(
            str(self.solution.characterReplacement(s, k)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        s = "AABABBA"
        k = 1
        expect = 4
        self.assertEqual(
            str(self.solution.characterReplacement(s, k)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

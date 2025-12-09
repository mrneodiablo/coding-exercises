from collections import Counter
from typing import List
import unittest


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        count_midle = False
        counter = Counter(words)
        set_words = list(set(words))
        while len(set_words) > 0:
            first = set_words[0]
            if first[0] == first[1]:
                if (counter[first] % 2) == 0:
                    ans += (counter[first]) * 2
                else:
                    ans += (counter[first] - 1) * 2
                    if not count_midle:
                        ans += 2
                        count_midle = True

            else:
                if first[::-1] in set_words:
                    ans += min(counter[first], counter[first[::-1]]) * 2 * 2
                    set_words.remove(first[::-1])

            set_words.remove(first)

        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        words = ["lc", "cl", "gg"]
        expect = 6
        self.assertEqual(
            self.solution.longestPalindrome(words),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        words = [
            "dd",
            "aa",
            "bb",
            "dd",
            "aa",
            "dd",
            "bb",
            "dd",
            "aa",
            "cc",
            "bb",
            "cc",
            "dd",
            "cc",
        ]
        expect = 22
        self.assertEqual(
            self.solution.longestPalindrome(words),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        words = ["em", "pe", "mp", "ee", "pp", "me", "ep", "em", "em", "me"]
        expect = 14
        self.assertEqual(
            self.solution.longestPalindrome(words),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

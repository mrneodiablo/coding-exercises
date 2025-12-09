from collections import Counter
from typing import List
import unittest


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        tuples = list(counter.items())
        tuples.sort(key=lambda x: (-x[1], x[0]))
        return [t[0] for t in tuples[:k]]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        expect = ["i", "love"]
        self.assertEqual(
            str(self.solution.topKFrequent(words, k)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        words = ["the",
                 "day",
                 "is",
                 "sunny",
                 "the",
                 "the",
                 "the",
                 "sunny",
                 "is",
                 "is"]
        k = 4
        expect = ["the", "is", "sunny", "day"]
        self.assertEqual(
            str(self.solution.topKFrequent(words, k)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

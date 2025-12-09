from heapq import heapify, heappop, heappush
from typing import List
import unittest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first, negate all weight values in-place
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  # pass all negated values into the min-heap
        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # push the NEGATED value of s1-s2; i.e., s2-s1
                heappush(stones, s2 - s1)
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        stones = [2, 7, 4, 1, 8, 1]
        expect = 1
        self.assertEqual(
            str(self.solution.lastStoneWeight(stones)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        stones = [1]
        expect = 1
        self.assertEqual(
            str(self.solution.lastStoneWeight(stones)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

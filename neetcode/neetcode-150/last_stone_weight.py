"""
Docstring for neetcode.neetcode-150.last_stone_weight
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from typing import List
import heapq
import unittest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap_stones = []
        for s in stones:
            heapq.heappush(heap_stones, -s)

        while len(heap_stones) > 1:
            big = heapq.heappop(heap_stones)
            small = heapq.heappop(heap_stones)
            if small - big != 0:
                heapq.heappush(heap_stones, -(small - big))

        return 0 if len(heap_stones) == 0 else -heap_stones[0]


class TestFunctions(unittest.TestCase):

    def test_case_1_multiple_stones(self):
        """Test case with multiple stones requiring several smashes"""
        solution = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        expect = 1
        self.assertEqual(
            solution.lastStoneWeight(stones),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_2_single_stone(self):
        """Test case with only one stone"""
        solution = Solution()
        stones = [1]
        expect = 1
        self.assertEqual(
            solution.lastStoneWeight(stones),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_case_3_all_stones_destroyed(self):
        """Test case where all stones are destroyed"""
        solution = Solution()
        stones = [2, 2]
        expect = 0
        self.assertEqual(
            solution.lastStoneWeight(stones),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

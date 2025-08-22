"""
Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas during this hour

Koko likes to eat slowly but still
wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat
all the bananas within h hours.



Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

from typing import List


class Solution:
    def check_koko_eating(self, k, piles):
        eating_hour = 0
        for pile in piles:
            eating_hour += pile // k
            if pile % k > 0:
                eating_hour += 1
        return eating_hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_k = right
        while left <= right:
            k = (left + right) // 2
            checker = self.check_koko_eating(k, piles)
            if checker > h:
                left = k + 1
            else:
                right = k - 1
                best_k = k
        return best_k


solution = Solution()
print(solution.minEatingSpeed(piles=[312884470], h=312884469))

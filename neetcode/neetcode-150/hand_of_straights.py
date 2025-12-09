"""
Docstring for neetcode-150.hand_of_straights
Alice has some number of cards and she wants to rearrange
the cards into groups so that each group is of size groupSize,
and consists of groupSize consecutive cards.

Given an integer array hand where hand[i]
is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.



Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
"""

import heapq
from typing import Counter, List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand:
            return False

        if (len(hand) % groupSize) != 0:
            return False
        count = Counter(hand)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]  # Always start from smallest
            for card in range(first, first + groupSize):
                count[card] -= 1  # Use one card
                if count[card] == 0:
                    # This card type is exhausted
                    if card != min_heap[0]:
                        return False  # Out of order!
                    heapq.heappop(min_heap)  # Remove from heap
                elif count[card] < 0:
                    return False
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    hand1 = [8, 10, 12]
    groupSize1 = 3
    result1 = solution.isNStraightHand(hand1, groupSize1)

    # Test case 1: Can form consecutive groups
    hand1 = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize1 = 3
    result1 = solution.isNStraightHand(hand1, groupSize1)
    print("Test 1:")
    print(f"Input:  hand = {hand1}, groupSize = {groupSize1}")
    print(f"Output: {result1}")
    print("Expected: True")
    print("Explanation: Can form [1,2,3], [2,3,4], [6,7,8]")
    print()

    # Test case 2: Cannot form groups (not enough cards)
    hand2 = [1, 2, 3, 4, 5]
    groupSize2 = 4
    result2 = solution.isNStraightHand(hand2, groupSize2)
    print("Test 2:")
    print(f"Input:  hand = {hand2}, groupSize = {groupSize2}")
    print(f"Output: {result2}")
    print("Expected: False")
    print("Explanation: 5 cards cannot be divided into groups of 4")
    print()

    # Test case 3: Cannot form consecutive groups (missing card)
    hand3 = [1, 2, 3, 5, 6, 7]
    groupSize3 = 3
    result3 = solution.isNStraightHand(hand3, groupSize3)
    print("Test 3:")
    print(f"Input:  hand = {hand3}, groupSize = {groupSize3}")
    print(f"Output: {result3}")
    print("Expected: True")
    print()

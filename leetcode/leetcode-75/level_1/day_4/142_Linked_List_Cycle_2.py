# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mapping = {}
        ans = None
        while head:
            if head not in mapping.keys():
                mapping[head] = 1
            else:
                ans = head
                break
            head = head.next
        return ans

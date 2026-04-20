"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # init
        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        current_node = head
        next_node = current_node.next

        while True:

            # step 1 count K node from current
            tmp = current_node
            for _ in range(k):
                if not tmp:
                    return dummy.next
                tmp = tmp.next

            # step 2 reverse K node
            previous_node = None
            for _ in range(k):
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            # step 3:
            group_tail = group_prev.next
            group_tail.next = current_node
            group_prev.next = previous_node

            group_prev = group_tail

        return dummy.next


def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestReverseKGroup(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_k2(self):
        head = build_list([1, 2, 3, 4, 5])
        result = self.sol.reverseKGroup(head, 2)
        self.assertEqual(to_list(result), [2, 1, 4, 3, 5])

    def test_k3(self):
        head = build_list([1, 2, 3, 4, 5])
        result = self.sol.reverseKGroup(head, 3)
        self.assertEqual(to_list(result), [3, 2, 1, 4, 5])

    def test_k_equals_length(self):
        head = build_list([1, 2, 3])
        result = self.sol.reverseKGroup(head, 3)
        self.assertEqual(to_list(result), [3, 2, 1])

    def test_k1(self):
        head = build_list([1, 2, 3])
        result = self.sol.reverseKGroup(head, 1)
        self.assertEqual(to_list(result), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)

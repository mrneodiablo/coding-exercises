"""
Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional
import unittest


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        # Step 1: Interleave — insert copy after each original
        # A -> A' -> B -> B' -> C -> C'
        pointer = head
        while pointer:
            copy = Node(pointer.val)
            copy.next = pointer.next
            pointer.next = copy
            pointer = copy.next

        # Step 2: Wire up random pointers for copies
        pointer = head
        while pointer:
            if pointer.random:
                pointer.next.random = pointer.random.next
            pointer = pointer.next.next

        # Step 3: Separate the two lists
        pointer = head
        copy_head = head.next
        while pointer:
            copy = pointer.next
            pointer.next = copy.next
            copy.next = copy.next.next if copy.next else None
            pointer = pointer.next

        return copy_head

    def copyRandomListHashmap(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return

        tracking = {}

        pointer = head
        new_copy_head = None
        while pointer:

            new_node = Node(pointer.val)
            tracking[pointer] = new_node

            if not new_copy_head:
                new_copy_head = new_node

            pointer = pointer.next

        pointer = head
        while pointer:

            if pointer.next:
                tracking[pointer].next = tracking[pointer.next]

            if pointer.random:
                tracking[pointer].random = tracking[pointer.random]

            pointer = pointer.next

        return new_copy_head


def build_list(data):
    """Build linked list from list of [val, random_index] pairs."""
    if not data:
        return None
    nodes = [Node(v) for v, _ in data]
    for i, node in enumerate(nodes):
        node.next = nodes[i + 1] if i + 1 < len(nodes) else None
        ri = data[i][1]
        node.random = nodes[ri] if ri is not None else None
    return nodes[0]


def to_list(head):
    """Convert linked list to list of [val, random_index] pairs."""
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    result = []
    for node in nodes:
        ri = nodes.index(node.random) if node.random is not None else None
        result.append([node.val, ri])
    return result


class TestCopyRandomList(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        head = build_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
        copied = self.sol.copyRandomList(head)
        self.assertEqual(
            to_list(copied), [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
        )

    def test_example2(self):
        head = build_list([[1, 1], [2, 1]])
        copied = self.sol.copyRandomList(head)
        self.assertEqual(to_list(copied), [[1, 1], [2, 1]])

    def test_example3(self):
        head = build_list([[3, None], [3, 0], [3, None]])
        copied = self.sol.copyRandomList(head)
        self.assertEqual(to_list(copied), [[3, None], [3, 0], [3, None]])

    def test_empty_list(self):
        copied = self.sol.copyRandomList(None)
        self.assertIsNone(copied)


if __name__ == "__main__":
    unittest.main(verbosity=2)

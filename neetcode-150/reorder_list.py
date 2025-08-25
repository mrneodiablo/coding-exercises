"""
You are given the head of a singly linked-list.
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow = head
        # Start fast at head.next for better splitting
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the list into two halves
        second = slow.next
        slow.next = None  # Cut the connection

        # Step 3: Reverse the second half
        prev = None
        current = second
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        # Step 4: Merge the two halves
        first = head
        second = prev

        while second:  # second list determines when to stop
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Even number of nodes [1,2,3,4] -> [1,4,2,3]"""
        input_list = create_linked_list([1, 2, 3, 4])
        expected = [1, 4, 2, 3]
        self.solution.reorderList(input_list)  # Modifies in-place
        result_list = linked_list_to_list(input_list)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}"
        )

    def test_run_2(self):
        """Test case 2: Odd number of nodes [1,2,3,4,5] -> [1,5,2,4,3]"""
        input_list = create_linked_list([1, 2, 3, 4, 5])
        expected = [1, 5, 2, 4, 3]
        self.solution.reorderList(input_list)  # Modifies in-place
        result_list = linked_list_to_list(input_list)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}"
        )

    def test_run_3(self):
        """Test case 3: Single node [1] -> [1] (edge case)"""
        input_list = create_linked_list([1])
        expected = [1]
        self.solution.reorderList(input_list)  # Modifies in-place
        result_list = linked_list_to_list(input_list)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

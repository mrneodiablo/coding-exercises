"""
Given the head of a singly linked list,
reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None

        previous = dummy
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous


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


def sum_link_list(linkList: ListNode):
    """Sum all values in linked list (for alternative testing)"""
    if not linkList:
        return 0
    total = 0
    while linkList is not None:
        total += int(linkList.val)
        linkList = linkList.next
    return total


# Test cases using unittest pattern (matching your style)

class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Basic reverse [1,2,3,4,5] -> [5,4,3,2,1]"""
        input_list = create_linked_list([1, 2, 3, 4, 5])
        expected = [5, 4, 3, 2, 1]
        result = self.solution.reverseList(input_list)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}"
        )

    def test_run_2(self):
        """Test case 2: Two nodes [1,2] -> [2,1]"""
        input_list = create_linked_list([1, 2])
        expected = [2, 1]
        result = self.solution.reverseList(input_list)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}"
        )

    def test_run_3(self):
        """Test case 3: Empty list [] -> []"""
        input_list = create_linked_list([])
        expected = []
        result = self.solution.reverseList(input_list)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"incorrect, expect is {expected}, got {result_list}"
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

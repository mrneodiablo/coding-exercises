"""
Given the head of a linked list,
remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self,
                         head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


def create_linked_list(values):
    """Helper function to create
    a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert
    linked list back to a list for easy comparison"""
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
        # Test case 1: Remove 2nd node from end (middle removal)
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected = [1, 2, 3, 5]  # Remove node with value 4
        result = self.solution.removeNthFromEnd(head, n)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"Expected {expected}, but got {result_list}"
        )

    def test_run_2(self):
        # Test case 2: Remove 1st node from end (tail removal)
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 1
        expected = [1, 2, 3, 4]  # Remove node with value 5
        result = self.solution.removeNthFromEnd(head, n)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"Expected {expected}, but got {result_list}"
        )

    def test_run_3(self):
        # Test case 3: Remove last node from end (head removal)
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 5
        expected = [2, 3, 4, 5]  # Remove node with value 1
        result = self.solution.removeNthFromEnd(head, n)
        result_list = linked_list_to_list(result)
        self.assertEqual(
            result_list,
            expected,
            f"Expected {expected}, but got {result_list}"
        )


def test_remove_nth_from_end():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Remove 2nd node from end (middle removal)")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    expected1 = [1, 2, 3, 5]
    result1 = solution.removeNthFromEnd(head1, n1)
    result1_list = linked_list_to_list(result1)
    print(f"  Input: head = [1,2,3,4,5], n = {n1}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1_list}")
    print(f"  ✅ {'PASSED' if result1_list == expected1 else 'FAILED'}")
    print()

    print("Test 2: Remove 1st node from end (tail removal)")
    head2 = create_linked_list([1, 2, 3, 4, 5])
    n2 = 1
    expected2 = [1, 2, 3, 4]
    result2 = solution.removeNthFromEnd(head2, n2)
    result2_list = linked_list_to_list(result2)
    print(f"  Input: head = [1,2,3,4,5], n = {n2}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2_list}")
    print(f"  ✅ {'PASSED' if result2_list == expected2 else 'FAILED'}")
    print()

    print("Test 3: Remove last node from end (head removal)")
    head3 = create_linked_list([1, 2, 3, 4, 5])
    n3 = 5
    expected3 = [2, 3, 4, 5]
    result3 = solution.removeNthFromEnd(head3, n3)
    result3_list = linked_list_to_list(result3)
    print(f"  Input: head = [1,2,3,4,5], n = {n3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3_list}")
    print(f"  ✅ {'PASSED' if result3_list == expected3 else 'FAILED'}")
    print()

    print("Test 4: Single node list")
    head4 = create_linked_list([1])
    n4 = 1
    expected4 = []
    result4 = solution.removeNthFromEnd(head4, n4)
    result4_list = linked_list_to_list(result4)
    print(f"  Input: head = [1], n = {n4}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4_list}")
    print(f"  ✅ {'PASSED' if result4_list == expected4 else 'FAILED'}")
    print()

    print("Test 5: Two node list, remove first")
    head5 = create_linked_list([1, 2])
    n5 = 2
    expected5 = [2]
    result5 = solution.removeNthFromEnd(head5, n5)
    result5_list = linked_list_to_list(result5)
    print(f"  Input: head = [1,2], n = {n5}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5_list}")
    print(f"  ✅ {'PASSED' if result5_list == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

    # Run manual tests
    print("\n" + "=" * 50)
    test_remove_nth_from_end()

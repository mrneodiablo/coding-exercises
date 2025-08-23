"""
Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together
the nodes of the first two lists.

Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
            current.next = list1

        if list2 is not None:
            current.next = list2

        return dummy.next


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


def test_merge_two_sorted_lists():
    """3 test cases for mergeTwoLists function"""
    solution = Solution()

    print("🧪 Testing mergeTwoLists - 3 Key Test Cases")
    print("=" * 50)

    # Test Case 1: Basic merge of two non-empty lists
    print("Test 1: Basic merge example")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    expected1 = [1, 1, 2, 3, 4, 4]
    result1 = solution.mergeTwoLists(list1, list2)
    result1_list = linked_list_to_list(result1)

    print("  Input: list1 = [1,2,4], list2 = [1,3,4]")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1_list}")
    print(f"  ✅ {'PASSED' if result1_list == expected1 else 'FAILED'}")
    print()

    # Test Case 2: One empty list
    print("Test 2: One empty list (edge case)")
    list1 = create_linked_list([])  # Empty list
    list2 = create_linked_list([0])
    expected2 = [0]
    result2 = solution.mergeTwoLists(list1, list2)
    result2_list = linked_list_to_list(result2)

    print("  Input: list1 = [], list2 = [0]")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2_list}")
    print(f"  ✅ {'PASSED' if result2_list == expected2 else 'FAILED'}")
    print()

    # Test Case 3: Both empty lists
    print("Test 3: Both empty lists (edge case)")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    expected3 = []
    result3 = solution.mergeTwoLists(list1, list2)
    result3_list = linked_list_to_list(result3)

    print("  Input: list1 = [], list2 = []")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3_list}")
    print(f"  ✅ {'PASSED' if result3_list == expected3 else 'FAILED'}")
    print()

    # Summary
    all_results = [result1_list, result2_list, result3_list]
    all_expected = [expected1, expected2, expected3]
    passed = sum(1 for r, e in zip(all_results, all_expected) if r == e)

    print(f"📊 SUMMARY: {passed}/3 tests passed")
    if passed == 3:
        print("🎉 ALL TESTS PASSED! Your function works correctly!")
    else:
        print("🔧 Some tests failed. Check the implementation.")


if __name__ == "__main__":
    test_merge_two_sorted_lists()

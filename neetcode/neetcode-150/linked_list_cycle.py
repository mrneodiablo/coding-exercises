"""
Linked List Cycle
Given head, the head of a linked list,
determine if the linked list has a cycle in it.

There is a cycle in a linked list if there
is some node in the list that can be reached again by
continuously following the next pointer.
Internally, pos is used to denote the index of
the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list.
Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where the tail connects to the 1st node (0-indexed).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        checker = {}
        current = head
        while current:
            if current not in checker:
                checker[current] = 1
            else:
                return True
            current = current.next

        return False


# Helper functions for testing
def create_linked_list_with_cycle(values, pos):
    """Create a linked list with a cycle at given position"""
    if not values:
        return None

    # Create all nodes
    nodes = [ListNode(val) for val in values]

    # Link nodes together
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create cycle if pos is valid
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]  # Last node points to pos

    return nodes[0]  # Return head


def create_linked_list_no_cycle(values):
    """Create a linked list without cycle"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def test_has_cycle():
    """Test cases for hasCycle function"""
    solution = Solution()

    print("🧪 Testing hasCycle - 4 Key Test Cases")
    print("=" * 50)

    # Test Case 1: List with cycle (from problem example)
    print("Test 1: List with cycle at position 1")
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], pos=1)
    expected1 = True
    result1 = solution.hasCycle(head1)

    print("  Input: [3,2,0,-4] with cycle at pos=1")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    # Test Case 2: List without cycle
    print("Test 2: List without cycle")
    head2 = create_linked_list_no_cycle([1, 2, 3, 4])
    expected2 = False
    result2 = solution.hasCycle(head2)

    print("  Input: [1,2,3,4] with no cycle")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    # Test Case 3: Single node with self-cycle
    print("Test 3: Single node pointing to itself")
    head3 = ListNode(1)
    head3.next = head3  # Points to itself
    expected3 = True
    result3 = solution.hasCycle(head3)

    print("  Input: [1] pointing to itself")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    # Test Case 4: Empty list
    print("Test 4: Empty list")
    head4 = None
    expected4 = False
    result4 = solution.hasCycle(head4)

    print("  Input: None (empty list)")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    # Summary
    all_results = [result1, result2, result3, result4]
    all_expected = [expected1, expected2, expected3, expected4]
    passed = sum(1 for r, e in zip(all_results, all_expected) if r == e)

    print(f"📊 SUMMARY: {passed}/4 tests passed")
    if passed == 4:
        print("🎉 ALL TESTS PASSED! Your hasCycle function works correctly!")
    else:
        print("🔧 Some tests failed. Check the implementation.")


if __name__ == "__main__":
    test_has_cycle()

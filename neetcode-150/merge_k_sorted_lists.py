# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[int]]) -> Optional[int]:
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = tail = ListNode()

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ============== HELPER FUNCTIONS ==============


def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from array"""
    if not arr:
        return None

    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return dummy.next


def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert linked list to array for easy testing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# ============== TEST CASES ==============


def test_merge_k_lists():
    s = Solution()

    print("=" * 60)
    print("Testing Merge K Sorted Lists")
    print("=" * 60)

    # Test Case 1: Basic example with 3 lists
    print("\n📝 Test Case 1: Merge 3 sorted lists")
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6]),
    ]
    result1 = s.mergeKLists(lists1)
    output1 = linked_list_to_array(result1)
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]

    print("Input lists: [[1,4,5], [1,3,4], [2,6]]")
    print(f"Output: {output1}")
    print(f"Expected: {expected1}")
    status1 = "✓ PASS" if output1 == expected1 else "✗ FAIL"
    print(status1)

    # Test Case 2: Empty lists
    print("\n📝 Test Case 2: Empty input")
    lists2 = []
    result2 = s.mergeKLists(lists2)
    output2 = linked_list_to_array(result2)
    expected2 = []

    print("Input lists: []")
    print(f"Output: {output2}")
    print(f"Expected: {expected2}")
    status = "✓ PASS" if output2 == expected2 else "✗ FAIL"
    print(status)

    # Test Case 3: Lists with empty list included
    print("\n📝 Test Case 3: Mix of empty and non-empty lists")
    lists3 = [create_linked_list([]),
              create_linked_list([1]),
              create_linked_list([])]
    result3 = s.mergeKLists(lists3)
    output3 = linked_list_to_array(result3)
    expected3 = [1]

    print("Input lists: [[], [1], []]")
    print(f"Output: {output3}")
    print(f"Expected: {expected3}")
    status = "✓ PASS" if output3 == expected3 else "✗ FAIL"
    print(status)

    # Test Case 4: Single list
    print("\n📝 Test Case 4: Single sorted list")
    lists4 = [create_linked_list([1, 2, 3, 4, 5])]
    result4 = s.mergeKLists(lists4)
    output4 = linked_list_to_array(result4)
    expected4 = [1, 2, 3, 4, 5]
    print("Input: [[1,2,3,4,5]]")
    print(f"Output: {output4}")
    print(f"Expected: {expected4}")
    status = "✓ PASS" if output4 == expected4 else "✗ FAIL"
    print(status)

    # Test Case 5: Lists with negative numbers
    print("\n📝 Test Case 5: Lists with negative numbers")
    lists5 = [
        create_linked_list([-2, -1, 0]),
        create_linked_list([-3, 1, 2]),
        create_linked_list([-5, -4, 3]),
    ]
    result5 = s.mergeKLists(lists5)
    output5 = linked_list_to_array(result5)
    expected5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3]
    print("Input: [[-2,-1,0], [-3,1,2], [-5,-4,3]]")
    print(f"Output: {output5}")
    print(f"Expected: {expected5}")
    status = "✓ PASS" if output5 == expected5 else "✗ FAIL"
    print(status)


if __name__ == "__main__":
    test_merge_k_lists()

"""
You are given two non-empty linked lists
representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Optimize by reusing l1 and extending it when needed
        residual = 0
        curr = l1
        prev = None
        while curr or residual:

            summary = residual
            if curr:
                summary += curr.val
            else:
                # If curr is None but we still have residual or l2, extend l1
                curr = ListNode(0)
                prev.next = curr
                summary += curr.val

            if l2:
                summary += l2.val
                l2 = l2.next

            dec_addition = summary % 10
            residual = summary // 10
            curr.val = dec_addition

            # Keep track of previous node for extending l1
            prev = curr
            curr = curr.next

            # If we need to continue but curr is None, create new node
            if (residual or l2) and not curr:
                curr = ListNode(0)
                prev.next = curr

        return l1


def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert linked list back to
    a list for easy comparison"""
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
        # Test case 1: Basic addition (342 + 465 = 807)
        l1 = create_linked_list([2, 4, 3])  # represents 342
        l2 = create_linked_list([5, 6, 4])  # represents 465
        expected = [7, 0, 8]  # represents 807
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result)
        self.assertEqual(result_list,
                         expected,
                         "incorrect, expect is " + str(expected))

    def test_run_2(self):
        # Test case 2: Different lengths with carry (99 + 9 = 108)
        l1 = create_linked_list([9, 9])  # represents 99
        l2 = create_linked_list([9])  # represents 9
        expected = [8, 0, 1]  # represents 108
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result)
        self.assertEqual(result_list,
                         expected,
                         "incorrect, expect is " + str(expected)
                         )

    def test_run_3(self):
        # Test case 3: Multiple carries (999 + 999 = 1998)
        l1 = create_linked_list([9, 9, 9])  # represents 999
        l2 = create_linked_list([9, 9, 9])  # represents 999
        expected = [8, 9, 9, 1]  # represents 1998
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = linked_list_to_list(result)
        self.assertEqual(result_list,
                         expected,
                         "incorrect, expect is " + str(expected)
                         )


def test_add_two_numbers():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Basic addition (342 + 465 = 807)")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    expected1 = [7, 0, 8]
    result1 = solution.addTwoNumbers(l1, l2)
    result1_list = linked_list_to_list(result1)
    print("  Input: l1 = [2,4,3], l2 = [5,6,4]")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1_list}")
    print(f"  ✅ {'PASSED' if result1_list == expected1 else 'FAILED'}")
    print()

    print("Test 2: Different lengths with carry (99 + 9 = 108)")
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([9])
    expected2 = [8, 0, 1]
    result2 = solution.addTwoNumbers(l1, l2)
    result2_list = linked_list_to_list(result2)
    print("  Input: l1 = [9,9], l2 = [9]")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2_list}")
    print(f"  ✅ {'PASSED' if result2_list == expected2 else 'FAILED'}")
    print()

    print("Test 3: Multiple carries (999 + 999 = 1998)")
    l1 = create_linked_list([9, 9, 9])
    l2 = create_linked_list([9, 9, 9])
    expected3 = [8, 9, 9, 1]
    result3 = solution.addTwoNumbers(l1, l2)
    result3_list = linked_list_to_list(result3)
    print("  Input: l1 = [9,9,9], l2 = [9,9,9]")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3_list}")
    print(f"  ✅ {'PASSED' if result3_list == expected3 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_add_two_numbers()

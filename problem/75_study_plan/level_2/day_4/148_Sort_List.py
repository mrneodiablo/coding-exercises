# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def travesalLinkList(head: Optional[ListNode]) -> Optional[list]:
    ans = []
    dummy = head
    while dummy:
        ans.append(dummy.val)
        dummy = dummy.next
    return ans


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1 2 3 4 5 6 7
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # midle is slow
        midle = slow.next
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(midle)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        curr.next = left or right
        return dummy.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        expect = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertEqual(
            travesalLinkList(self.solution.sortList(head)),
            travesalLinkList(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

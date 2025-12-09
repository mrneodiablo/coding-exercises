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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenList = dummyEven = ListNode()
        oddList = dummyOod = ListNode()

        couter = 0
        while head:
            couter += 1
            # even
            if (couter % 2) == 0:
                dummyEven.next = head
                dummyEven = dummyEven.next
                dummyOod.next = None
            else:
                # odd
                dummyOod.next = head
                dummyOod = dummyOod.next
                dummyEven.next = None
            head = head.next

        if evenList.next:
            dummyOod.next = evenList.next

        return oddList.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(1,
                        ListNode(2,
                                 ListNode(3, ListNode(4, ListNode(5)))))
        expect = ListNode(1,
                          ListNode(3,
                                   ListNode(5, ListNode(2, ListNode(4)))))
        self.assertEqual(
            travesalLinkList(self.solution.oddEvenList(head)),
            travesalLinkList(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

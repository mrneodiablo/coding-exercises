from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_link_list(linkList: ListNode):
    a = 0
    while linkList is not None:
        a += int(linkList.val)
        linkList = linkList.next
    return a


class Solution:

    def removeNthFromEnd(self,
                         head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pnt1, pnt2 = dummy, head

        for _ in range(n):
            pnt2 = pnt2.next

        while pnt2:
            pnt1, pnt2 = pnt1.next, pnt2.next

        pnt1.next = pnt1.next.next
        return dummy.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        n = 2
        expect = ListNode(1, ListNode(2, ListNode(3, ListNode(5, None))))
        self.assertEqual(
            sum_link_list(self.solution.removeNthFromEnd(head, n)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)),
        )

    def test_run_2(self):
        # test case
        head = ListNode(1)
        n = 1
        expect = 0
        self.assertEqual(
            sum_link_list(self.solution.removeNthFromEnd(head, n)),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

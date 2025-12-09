from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sum_link_list(linkList: ListNode):
    a = 0
    while linkList.next is not None:
        a += int(linkList.val)
        linkList = linkList.next
    return a


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        list1 = ListNode(1, ListNode(2, ListNode(4, None)))
        list2 = ListNode(1, ListNode(3, ListNode(4, None)))

        expect = ListNode(
            1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
        )
        self.assertEqual(
            sum_link_list(self.solution.mergeTwoLists(list1, list2)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)),
        )

    def test_run_2(self):
        # test case
        list1 = ListNode()
        list2 = ListNode()

        expect = ListNode()
        self.assertEqual(
            sum_link_list(self.solution.mergeTwoLists(list1, list2)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)),
        )

    def test_run_3(self):
        # test case
        list1 = ListNode()
        list2 = ListNode(0)

        expect = ListNode(0)
        self.assertEqual(
            sum_link_list(self.solution.mergeTwoLists(list1, list2)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

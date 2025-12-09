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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp

        return previous


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        list1 = ListNode(1, ListNode(2, ListNode(4, None)))
        expect = ListNode(
            4,
            ListNode(
                2,
                ListNode(
                    1,
                ),
            ),
        )
        self.assertEqual(
            sum_link_list(self.solution.reverseList(list1)),
            sum_link_list(expect),
            "incorrect, expect is " + str(sum_link_list(expect)),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

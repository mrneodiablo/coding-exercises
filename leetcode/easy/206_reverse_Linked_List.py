# Definition for singly-linked list.
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        [1] -> [2] -> [3] -> [4]
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expect = ListNode(4, ListNode(3, ListNode(2, ListNode(1))))

        self.assertEqual(sum_link_list(self.solution.reverseList(head)),
                         sum_link_list(expect),
                         "incorrect, expect is " + str(sum_link_list(expect))
                         )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

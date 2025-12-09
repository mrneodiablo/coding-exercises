# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp == tmp[::-1]


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        expect = True
        self.assertEqual(
            self.solution.isPalindrome(head),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        head = ListNode(1, ListNode(2))
        expect = False
        self.assertEqual(
            self.solution.isPalindrome(head),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

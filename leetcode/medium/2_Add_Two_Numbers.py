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
        value_l1 = ""
        value_l2 = ""

        while l1:
            value_l1 += str(l1.val)
            l1 = l1.next

        while l2:
            value_l2 += str(l2.val)
            l2 = l2.next

        out = ListNode()
        for i in str(int(value_l1[::-1]) + int(value_l2[::-1])):
            newNode = ListNode(i)
            newNode.next = out.next
            out.next = newNode
        return out.next

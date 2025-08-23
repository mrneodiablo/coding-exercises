"""
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true
Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkNode(node: TreeNode):
            if node is None:
                return 0  #

            left_hight = checkNode(node.left)
            right_hight = checkNode(node.right)

            if abs(left_hight - right_hight) > 1:
                return -1

            if left_hight == -1 or right_hight == -1:
                return -1

            return max(left_hight, right_hight) + 1

        return checkNode(root) >= 0

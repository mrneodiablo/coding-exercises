"""
98. Validate Binary Search Tree
Given the root of a binary tree,
determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

* The left subtree of a node contains only nodes with
keys strictly less than the node's key.

* The right subtree of a node contains only nodes with
keys strictly greater than the node's key.

Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true
"""

# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use a list to allow modification in nested function
        prev = [None]

        def inorderBST(node: Optional[TreeNode]):
            if not node:
                return True
            # Traverse left subtree
            if not inorderBST(node.left):
                return False
            # Compare current node's value with previous value
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val  # Update previous value
            # Traverse right subtree
            return inorderBST(node.right)

        return inorderBST(root)


def build_tree_from_list(vals):
    if not vals:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


class TestValidateBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_bst(self):
        # [2,1,3] is a valid BST
        root = build_tree_from_list([2, 1, 3])
        self.assertTrue(self.solution.isValidBST(root))

    # def test_invalid_bst(self):
    #     # [5,1,4,None,None,3,6] is not a valid BST
    #     root = build_tree_from_list([5, 1, 4, None, None, 3, 6])
    #     self.assertFalse(self.solution.isValidBST(root))

    # def test_single_node(self):
    #     # [1] is a valid BST
    #     root = build_tree_from_list([1])
    #     self.assertTrue(self.solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()

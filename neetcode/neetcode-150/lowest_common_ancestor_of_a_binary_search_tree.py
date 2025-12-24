"""
Docstring for neetcode.neetcode-150.lowest_common_ancestor_of_a_binary_search_tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Iterative approach - O(h) time, O(1) space
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while root:
            # Both nodes are in right subtree
            if p.val > root.val and q.val > root.val:
                root = root.right
            # Both nodes are in left subtree
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # Split point found - this is the LCA
            else:
                return root
        return root

    # Recursive approach - O(h) time, O(h) space
    def lowestCommonAncestor_recursive(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_recursive(root.right, p, q)

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_recursive(root.left, p, q)

        return root


class TestLowestCommonAncestor(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_lca_with_nodes_on_different_sides(self):
        """Test case 1: p and q are on different sides of root"""
        # Build tree: [6,2,8,0,4,7,9,null,null,3,5]
        #        6
        #       / \
        #      2   8
        #     / \ / \
        #    0  4 7  9
        #      / \
        #     3   5
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left  # Node with value 2
        q = root.right  # Node with value 8

        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 6, "LCA of 2 and 8 should be 6")

    def test_lca_when_one_node_is_ancestor(self):
        """Test case 2: One node is ancestor of the other"""
        # Build tree: [6,2,8,0,4,7,9,null,null,3,5]
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left  # Node with value 2
        q = root.left.right  # Node with value 4

        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2, "LCA of 2 and 4 should be 2")

    def test_lca_with_minimal_tree(self):
        """Test case 3: Minimal tree with two nodes"""
        # Build tree: [2,1]
        #      2
        #     /
        #    1
        root = TreeNode(2)
        root.left = TreeNode(1)

        p = root  # Node with value 2
        q = root.left  # Node with value 1

        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2, "LCA of 2 and 1 should be 2")


if __name__ == "__main__":
    unittest.main(verbosity=2)

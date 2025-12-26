"""
Docstring for neetcode.neetcode-150.binary_tree_maximum_path_sum
124. Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

"""

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Bottom-up approach: Start with smallest case and build up

        Case 1: Single node (leaf)
            - left = 0, right = 0
            - ans = max(ans, node.val + 0 + 0) = node.val
            - return node.val (max path going down from this node)

        Case 2: Node with 2 children (3 nodes total)
            - left = max from left subtree
            - right = max from right subtree
            - ans = max(ans, node.val + left + right) <- path through this node
            - return node.val + max(left, right) <- continue path upward

        Case 3: Larger tree
            - DFS from leaves up to root
            - At each node, calculate max path THROUGH that node
            - Keep global max across all possibilities
        """
        # Initialize ans with root value to handle single node case
        ans = root.val

        def dfs(node: Optional[TreeNode]):
            """
            DFS returns the maximum path sum from this node going DOWN (one direction only).
            This is used by parent node to calculate its path sum.
            """
            nonlocal ans

            if not node:
                return 0

            # Get max path sum from left and right subtrees
            # Ignore negative paths (don't include them, set to 0)
            # Because negative path will decrease our sum
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Update global max: consider current node as "root" of a path
            # Path goes through this node: left -> node -> right
            ans = max(ans, node.val + left + right)

            # Return max path going DOWN from this node (for parent to use)
            # Can only go either left OR right (not both), so choose the better one
            return node.val + max(left, right)

        dfs(root)
        return ans


class TestMaxPathSum(unittest.TestCase):
    def test_case_1(self):
        """Test case 1: root = [1,2,3], expected output = 6"""
        # Build tree: 1 -> left: 2, right: 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        solution = Solution()
        result = solution.maxPathSum(root)
        self.assertEqual(result, 6)

    def test_case_2(self):
        """Test case 2: root = [-10,9,20,null,null,15,7], expected output = 42"""
        # Build tree: -10 -> left: 9, right: 20 (20 -> left: 15, right: 7)
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()
        result = solution.maxPathSum(root)
        self.assertEqual(result, 42)

    def test_case_3(self):
        """Test case 3: Single node with negative value, root = [-3], expected output = -3"""
        root = TreeNode(-3)

        solution = Solution()
        result = solution.maxPathSum(root)
        self.assertEqual(result, -3)

    def test_case_4(self):
        """Test case 4: root = [1,-2,3], expected output = 4"""
        # Build tree: 1 -> left: -2, right: 3
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.right = TreeNode(3)

        solution = Solution()
        result = solution.maxPathSum(root)
        self.assertEqual(result, 4)


if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxPathSum)
    unittest.TextTestRunner(verbosity=2).run(suite)

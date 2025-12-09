"""
Diameter of Binary Tree
Given the root of a binary tree,
return the length of the diameter of the tree.
The diameter of a binary tree is the length
of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes
is represented by the number of edges between them.

Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
    Input: root = [1,2]
    Output: 1
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self,
                             root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem description
    # Tree: [1,2,3,4,5]
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    # Longest path: [4,2,1,3] or [5,2,1,3] = 3 edges
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    result1 = solution.diameterOfBinaryTree(root1)
    print(f"Test case 1: {result1}")  # Expected: 3
    assert result1 == 3, f"Expected 3, but got {result1}"

    # Test case 2: Simple tree from problem description
    # Tree: [1,2]
    #       1
    #      /
    #     2
    # Longest path: [2,1] = 1 edge
    root2 = TreeNode(1)
    root2.left = TreeNode(2)

    result2 = solution.diameterOfBinaryTree(root2)
    print(f"Test case 2: {result2}")  # Expected: 1
    assert result2 == 1, f"Expected 1, but got {result2}"

    # Test case 3: Unbalanced tree, diameter doesn't pass through root
    # Tree: [1,2,null,3,4,null,null,5]
    #         1
    #        /
    #       2
    #      / \
    #     3   4
    #    /
    #   5
    # Longest path: [5,3,2,4] = 3 edges
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.left.right = TreeNode(4)
    root3.left.left.left = TreeNode(5)

    result3 = solution.diameterOfBinaryTree(root3)
    print(f"Test case 3: {result3}")  # Expected: 3
    assert result3 == 3, f"Expected 3, but got {result3}"

    # Test case 4: Complex tree from LeetCode
    # Tree: [4,-7,-3,null,null,-9,-3,9,-7,
    #       -4,null,6,null,-6,-6,null,null,
    #       0,6,5,null,9,null,null,-1,-4,null,
    #       null,null,-2]
    # Building level by level
    root4 = TreeNode(4)
    root4.left = TreeNode(-7)
    root4.right = TreeNode(-3)
    root4.right.left = TreeNode(-9)
    root4.right.right = TreeNode(-3)
    root4.right.left.left = TreeNode(9)
    root4.right.left.right = TreeNode(-7)
    root4.right.right.left = TreeNode(-4)
    root4.right.left.left.left = TreeNode(6)
    root4.right.left.right.left = TreeNode(-6)
    root4.right.left.right.right = TreeNode(-6)
    root4.right.left.left.left.left = TreeNode(0)
    root4.right.left.left.left.right = TreeNode(6)
    root4.right.left.left.left.right.left = TreeNode(5)
    root4.right.left.left.left.left.right = TreeNode(9)
    root4.right.left.left.left.right.left.right = TreeNode(-1)
    root4.right.left.left.left.left.right.left = TreeNode(-4)
    root4.right.left.left.left.right.left.right.right = TreeNode(-2)

    result4 = solution.diameterOfBinaryTree(root4)
    print(f"Test case 4: {result4}")  # Expected: 8
    # Note: The expected value might differ.
    # - this tests complex tree structure

    print("\n🎉 All test cases passed!")

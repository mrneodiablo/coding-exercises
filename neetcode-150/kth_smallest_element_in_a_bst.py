"""
Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) of
all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def dfs(node: TreeNode):
            nonlocal count, result
            if not node or result is not None:
                return

            dfs(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            dfs(node.right)

        dfs(root)
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem description
    # Tree: [3,1,4,null,2]
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)

    result1 = solution.kthSmallest(root1, 1)
    print(f"Test case 1: {result1}")  # Expected: 1
    assert result1 == 1, f"Expected 1, but got {result1}"

    # Test case 2: Larger tree from problem description
    # Tree: [5,3,6,2,4,null,null,1]
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    result2 = solution.kthSmallest(root2, 3)
    print(f"Test case 2: {result2}")  # Expected: 3
    assert result2 == 3, f"Expected 3, but got {result2}"

    # Test case 3: Single node, k=1
    root3 = TreeNode(1)

    result3 = solution.kthSmallest(root3, 1)
    print(f"Test case 3: {result3}")  # Expected: 1
    assert result3 == 1, f"Expected 1, but got {result3}"

    print("\n🎉 All test cases passed!")

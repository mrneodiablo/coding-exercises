"""
1448. Count Good Nodes in Binary Tree

Given a binary tree root,
a node X in the tree is named good if
in the path from root to X there are no nodes with
a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path
starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0

        def helper(node, tracking_max):
            nonlocal counter
            if not node:
                return

            if node.val >= tracking_max:
                counter += 1
                tracking_max = node.val

            helper(node.left, tracking_max)
            helper(node.right, tracking_max)

        helper(root, float("-inf"))

        return counter


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from problem description
    # Tree structure: [3,1,4,3,null,1,5]
    #       3
    #      / \
    #     1   4
    #    /   / \
    #   3   1   5
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)

    result1 = solution.goodNodes(root1)
    print(f"Test case 1: {result1}")  # Expected: 4
    assert result1 == 4, f"Expected 4, but got {result1}"

    # Test case 2: Single path with increasing values
    # Tree structure: [3,3,null,4,2]
    #       3
    #      /
    #     3
    #    / \
    #   4   2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)

    result2 = solution.goodNodes(root2)
    print(f"Test case 2: {result2}")  # Expected: 3
    assert result2 == 3, f"Expected 3, but got {result2}"

    print("All test cases passed!")

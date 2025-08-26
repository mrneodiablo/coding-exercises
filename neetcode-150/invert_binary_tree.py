"""
Invert Binary Tree
Given the root of a binary tree,
invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

from typing import Optional
import unittest


# Helper functions for testing
def create_tree_from_list(values):
    """Create a binary tree from a list representation (level-order)"""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    """Convert binary tree to list representation (level-order)"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(current_node):
            if not current_node:
                return None

            left = dfs(current_node.left)
            right = dfs(current_node.right)

            current_node.left = right
            current_node.right = left

            return current_node

        return dfs(root)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    # def test_run_1(self):
    #     # Test case 1: Standard example from problem
    #     # Input: [4,2,7,1,3,6,9] -> Output: [4,7,2,9,6,3,1]
    #     root = create_tree_from_list([4, 2, 7, 1, 3, 6, 9])
    #     expected = [4, 7, 2, 9, 6, 3, 1]

    #     result_root = self.solution.invertTree(root)
    #     result = tree_to_list(result_root)

    #     self.assertEqual(
    #         result,
    #         expected,
    #         f"incorrect, expect is {expected}"
    #     )

    def test_run_2(self):
        # Test case 2: Simple tree with 3 nodes
        # Input: [2,1,3] -> Output: [2,3,1]
        root = create_tree_from_list([2, 1, 3])
        expected = [2, 3, 1]

        result_root = self.solution.invertTree(root)
        result = tree_to_list(result_root)

        self.assertEqual(result, expected, f"incorrect, expect is {expected}")

    # def test_run_3(self):
    #     # Test case 3: Empty tree (edge case)
    #     # Input: [] -> Output: []
    #     root = None
    #     expected = []

    #     result_root = self.solution.invertTree(root)
    #     result = tree_to_list(result_root) if result_root else []

    #     self.assertEqual(
    #         result,
    #         expected,
    #         f"incorrect, expect is {expected}"
    #     )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

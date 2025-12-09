"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
Example 2:
    Input: root = [1,null,2]
    Output: 2
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if node is None, depth is 0
        if not root:
            return 0

        # Recursive case: 1 + max depth of left and right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def build_tree_from_list(vals):
    """Helper function to build a binary tree from a list representation"""
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


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem - balanced tree
        # Tree: [3,9,20,None,None,15,7]
        #       3
        #      / \
        #     9   20
        #        /  \
        #       15   7
        root = build_tree_from_list([3, 9, 20, None, None, 15, 7])
        expected = 3
        result = self.solution.maxDepth(root)
        self.assertEqual(result,
                         expected,
                         f"Expected depth {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Right-skewed tree
        # Tree: [1,None,2]
        #   1
        #    \
        #     2
        root = build_tree_from_list([1, None, 2])
        expected = 2
        result = self.solution.maxDepth(root)
        self.assertEqual(result,
                         expected,
                         f"Expected depth {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: Single node tree
        # Tree: [5]
        root = build_tree_from_list([5])
        expected = 1
        result = self.solution.maxDepth(root)
        self.assertEqual(result,
                         expected,
                         f"Expected depth {expected}, got {result}")


def test_max_depth():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Balanced tree [3,9,20,None,None,15,7]")
    root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    expected1 = 3
    result1 = solution.maxDepth(root1)
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Right-skewed tree [1,None,2]")
    root2 = build_tree_from_list([1, None, 2])
    expected2 = 2
    result2 = solution.maxDepth(root2)
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Single node [5]")
    root3 = build_tree_from_list([5])
    expected3 = 1
    result3 = solution.maxDepth(root3)
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Empty tree []")
    root4 = build_tree_from_list([])
    expected4 = 0
    result4 = solution.maxDepth(root4)
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Left-skewed tree")
    # Manually create [1,2,None,3,None,None,None]
    #     1
    #    /
    #   2
    #  /
    # 3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    expected5 = 3
    result5 = solution.maxDepth(root5)
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxDepth)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_max_depth()

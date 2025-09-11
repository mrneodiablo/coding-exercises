"""
Binary Tree Right Side View
Given the root of a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
"""

# Definition for a binary tree node.
from typing import List, Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self,
                      root: Optional[TreeNode]) -> List[int]:

        right_side_out = []

        def dfs(node, level):
            if not node:
                return

            if len(right_side_out) == level:
                right_side_out.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return right_side_out


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


class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Example from problem description
        # Tree: [1,2,3,null,5,null,4]
        #       1
        #      / \
        #     2   3
        #      \   \
        #       5   4
        # Right side view: [1, 3, 4]
        root = build_tree_from_list([1, 2, 3, None, 5, None, 4])
        expected = [1, 3, 4]
        result = self.solution.rightSideView(root)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Right-skewed tree
        # Tree: [1,null,3]
        #   1
        #    \
        #     3
        # Right side view: [1, 3]
        root = build_tree_from_list([1, None, 3])
        expected = [1, 3]
        result = self.solution.rightSideView(root)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: Empty tree
        # Tree: []
        # Right side view: []
        root = build_tree_from_list([])
        expected = []
        result = self.solution.rightSideView(root)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_right_side_view():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Example tree [1,2,3,null,5,null,4]")
    root1 = build_tree_from_list([1, 2, 3, None, 5, None, 4])
    expected1 = [1, 3, 4]
    result1 = solution.rightSideView(root1)
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Right-skewed tree [1,null,3]")
    root2 = build_tree_from_list([1, None, 3])
    expected2 = [1, 3]
    result2 = solution.rightSideView(root2)
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Empty tree []")
    root3 = build_tree_from_list([])
    expected3 = []
    result3 = solution.rightSideView(root3)
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Single node [1]")
    root4 = build_tree_from_list([1])
    expected4 = [1]
    result4 = solution.rightSideView(root4)
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: Left-skewed tree [1,2,null,3]")
    # Tree:   1
    #        /
    #       2
    #      /
    #     3
    # Right side view: [1, 2, 3] (leftmost nodes at each level)
    root5 = build_tree_from_list([1, 2, None, 3])
    expected5 = [1, 2, 3]
    result5 = solution.rightSideView(root5)
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRightSideView)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_right_side_view()

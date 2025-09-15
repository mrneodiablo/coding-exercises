"""
Same Tree

Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.



Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.right, q.right)
                and
                self.isSameTree(p.left, q.left))


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


class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        # Test case 1: Identical trees - Example 1 from problem
        # Trees: p = [1,2,3], q = [1,2,3]
        #    1       1
        #   / \     / \
        #  2   3   2   3
        p = build_tree_from_list([1, 2, 3])
        q = build_tree_from_list([1, 2, 3])
        expected = True
        result = self.solution.isSameTree(p, q)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_2(self):
        # Test case 2: Different structure - Example 2 from problem
        # Trees: p = [1,2], q = [1,null,2]
        #  1     1
        # /       \
        # 2         2
        p = build_tree_from_list([1, 2])
        q = build_tree_from_list([1, None, 2])
        expected = False
        result = self.solution.isSameTree(p, q)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")

    def test_run_3(self):
        # Test case 3: Both trees are empty
        # Trees: p = [], q = []
        p = build_tree_from_list([])
        q = build_tree_from_list([])
        expected = True
        result = self.solution.isSameTree(p, q)
        self.assertEqual(result,
                         expected,
                         f"Expected {expected}, got {result}")


def test_same_tree():
    """Alternative test function for manual testing"""
    solution = Solution()

    print("Test 1: Identical trees [1,2,3] vs [1,2,3]")
    p1 = build_tree_from_list([1, 2, 3])
    q1 = build_tree_from_list([1, 2, 3])
    expected1 = True
    result1 = solution.isSameTree(p1, q1)
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    print(f"  ✅ {'PASSED' if result1 == expected1 else 'FAILED'}")
    print()

    print("Test 2: Different structure [1,2] vs [1,null,2]")
    p2 = build_tree_from_list([1, 2])
    q2 = build_tree_from_list([1, None, 2])
    expected2 = False
    result2 = solution.isSameTree(p2, q2)
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    print(f"  ✅ {'PASSED' if result2 == expected2 else 'FAILED'}")
    print()

    print("Test 3: Both empty trees [] vs []")
    p3 = build_tree_from_list([])
    q3 = build_tree_from_list([])
    expected3 = True
    result3 = solution.isSameTree(p3, q3)
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    print(f"  ✅ {'PASSED' if result3 == expected3 else 'FAILED'}")
    print()

    print("Test 4: Different values [1,2,1] vs [1,1,2]")
    p4 = build_tree_from_list([1, 2, 1])
    q4 = build_tree_from_list([1, 1, 2])
    expected4 = False
    result4 = solution.isSameTree(p4, q4)
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    print(f"  ✅ {'PASSED' if result4 == expected4 else 'FAILED'}")
    print()

    print("Test 5: One empty, one not [] vs [1]")
    p5 = build_tree_from_list([])
    q5 = build_tree_from_list([1])
    expected5 = False
    result5 = solution.isSameTree(p5, q5)
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    print(f"  ✅ {'PASSED' if result5 == expected5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSameTree)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Or run manual tests
    # test_same_tree()

"""
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of
a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Example 1:
    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
    Output: true

Example 2:
    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
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

        return (self.isSameTree(p.right, q.right) and
                self.isSameTree(p.left, q.left))

    def isSubtree(self,
                  root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        # Một cây rỗng luôn là subtree của bất kỳ cây nào
        if not subRoot:
            return True

        # Nếu root rỗng và subtree không rỗng
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from
        problem description - True case"""
        # root = [3,4,5,1,2], subRoot = [4,1,2]
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)

        result = self.solution.isSubtree(root, subRoot)
        self.assertTrue(result)

    def test_run_2(self):
        """Test case 2: Example from problem description - False case"""
        # root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)

        result = self.solution.isSubtree(root, subRoot)
        self.assertFalse(result)

    def test_run_3(self):
        """Test case 3: Edge case - Empty subRoot"""
        # root = [1,2,3], subRoot = None
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        subRoot = None

        result = self.solution.isSubtree(root, subRoot)
        self.assertTrue(result)


def create_tree_from_list(values):
    """Helper function to create tree from list representation"""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root):
    """Helper function to convert tree to list for visualization"""
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

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("SUBTREE OF ANOTHER TREE - TEST CASES")
    print("=" * 50)

    # Test 1: Example from problem description - True case
    print("Test 1: Example from problem description - True case")
    root1 = create_tree_from_list([3, 4, 5, 1, 2])
    subRoot1 = create_tree_from_list([4, 1, 2])
    expected1 = True
    result1 = solution.isSubtree(root1, subRoot1)

    print(f"  Root tree: {tree_to_list(root1)}")
    print(f"  SubRoot tree: {tree_to_list(subRoot1)}")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    passed1 = result1 == expected1
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Example from problem description - False case
    print("Test 2: Example from problem description - False case")
    root2 = create_tree_from_list([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot2 = create_tree_from_list([4, 1, 2])
    expected2 = False
    result2 = solution.isSubtree(root2, subRoot2)

    print(f"  Root tree: {tree_to_list(root2)}")
    print(f"  SubRoot tree: {tree_to_list(subRoot2)}")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    passed2 = result2 == expected2
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Edge case - Empty subRoot
    print("Test 3: Edge case - Empty subRoot")
    root3 = create_tree_from_list([1, 2, 3])
    subRoot3 = None
    expected3 = True
    result3 = solution.isSubtree(root3, subRoot3)

    print(f"  Root tree: {tree_to_list(root3)}")
    print(f"  SubRoot tree: {subRoot3}")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Single node trees
    print("Test 4: Single node trees")
    root4 = create_tree_from_list([1])
    subRoot4 = create_tree_from_list([1])
    expected4 = True
    result4 = solution.isSubtree(root4, subRoot4)

    print(f"  Root tree: {tree_to_list(root4)}")
    print(f"  SubRoot tree: {tree_to_list(subRoot4)}")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    passed4 = result4 == expected4
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: SubRoot larger than any subtree
    print("Test 5: SubRoot larger than any subtree")
    root5 = create_tree_from_list([1, 2])
    subRoot5 = create_tree_from_list([1, 2, 3])
    expected5 = False
    result5 = solution.isSubtree(root5, subRoot5)

    print(f"  Root tree: {tree_to_list(root5)}")
    print(f"  SubRoot tree: {tree_to_list(subRoot5)}")
    print(f"  Expected: {expected5}")
    print(f"  Got:      {result5}")
    passed5 = result5 == expected5
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 50)
    print("MANUAL TEST RESULTS")
    print("=" * 50)

    # Run manual tests
    manual_test()

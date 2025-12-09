"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where
preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
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
    def buildTree(self,
                  preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:

        root_index = 0

        inorder_index_map = ({
            element: idx for idx, element in enumerate(inorder)}
            )

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal root_index

            if in_left > in_right:
                return None

            root_val = preorder[root_index]
            node = TreeNode(root_val)

            root_index += 1

            index = inorder_index_map[root_val]

            node.left = helper(in_left, index - 1)
            node.right = helper(index + 1, in_right)

            return node

        return helper(0, len(preorder) - 1)


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Convert tree to list representation for easy comparison"""
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


def create_tree_from_list(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """Create tree from list representation"""
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while queue and i < len(arr):
        node = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Get inorder traversal for verification"""
    if not root:
        return []
    return (inorder_traversal(root.left) +
            [root.val] +
            inorder_traversal(root.right))


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Get preorder traversal for verification"""
    if not root:
        return []
    return ([root.val] +
            preorder_traversal(root.left) +
            preorder_traversal(root.right))


class TestConstructBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description"""
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = [3, 9, 20, None, None, 15, 7]

        result = self.solution.buildTree(preorder, inorder)
        result_list = tree_to_list(result)

        # Verify the tree structure matches expected
        self.assertEqual(result_list, expected)

        # Verify traversals match input
        self.assertEqual(preorder_traversal(result), preorder)
        self.assertEqual(inorder_traversal(result), inorder)

    def test_run_2(self):
        """Test case 2: Single node tree"""
        preorder = [-1]
        inorder = [-1]
        expected = [-1]

        result = self.solution.buildTree(preorder, inorder)
        result_list = tree_to_list(result)

        self.assertEqual(result_list, expected)
        self.assertEqual(preorder_traversal(result), preorder)
        self.assertEqual(inorder_traversal(result), inorder)

    def test_run_3(self):
        """Test case 3: Left-heavy tree"""
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        expected = [1, 2, None, 3]

        result = self.solution.buildTree(preorder, inorder)
        result_list = tree_to_list(result)

        self.assertEqual(result_list, expected)
        self.assertEqual(preorder_traversal(result), preorder)
        self.assertEqual(inorder_traversal(result), inorder)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 60)
    print("CONSTRUCT BINARY TREE FROM PREORDER AND INORDER TRAVERSAL")
    print("=" * 60)

    # Test 1: Example from problem description
    print("Test 1: Example from problem description")
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    expected1 = [3, 9, 20, None, None, 15, 7]
    result1 = solution.buildTree(preorder1, inorder1)
    result1_list = tree_to_list(result1)

    print(f"  Preorder:  {preorder1}")
    print(f"  Inorder:   {inorder1}")
    print(f"  Expected:  {expected1}")
    print(f"  Got:       {result1_list}")
    print("  Tree structure:")
    print("       3")
    print("      / \\")
    print("     9  20")
    print("       /  \\")
    print("      15   7")

    passed1 = (
        result1_list == expected1
        and preorder_traversal(result1) == preorder1
        and inorder_traversal(result1) == inorder1
    )
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Single node tree
    print("Test 2: Single node tree")
    preorder2 = [-1]
    inorder2 = [-1]
    expected2 = [-1]
    result2 = solution.buildTree(preorder2, inorder2)
    result2_list = tree_to_list(result2)

    print(f"  Preorder:  {preorder2}")
    print(f"  Inorder:   {inorder2}")
    print(f"  Expected:  {expected2}")
    print(f"  Got:       {result2_list}")
    print("  Tree structure: -1")

    passed2 = (
        result2_list == expected2
        and preorder_traversal(result2) == preorder2
        and inorder_traversal(result2) == inorder2
    )
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Left-heavy tree
    print("Test 3: Left-heavy tree")
    preorder3 = [1, 2, 3]
    inorder3 = [3, 2, 1]
    expected3 = [1, 2, None, 3]
    result3 = solution.buildTree(preorder3, inorder3)
    result3_list = tree_to_list(result3)

    print(f"  Preorder:  {preorder3}")
    print(f"  Inorder:   {inorder3}")
    print(f"  Expected:  {expected3}")
    print(f"  Got:       {result3_list}")
    print("  Tree structure:")
    print("     1")
    print("    /")
    print("   2")
    print("  /")
    print(" 3")

    passed3 = (
        result3_list == expected3
        and preorder_traversal(result3) == preorder3
        and inorder_traversal(result3) == inorder3
    )
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Right-heavy tree
    print("Test 4: Right-heavy tree")
    preorder4 = [1, 2, 3]
    inorder4 = [1, 2, 3]
    expected4 = [1, None, 2, None, 3]
    result4 = solution.buildTree(preorder4, inorder4)
    result4_list = tree_to_list(result4)

    print(f"  Preorder:  {preorder4}")
    print(f"  Inorder:   {inorder4}")
    print(f"  Expected:  {expected4}")
    print(f"  Got:       {result4_list}")
    print("  Tree structure:")
    print("  1")
    print("   \\")
    print("    2")
    print("     \\")
    print("      3")

    passed4 = (
        result4_list == expected4
        and preorder_traversal(result4) == preorder4
        and inorder_traversal(result4) == inorder4
    )
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: Balanced tree
    print("Test 5: Balanced tree")
    preorder5 = [1, 2, 4, 5, 3, 6, 7]
    inorder5 = [4, 2, 5, 1, 6, 3, 7]
    expected5 = [1, 2, 3, 4, 5, 6, 7]
    result5 = solution.buildTree(preorder5, inorder5)
    result5_list = tree_to_list(result5)

    print(f"  Preorder:  {preorder5}")
    print(f"  Inorder:   {inorder5}")
    print(f"  Expected:  {expected5}")
    print(f"  Got:       {result5_list}")
    print("  Tree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")

    passed5 = (
        result5_list == expected5
        and preorder_traversal(result5) == preorder5
        and inorder_traversal(result5) == inorder5
    )
    print(f"  ✅ {'PASSED' if passed5 else 'FAILED'}")


if __name__ == "__main__":
    # Run unittest cases
    unittest.main(argv=[""], verbosity=2, exit=False)

    print("\n" + "=" * 60)
    print("MANUAL TEST RESULTS")
    print("=" * 60)

    # Run manual tests
    manual_test()

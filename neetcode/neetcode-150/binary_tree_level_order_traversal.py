"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree,
return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
Example 2:
    Input: root = [1]
    Output: [[1]]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def dfs(node: TreeNode, level: int):

            if not node:
                return

            if len(output) == level:
                output.append([])

            output[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return output


def create_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to create binary tree from list representation"""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Helper function to convert
    binary tree to list representation"""
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


class TestBinaryTreeLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_run_1(self):
        """Test case 1: Example from problem description"""
        # Tree: [3,9,20,null,null,15,7]
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        tree_list = [3, 9, 20, None, None, 15, 7]
        root = create_tree_from_list(tree_list)
        expected = [[3], [9, 20], [15, 7]]
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)

    def test_run_2(self):
        """Test case 2: Single node tree"""
        tree_list = [1]
        root = create_tree_from_list(tree_list)
        expected = [[1]]
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)

    def test_run_3(self):
        """Test case 3: Empty tree"""
        root = None
        expected = []
        result = self.solution.levelOrder(root)
        self.assertEqual(result, expected)


def manual_test():
    """Manual testing with detailed output"""
    solution = Solution()

    print("=" * 50)
    print("BINARY TREE LEVEL ORDER TRAVERSAL - TEST CASES")
    print("=" * 50)

    # Test 1: Example from problem description
    print("Test 1: Example from problem description")
    tree_list1 = [3, 9, 20, None, None, 15, 7]
    root1 = create_tree_from_list(tree_list1)
    expected1 = [[3], [9, 20], [15, 7]]
    result1 = solution.levelOrder(root1)

    print(f"  Input tree: {tree_list1}")
    print("  Tree structure:")
    print("       3")
    print("      / \\")
    print("     9  20")
    print("       /  \\")
    print("      15   7")
    print(f"  Expected: {expected1}")
    print(f"  Got:      {result1}")
    passed1 = result1 == expected1
    print(f"  ✅ {'PASSED' if passed1 else 'FAILED'}")
    print()

    # Test 2: Single node tree
    print("Test 2: Single node tree")
    tree_list2 = [1]
    root2 = create_tree_from_list(tree_list2)
    expected2 = [[1]]
    result2 = solution.levelOrder(root2)

    print(f"  Input tree: {tree_list2}")
    print("  Tree structure: 1")
    print(f"  Expected: {expected2}")
    print(f"  Got:      {result2}")
    passed2 = result2 == expected2
    print(f"  ✅ {'PASSED' if passed2 else 'FAILED'}")
    print()

    # Test 3: Empty tree
    print("Test 3: Empty tree")
    root3 = None
    expected3 = []
    result3 = solution.levelOrder(root3)

    print("  Input tree: None")
    print("  Tree structure: (empty)")
    print(f"  Expected: {expected3}")
    print(f"  Got:      {result3}")
    passed3 = result3 == expected3
    print(f"  ✅ {'PASSED' if passed3 else 'FAILED'}")
    print()

    # Test 4: Unbalanced tree
    print("Test 4: Unbalanced tree (left-heavy)")
    tree_list4 = [1, 2, None, 3, None, 4]
    root4 = create_tree_from_list(tree_list4)
    expected4 = [[1], [2], [3], [4]]
    result4 = solution.levelOrder(root4)

    print(f"  Input tree: {tree_list4}")
    print("  Tree structure:")
    print("    1")
    print("   /")
    print("  2")
    print(" /")
    print("3")
    print(" \\")
    print("  4")
    print(f"  Expected: {expected4}")
    print(f"  Got:      {result4}")
    passed4 = result4 == expected4
    print(f"  ✅ {'PASSED' if passed4 else 'FAILED'}")
    print()

    # Test 5: Complete binary tree
    print("Test 5: Complete binary tree")
    tree_list5 = [1, 2, 3, 4, 5, 6, 7]
    root5 = create_tree_from_list(tree_list5)
    expected5 = [[1], [2, 3], [4, 5, 6, 7]]
    result5 = solution.levelOrder(root5)

    print(f"  Input tree: {tree_list5}")
    print("  Tree structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\ / \\")
    print("   4  5 6  7")
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

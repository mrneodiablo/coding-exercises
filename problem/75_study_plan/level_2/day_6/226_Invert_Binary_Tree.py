# Definition for a binary tree node.
from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    output = []

    def dfs(root):
        if root:
            output.append(root.val)
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return output


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return (
            TreeNode(
                root.val,
                right=self.invertTree(root.left),
                left=self.invertTree(root.right),
            )
            if root
            else None
        )


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            4,
            left=TreeNode(2, TreeNode(1), TreeNode(3)),
            right=TreeNode(7, TreeNode(6), TreeNode(9)),
        )
        expect = [4, 7, 9, 6, 2, 3, 1]
        tmp = preorderTraversal(self.solution.invertTree(root))
        self.assertEqual(str(tmp),
                         str(expect),
                         "incorrect, expect is " + str(expect))

    def test_run_2(self):
        # test case
        root = TreeNode(
            1,
            left=TreeNode(2),
            right=None,
        )
        expect = [1, 2]
        self.assertEqual(
            str(preorderTraversal(self.solution.invertTree(root))),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

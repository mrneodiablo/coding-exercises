# Definition for a binary tree node.
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        def compareH(node):
            if node is None:
                return 1
            dr = compareH(node.right)
            if dr == 0:
                return 0
            dl = compareH(node.left)
            if dl == 0:
                return 0
            if abs(dr - dl) > 1:
                return 0
            return max(dr, dl) + 1

        return compareH(root) != 0


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            3,
            left=TreeNode(9),
            right=TreeNode(20, TreeNode(15), TreeNode(7)),
        )
        expect = True
        self.assertEqual(
            str(self.solution.isBalanced(root)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        root = TreeNode(
            1,
            left=TreeNode(2,
                          left=TreeNode(4,
                                        left=TreeNode(8)), right=TreeNode(5)),
            right=TreeNode(3,
                           left=TreeNode(6)),
        )
        expect = True
        self.assertEqual(
            str(self.solution.isBalanced(root)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

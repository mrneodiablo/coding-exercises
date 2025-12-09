from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        return arr == list(sorted(set(arr)))


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        tree = TreeNode(2, TreeNode(1), TreeNode(3))
        expect = True
        self.assertEqual(
            self.solution.isValidBST(tree),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        tree = TreeNode(
            5,
            TreeNode(1),
            TreeNode(
                4,
                TreeNode(3),
                TreeNode(6),
            ),
        )
        expect = False
        self.assertEqual(
            self.solution.isValidBST(tree),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_3(self):
        # test case
        tree = TreeNode(0)
        expect = True
        self.assertEqual(
            self.solution.isValidBST(tree),
            expect,
            "incorrect, expect is " + str(expect),
        )

    def test_run_4(self):
        # test case
        tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
        expect = False
        self.assertEqual(
            self.solution.isValidBST(tree),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

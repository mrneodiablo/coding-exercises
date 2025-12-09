import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def LCA(node, x, y):
            if x.val < node.val and y.val < node.val:
                return LCA(node.left, x, y)
            if x.val > node.val and y.val > node.val:
                return LCA(node.right, x, y)
            return node

        return LCA(root, p, q)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        tree = TreeNode(
            6,
            TreeNode(
                2,
                TreeNode(0),
                TreeNode(
                    4,
                    TreeNode(3),
                    TreeNode(5),
                ),
            ),
            TreeNode(8, TreeNode(7), TreeNode(9)),
        )
        p = TreeNode(
            2,
            TreeNode(0),
            TreeNode(
                4,
                TreeNode(3),
                TreeNode(5),
            ),
        )
        q = TreeNode(
            4,
            TreeNode(3),
            TreeNode(5),
        )

        expect = 2
        self.assertEqual(
            self.solution.lowestCommonAncestor(tree, p, q).val,
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        out = True

        def bfs(root_p=p, root_q=q):
            nonlocal out
            if root_p or root_q:
                if root_p is None or root_q is None:
                    out = False
                    return

                if root_p is not None and root_q is not None:
                    if root_p.val != root_q.val:
                        out = False
                        return
                    bfs(root_p.left, root_q.left)
                    bfs(root_p.right, root_q.right)

        bfs()
        return out


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        # tree = [3,9,20,null,null,15,7]
        tree_1 = TreeNode(
            3,
            TreeNode(9,
                     TreeNode(1),
                     TreeNode(10)
                     ),
            TreeNode(20,
                     TreeNode(15),
                     TreeNode(7),
                     ),
        )
        tree_2 = TreeNode(
            3,
            TreeNode(9,
                     TreeNode(1),
                     TreeNode(10)
                     ),
            TreeNode(20,
                     TreeNode(15),
                     TreeNode(7),
                     ),
        )
        expect = True
        self.assertEqual(
            self.solution.isSameTree(tree_1, tree_2),
            expect,
            "incorrect, expect is " + str(expect)
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

# Definition for a binary tree node.
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0  # variable to store the maximum diameter found so far

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right)  # update ans if new diameter is found
            # return the maximum height of the node
            return max(left, right) + 1

        dfs(root)
        return ans


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
            right=TreeNode(3),
        )
        expect = 3
        self.assertEqual(
            str(self.solution.diameterOfBinaryTree(root)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

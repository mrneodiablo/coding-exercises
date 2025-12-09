# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # prefix sums encountered in current path
        sumHash = defaultdict(int)
        sumHash[0] = 1

        def dfs(root, prefixSum):
            count = 0
            if root:

                # Sum of current path
                prefixSum += root.val

                # number of paths that ends at current node
                count = sumHash[prefixSum - targetSum]

                # Add value of this prefixSum
                sumHash[prefixSum] += 1

                # Explore children
                count += dfs(root.left, prefixSum) + dfs(root.right, prefixSum)
                # Remove value of this prefixSum (path's been explored)
                sumHash[prefixSum] -= 1

            return count

        return dfs(root, 0)


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        root = TreeNode(
            10,
            left=TreeNode(
                5,
                left=TreeNode(3, left=TreeNode(3), right=TreeNode(-2)),
                right=TreeNode(2, left=None, right=TreeNode(1)),
            ),
            right=TreeNode(-3, left=None, right=TreeNode(11)),
        )
        targetSum = 8
        expect = 3
        self.assertEqual(
            self.solution.pathSum(root, targetSum),
            expect,
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

from typing import List, Optional
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node],
            left=self.sortedArrayToBST(nums[:mid_node]),
            right=self.sortedArrayToBST(nums[mid_node + 1:]),
        )


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        nums = [-10, -3, 0, 5, 9]
        expect = [0, -3, -10, 9, 5]
        self.assertEqual(
            str(preorderTraversal(self.solution.sortedArrayToBST(nums))),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

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

        def bfs(curr=root, level=0):
            if curr:
                if len(output) > level:
                    output[level].append(curr.val)
                else:
                    output.append([curr.val])
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)

        bfs()
        return output


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        # tree = [3,9,20,null,null,15,7]
        tree = TreeNode(
            3,
            TreeNode(9, TreeNode(1), TreeNode(10)),
            TreeNode(
                20,
                TreeNode(15),
                TreeNode(7),
            ),
        )

        expect = [[3], [9, 20], [1, 10, 15, 7]]
        self.assertEqual(
            str(self.solution.levelOrder(tree)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

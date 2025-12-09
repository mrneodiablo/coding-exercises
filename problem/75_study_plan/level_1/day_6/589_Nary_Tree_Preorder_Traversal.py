# Definition for a Node.
from typing import List
import unittest


class Node:
    def __init__(self, val=None, children: List = []):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        preorder_result = []

        def helper(curr=root):
            if curr:
                preorder_result.append(curr.val)
                for i in curr.children:
                    helper(i)

        helper()
        return preorder_result


class TestFunctions(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_run_1(self):
        # test case
        # root = [1,null,3,2,4,null,5,6]
        root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

        expect = [1, 3, 5, 6, 2, 4]
        self.assertEqual(
            str(self.solution.preorder(root)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )

    def test_run_2(self):
        # test case
        # root = [1,null,2,3,4,5,null,null,6,7,null,8,null,
        # 9,10,null,null,11,null,12,null,13,null,null,14
        # ]
        root = Node(
            1,
            [
                Node(2),
                Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
                Node(4, [Node(8, [Node(12)])]),
                Node(5, [Node(9, [Node(13)]), Node(10)]),
            ],
        )

        expect = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
        self.assertEqual(
            str(self.solution.preorder(root)),
            str(expect),
            "incorrect, expect is " + str(expect),
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

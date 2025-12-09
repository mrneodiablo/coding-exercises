import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def kth_smallest(self, kth) -> int:
        # # solution 1
        # # create a stack to hold nodes
        # stack = []
        # # start at the root of the tree
        # temp = self.root
        # while stack or temp:
        #     # get to left node
        #     while temp:
        #         stack.append(temp)
        #         temp = temp.left

        #     # pop the last node added to the stack
        #     temp = stack.pop()
        #     kth -= 1

        #     # return data
        #     if kth == 0:
        #         return temp.value

        #     # move to the right child of the node
        #     temp = temp.right
        # # if k is greater than the number of nodes in the tree, return None
        # return None

        # solution 2
        values = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            values.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)

        if self.root is None:
            return None

        traversal(self.root)

        if kth <= 0 or kth > len(values):
            return None

        return values[kth - 1]


class TestFunctions(unittest.TestCase):

    def test_basic_kth_smallest(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.insert(6)
        bst.insert(8)

        self.assertEqual(bst.kth_smallest(1), 2, "1st smallest should be 2")
        self.assertEqual(bst.kth_smallest(3), 4, "3rd smallest should be 4")
        self.assertEqual(bst.kth_smallest(5), 6, "5th smallest should be 6")
        self.assertEqual(bst.kth_smallest(7), 8, "7th smallest should be 8")

    def test_invalid_k(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)

        self.assertEqual(bst.kth_smallest(0), None, "k = 0 should return None")
        self.assertEqual(bst.kth_smallest(-1), None, "k = -1 should return None")
        self.assertEqual(
            bst.kth_smallest(10), None, "k out of bounds should return None"
        )

    def test_empty_tree(self):
        empty_bst = BinarySearchTree()
        self.assertEqual(
            empty_bst.kth_smallest(1), None, "Empty tree should return None"
        )

    def test_single_node(self):
        single_bst = BinarySearchTree()
        single_bst.insert(42)

        self.assertEqual(
            single_bst.kth_smallest(1), 42, "1st smallest in single node tree"
        )
        self.assertEqual(
            single_bst.kth_smallest(2), None, "2nd smallest should be None"
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)


"""
    EXPECTED OUTPUT:
    ----------------
    All tests should pass with kth_smallest working correctly
 """

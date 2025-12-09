
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

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __dfs_preorder_helper(self, current_node):
        parent = []
        child_left = []
        child_right = []

        if current_node is not None:
            parent = [current_node.value]

            if current_node.left:
                child_left = self.__dfs_preorder_helper(current_node.left)

            if current_node.right:
                child_right = self.__dfs_preorder_helper(current_node.right)

        return parent + child_left + child_right

    def __dfs_postorder_helper(self, current_node):
        parent = []
        child_left = []
        child_right = []

        if current_node is not None:
            parent = [current_node.value]

            if current_node.left:
                child_left = self.__dfs_postorder_helper(current_node.left)

            if current_node.right:
                child_right = self.__dfs_postorder_helper(current_node.right)

        return child_left + child_right + parent

    def __dfs_inorder_helper(self, current_node):
        parent = []
        child_left = []
        child_right = []

        if current_node is not None:
            parent = [current_node.value]

            if current_node.left:
                child_left = self.__dfs_inorder_helper(current_node.left)

            if current_node.right:
                child_right = self.__dfs_inorder_helper(current_node.right)

        return child_left + parent + child_right

    def dfs_pre_order(self) -> list:
        # [root] + [left ++ ] + [right ++ ]
        result = self.__dfs_preorder_helper(self.root)
        return result

    def dfs_post_order(self) -> list:
        # [left ++ ] + [right ++ ] + [root]
        result = self.__dfs_postorder_helper(self.root)
        return result

    def dfs_in_order(self) -> list:
        # [left ++ ] + [right ++ ] + [root]
        result = self.__dfs_inorder_helper(self.root)
        return result


class TestFunctions(unittest.TestCase):

    def test_dfs_pre_order(self):
        my_tree = BinarySearchTree()
        my_tree.insert(47)
        my_tree.insert(21)
        my_tree.insert(76)
        my_tree.insert(18)
        my_tree.insert(27)
        my_tree.insert(52)
        my_tree.insert(82)

        expect = [47, 21, 18, 27, 76, 52, 82]
        self.assertEqual(
            my_tree.dfs_pre_order(),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_dfs_post_order(self):
        my_tree = BinarySearchTree()
        my_tree.insert(47)
        my_tree.insert(21)
        my_tree.insert(76)
        my_tree.insert(18)
        my_tree.insert(27)
        my_tree.insert(52)
        my_tree.insert(82)

        expect = [18, 27, 21, 52, 82, 76, 47]
        self.assertEqual(
            my_tree.dfs_post_order(),
            expect,
            f"incorrect, expect is {expect}",
        )

    def test_dfs_in_order(self):
        my_tree = BinarySearchTree()
        my_tree.insert(47)
        my_tree.insert(21)
        my_tree.insert(76)
        my_tree.insert(18)
        my_tree.insert(27)
        my_tree.insert(52)
        my_tree.insert(82)

        expect = [18, 21, 27, 47, 52, 76, 82]
        self.assertEqual(
            my_tree.dfs_in_order(),
            expect,
            f"incorrect, expect is {expect}",
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)


"""
    EXPECTED OUTPUT:
    ----------------
    Pre-order: [47, 21, 18, 27, 76, 52, 82]
    Post-order: [18, 27, 21, 52, 82, 76, 47]
    In-order: [18, 21, 27, 47, 52, 76, 82]
 """

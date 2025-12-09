import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min_value(self, current_node):
        # find min value in the tree start from current node
        # noted that min value always on
        # the left side. node.left.left.value = min
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def insert(self, value) -> bool:
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        parent = self.root
        while parent:
            if value > parent.value:
                if parent.right is None:
                    parent.right = new_node
                    break
                parent = parent.right
            elif value < parent.value:
                if parent.left is None:
                    parent.left = new_node
                    break
                parent = parent.left
            else:
                return False
        return True

    def __r_insert(self, current_node: Node, value: int) -> bool:
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node

    def __r_contains(self, current_node: Node, value: int) -> bool:
        if current_node is None:
            return False

        if value == current_node.value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def __delete_node(self, current_node, value):
        # check if current node la None thi return None mục đích là xoá node
        if current_node is None:
            return None

        if value < current_node.value:
            # traveser tới node cần xoá theo điều kiện nếu value bé hơn
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            # traveser tới node cần xoá theo điều kiện nếu value lớn hơn
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # nếu  current_node == value; node cần xoá

            # case 1 nếu node cần xoá current_node không có node con.
            # đơn giản return None để Gc tự xoá
            if current_node.left is None and current_node.right is None:
                return None

            # case 2 node cần xoá có 1 node con bên phải hoặc bên trái
            # thì node cần xoá là node bên còn lại
            if current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                # case 3 node cần xoá có 2 nodes con

                # tìm min của nhánh con bên phải
                # tại vì min của nhánh con bên phải lớn hơn max
                # của nhánh con bên trái
                # nhưng vẫn nhỏ hơn tất cả nhánh con bên phải

                sub_tree_min = self.min_value(current_node.right)
                # gán giá trị node cần xoá thành giá trị min nhánh con bên phải
                current_node.value = sub_tree_min

                # build lại nhánh con bên phải:
                # thật sự là gán lại giá trị do xoá node
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def r_contains(self, value: int):
        return self.__r_contains(self.root, value)

    def r_insert(self, value: int):
        self.root = self.__r_insert(self.root, value)

    def r_delete_node(self, value):
        # gán lại tree cho self.root để đảm bảo mọi thay đổi được link với nhau
        self.root = self.__delete_node(self.root, value)


class TestFunctions(unittest.TestCase):

    def test_contains_empty_tree(self):
        bst = BinarySearchTree()
        result = bst.r_contains(5)
        self.assertEqual(result, False, "Check if 5 exists in an empty tree")

    def test_contains_existing_value(self):
        bst = BinarySearchTree()
        bst.r_insert(10)
        bst.r_insert(5)
        bst.r_insert(15)
        bst.r_insert(20)

        self.assertEqual(bst.r_contains(10), True, "Check if 10 exists")
        self.assertEqual(bst.r_contains(5), True, "Check if 5 exists")
        self.assertEqual(bst.r_contains(15), True, "Check if 15 exists")
        self.assertEqual(bst.r_contains(20), True, "Check if 20 exists")

    def test_contains_not_existing_value(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        result = bst.r_contains(15)
        self.assertEqual(result, False, "Check if 15 exists")

    def test_delete_leaf_node(self):
        bst = BinarySearchTree()
        bst.r_insert(10)
        bst.r_insert(5)
        bst.r_insert(15)
        bst.r_insert(3)
        bst.r_insert(7)
        bst.r_delete_node(3)

        self.assertEqual(
            bst.r_contains(3), False, "Check if 3 still exists after deletion"
        )
        self.assertEqual(bst.r_contains(5), True, "Check if parent 5 still exists")
        self.assertEqual(bst.r_contains(7), True, "Check if sibling 7 still exists")

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        bst.r_insert(10)
        bst.r_insert(5)
        bst.r_insert(15)
        bst.r_insert(3)
        bst.r_insert(7)
        bst.r_insert(12)
        bst.r_insert(18)
        bst.r_delete_node(10)

        self.assertEqual(
            bst.r_contains(10), False, "Check if 10 still exists after deletion"
        )
        self.assertEqual(
            bst.r_contains(12), True, "Check if successor 12 is now the root"
        )
        self.assertEqual(bst.r_contains(5), True, "Check if left subtree still exists")
        self.assertEqual(
            bst.r_contains(15), True, "Check if right subtree still exists"
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

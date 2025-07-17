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


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


if __name__ == "__main__":

    print("\n----- Test: Contains on Empty Tree -----\n")
    bst = BinarySearchTree()
    result = bst.r_contains(5)
    check(False, result, "Check if 5 exists in an empty tree:")

    print("\n----- Test: Contains Existing Value -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(20)

    result = bst.r_contains(10)
    check(True, result, "Check if 10 exists:")
    result = bst.r_contains(5)
    check(True, result, "Check if 5 exists:")
    result = bst.r_contains(15)
    check(True, result, "Check if 15 exists:")
    result = bst.r_contains(20)
    check(True, result, "Check if 20 exists:")
    print("\n----- Test: Contains Not Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.r_contains(15)
    check(False, result, "Check if 15 exists:")

    print("\n----- Test: Contains with Duplicate Inserts -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    result = bst.r_contains(10)
    check(True, result, "Check if 10 exists with duplicate inserts:")

    print("\n----- Test: Contains with Left and Right -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(1)
    bst.insert(8)
    bst.insert(12)
    bst.insert(20)
    result = bst.r_contains(1)
    check(True, result, "Check if 1 exists:")
    result = bst.r_contains(8)
    check(True, result, "Check if 8 exists:")
    result = bst.r_contains(12)
    check(True, result, "Check if 12 exists:")
    result = bst.r_contains(20)
    check(True, result, "Check if 20 exists:")

    print("\n----- Test: Delete Leaf Node -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(3)
    bst.r_insert(7)
    print("Tree before deleting leaf node 3:")
    print("    10")
    print("   /  \\")
    print("  5    15")
    print(" / \\")
    print("3   7")
    bst.r_delete_node(3)
    result = bst.r_contains(3)
    check(False, result, "Check if 3 still exists after deletion:")
    result = bst.r_contains(5)
    check(True, result, "Check if parent 5 still exists:")
    result = bst.r_contains(7)
    check(True, result, "Check if sibling 7 still exists:")

    print("\n----- Test: Delete Node with Only Left Child -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(3)
    bst.r_insert(1)
    print("Tree before deleting node 3 (has only left child):")
    print("    10")
    print("   /  \\")
    print("  5    15")
    print(" /")
    print("3")
    print("/")
    print("1")
    bst.r_delete_node(3)
    result = bst.r_contains(3)
    check(False, result, "Check if 3 still exists after deletion:")
    result = bst.r_contains(1)
    check(True, result, "Check if child 1 still exists:")
    result = bst.r_contains(5)
    check(True, result, "Check if parent 5 still exists:")

    print("\n----- Test: Delete Node with Only Right Child -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(18)
    bst.r_insert(20)
    print("Tree before deleting node 18 (has only right child):")
    print("    10")
    print("   /  \\")
    print("  5    15")
    print("         \\")
    print("         18")
    print("          \\")
    print("          20")
    bst.r_delete_node(18)
    result = bst.r_contains(18)
    check(False, result, "Check if 18 still exists after deletion:")
    result = bst.r_contains(20)
    check(True, result, "Check if child 20 still exists:")
    result = bst.r_contains(15)
    check(True, result, "Check if parent 15 still exists:")

    print("\n----- Test: Delete Node with Two Children -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(3)
    bst.r_insert(7)
    bst.r_insert(12)
    bst.r_insert(18)
    bst.r_insert(6)
    bst.r_insert(8)
    bst.r_insert(11)
    bst.r_insert(13)
    print("Tree before deleting node 5 (has two children):")
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     / \\   / \\")
    print("    3   7 12 18")
    print("       / \\  /\\")
    print("      6  8 11 13")
    bst.r_delete_node(5)
    result = bst.r_contains(5)
    check(False, result, "Check if 5 still exists after deletion:")
    result = bst.r_contains(6)
    check(True, result, "Check if successor 6 is now in place of 5:")
    result = bst.r_contains(3)
    check(True, result, "Check if left child 3 still exists:")
    result = bst.r_contains(7)
    check(True, result, "Check if right child 7 still exists:")

    print("\n----- Test: Delete Root Node with Two Children -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(3)
    bst.r_insert(7)
    bst.r_insert(12)
    bst.r_insert(18)
    print("Tree before deleting root node 10:")
    print("    10")
    print("   /  \\")
    print("  5    15")
    print(" / \\   / \\")
    print("3   7 12 18")
    bst.r_delete_node(10)
    result = bst.r_contains(10)
    check(False, result, "Check if 10 still exists after deletion:")
    result = bst.r_contains(12)
    check(True, result, "Check if successor 12 is now the root:")
    result = bst.r_contains(5)
    check(True, result, "Check if left subtree still exists:")
    result = bst.r_contains(15)
    check(True, result, "Check if right subtree still exists:")

    print("\n----- Test: Delete Root Node (Only Node) -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_delete_node(10)
    result = bst.r_contains(10)
    check(False, result, "Check if 10 still exists after deletion:")
    result = bst.r_contains(5)
    check(False, result, "Check tree is empty - no other nodes exist:")

    print("\n----- Test: Delete Non-existing Node -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    # Try to delete a node that doesn't exist
    bst.r_delete_node(20)
    result = bst.r_contains(10)
    check(True, result, "Check if 10 still exists (tree unchanged):")
    result = bst.r_contains(5)
    check(True, result, "Check if 5 still exists (tree unchanged):")
    result = bst.r_contains(15)
    check(True, result, "Check if 15 still exists (tree unchanged):")

    print("\n----- Test: Delete from Empty Tree -----\n")
    bst = BinarySearchTree()
    # Try to delete from empty tree
    bst.r_delete_node(10)
    result = bst.r_contains(10)
    check(False, result, "Check tree is still empty:")

    print("\n----- Test: Multiple Consecutive Deletes -----\n")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(15)
    bst.r_insert(3)
    bst.r_insert(7)
    bst.r_insert(12)
    bst.r_insert(18)

    # Delete multiple nodes in sequence
    bst.r_delete_node(3)
    bst.r_delete_node(18)
    bst.r_delete_node(5)

    result = bst.r_contains(3)
    check(False, result, "Check if 3 was deleted:")
    result = bst.r_contains(18)
    check(False, result, "Check if 18 was deleted:")
    result = bst.r_contains(5)
    check(False, result, "Check if 5 was deleted:")
    result = bst.r_contains(10)
    check(True, result, "Check if 10 still exists:")
    result = bst.r_contains(7)
    check(True, result, "Check if 7 still exists:")
    result = bst.r_contains(12)
    check(True, result, "Check if 12 still exists:")
    result = bst.r_contains(15)
    check(True, result, "Check if 15 still exists:")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

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

    def r_contains(self, value: int):
        return self.__r_contains(self.root, value)

    def r_insert(self, value: int):
        self.root = self.__r_insert(self.root, value)


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

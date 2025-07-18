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

    def min_value(self, current_node: Node) -> int:
        while current_node.left:
            current_node = current_node.left

        return current_node.value

    def __r_contains(self, current_node: Node, value: int) -> bool:
        if current_node is None:
            return False

        if current_node.value == value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value) -> bool:
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node: Node, value: int) -> Node:
        if current_node is None:
            current_node = Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        return current_node

    def __delete_node(self, current_node: Node, value: int) -> Node:
        if current_node is None:
            return None

        # fine node need to be delete . traversal all nodes
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        if value == current_node.value:
            if current_node.right is None and current_node.left is None:
                return None

            if current_node.right is None and current_node.left:
                return current_node.left

            if current_node.left is None and current_node.right:
                return current_node.right

            if current_node.left and current_node.right:
                min_right_subtree = self.min_value(current_node.right)
                current_node.value = min_right_subtree
                current_node.right = self.__delete_node(
                    current_node.right, min_right_subtree
                )
        return current_node

    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)

    def delete_node(self, value) -> bool:
        self.root = self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST Contains 27:")
print(my_tree.r_contains(27))

print("\nBST Contains 17:")
print(my_tree.r_contains(17))


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

print(my_tree.min_value(my_tree.root))

print(my_tree.min_value(my_tree.root.right))


# test delete node
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value,
      "Root value after attempting to delete 10:")

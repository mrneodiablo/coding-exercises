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

    def contains(self, value) -> bool:
        if self.root is None:
            return False

        parent = self.root
        while parent:
            if value > parent.value:
                parent = parent.right
            elif value < parent.value:
                parent = parent.left
            else:
                return True
        return False

    def delete_node(self, value):
        if self.root is None:
            return False

        # Special case: deleting root node
        if self.root.value == value:
            self.root = self.__delete_helper(self.root)
            return True

        # Find the node to delete and its parent
        parent = None
        current = self.root

        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Node not found
        if current is None:
            return False

        # Delete the node using helper method
        replacement = self.__delete_helper(current)

        # Update parent's pointer
        if parent.left == current:
            parent.left = replacement
        else:
            parent.right = replacement

        return True

    def __min_value_node(self, node):
        # node có giá trị nhỏ nhất luôn nằm bên trái
        while node.left:
            node = node.left
        return node

    def __delete_helper(self, node: Node) -> Node:
        # Case 1: Node has no children (leaf node)
        if node.left is None and node.right is None:
            return None

        # Case 2: Node has only right child
        if node.left is None:
            return node.right

        # Case 3: Node has only left child
        if node.right is None:
            return node.left

        # Case 4: Node has both children
        # Find the minimum value in the right subtree (successor)
        min_node = self.__min_value_node(node.right)

        # Replace current node's value with successor's value
        node.value = min_node.value

        # Delete the successor node iteratively
        self.__delete_min_from_right_subtree(node)

        return node

    def __delete_min_from_right_subtree(self, node):
        """Delete the minimum node from the right subtree iteratively"""
        current = node.right
        parent = node

        # Find the minimum node and its parent
        while current.left is not None:
            parent = current
            current = current.left

        # Delete the minimum node
        if parent == node:
            # The minimum node is the direct right child
            parent.right = current.right
        else:
            # The minimum node is deeper in the left subtree
            parent.left = current.right


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


if __name__ == "__main__":

    print("\n----- Test: Contains on Empty Tree -----\n")
    bst = BinarySearchTree()
    result = bst.contains(5)
    check(False, result, "Check if 5 exists in an empty tree:")

    print("\n----- Test: Contains Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    result = bst.contains(10)
    check(True, result, "Check if 10 exists:")
    result = bst.contains(5)
    check(True, result, "Check if 5 exists:")
    result = bst.contains(15)
    check(True, result, "Check if 15 exists:")

    print("\n----- Test: Contains Not Existing Value -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.contains(15)
    check(False, result, "Check if 15 exists:")

    print("\n----- Test: Contains with Duplicate Inserts -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(10)
    result = bst.contains(10)
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
    result = bst.contains(1)
    check(True, result, "Check if 1 exists:")
    result = bst.contains(8)
    check(True, result, "Check if 8 exists:")
    result = bst.contains(12)
    check(True, result, "Check if 12 exists:")
    result = bst.contains(20)
    check(True, result, "Check if 20 exists:")

    print("\n----- Test: Delete Leaf Node -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    result = bst.delete_node(5)
    check(True, result, "Delete leaf node 5:")
    result = bst.contains(5)
    check(False, result, "Check if 5 still exists after deletion:")
    result = bst.contains(10)
    check(True, result, "Check if 10 still exists:")

    print("\n----- Test: Delete Node with One Child -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(12)
    result = bst.delete_node(15)
    check(True, result, "Delete node 15 with one child:")
    result = bst.contains(15)
    check(False, result, "Check if 15 still exists after deletion:")
    result = bst.contains(12)
    check(True, result, "Check if 12 still exists:")

    print("\n----- Test: Delete Node with Two Children -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)
    result = bst.delete_node(10)
    check(True, result, "Delete root node 10 with two children:")
    result = bst.contains(10)
    check(False, result, "Check if 10 still exists after deletion:")
    result = bst.contains(12)
    check(True, result, "Check if 12 still exists (should be new root):")

    print("\n----- Test: Delete Non-existing Node -----\n")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    result = bst.delete_node(20)
    check(False, result, "Try to delete non-existing node 20:")

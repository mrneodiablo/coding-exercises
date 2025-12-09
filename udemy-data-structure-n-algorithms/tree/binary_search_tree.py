import unittest


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


class TestFunctions(unittest.TestCase):

    def test_contains_empty_tree(self):
        bst = BinarySearchTree()
        result = bst.contains(5)
        self.assertEqual(result, False, "Check if 5 exists in an empty tree")

    def test_contains_existing_value(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        self.assertEqual(bst.contains(10), True, "Check if 10 exists")
        self.assertEqual(bst.contains(5), True, "Check if 5 exists")
        self.assertEqual(bst.contains(15), True, "Check if 15 exists")

    def test_contains_not_existing_value(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        result = bst.contains(15)
        self.assertEqual(result, False, "Check if 15 exists")

    def test_contains_with_duplicate_inserts(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)
        result = bst.contains(10)
        self.assertEqual(result, True, "Check if 10 exists with duplicate inserts")

    def test_contains_with_left_and_right(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(1)
        bst.insert(8)
        bst.insert(12)
        bst.insert(20)

        self.assertEqual(bst.contains(1), True, "Check if 1 exists")
        self.assertEqual(bst.contains(8), True, "Check if 8 exists")
        self.assertEqual(bst.contains(12), True, "Check if 12 exists")
        self.assertEqual(bst.contains(20), True, "Check if 20 exists")

    def test_delete_leaf_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        result = bst.delete_node(5)

        self.assertEqual(result, True, "Delete leaf node 5")
        self.assertEqual(
            bst.contains(5), False, "Check if 5 still exists after deletion"
        )
        self.assertEqual(bst.contains(10), True, "Check if 10 still exists")

    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(12)
        result = bst.delete_node(15)

        self.assertEqual(result, True, "Delete node 15 with one child")
        self.assertEqual(
            bst.contains(15), False, "Check if 15 still exists after deletion"
        )
        self.assertEqual(bst.contains(12), True, "Check if 12 still exists")

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        bst.insert(12)
        bst.insert(18)
        result = bst.delete_node(10)

        self.assertEqual(result, True, "Delete root node 10 with two children")
        self.assertEqual(
            bst.contains(10), False, "Check if 10 still exists after deletion"
        )
        self.assertEqual(
            bst.contains(12), True, "Check if 12 still exists (should be new root)"
        )

    def test_delete_non_existing_node(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        result = bst.delete_node(20)
        self.assertEqual(result, False, "Try to delete non-existing node 20")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)

import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif (
            value > current_node.value
        ):  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, current_node: Node) -> Node:

        if current_node is None:
            return None

        current_node.left = self.__invert_tree(current_node.left)
        current_node.right = self.__invert_tree(current_node.right)

        current_node.left, current_node.right = (current_node.right, current_node.left)

        return current_node

    #   +===================================================+
    #   |              WRITE YOUR CODE HERE                 |
    #   | Description:                                      |
    #   | - Private method to invert a binary tree.         |
    #   | - It swaps every left child with its right child  |
    #   |   recursively.                                    |
    #   |                                                   |
    #   | Parameters:                                       |
    #   | - node: The current node being visited.           |
    #   |                                                   |
    #   | Return:                                           |
    #   | - The node after its subtree has been inverted.   |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - The function works recursively, swapping left   |
    #   |   and right children of all nodes in the tree.    |
    #   | - A temporary variable is used to facilitate the  |
    #   |   swap of the children.                           |
    #   +===================================================+


#  +====================================================+
#  |  Test code below will print output to "User logs"  |
#  +====================================================+


def tree_to_list(node):
    """Helper function to convert tree to
    list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result


class TestFunctions(unittest.TestCase):

    def tree_to_list(self, node):
        """Helper function to convert tree to list level-wise for easy comparison"""
        if not node:
            return []
        queue = [node]
        result = []
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.value)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    def test_empty_tree(self):
        bst = BinarySearchTree()
        bst.invert()
        result = self.tree_to_list(bst.root)
        self.assertEqual(result, [], "Empty tree should remain empty")

    def test_single_node(self):
        bst = BinarySearchTree()
        bst.r_insert(1)
        bst.invert()
        result = self.tree_to_list(bst.root)
        self.assertEqual(result, [1], "Single node should remain unchanged")

    def test_tree_with_left_child(self):
        bst = BinarySearchTree()
        bst.r_insert(2)
        bst.r_insert(1)
        bst.invert()
        result = self.tree_to_list(bst.root)
        self.assertEqual(result, [2, None, 1], "Left child should move to right")

    def test_tree_with_right_child(self):
        bst = BinarySearchTree()
        bst.r_insert(1)
        bst.r_insert(2)
        bst.invert()
        result = self.tree_to_list(bst.root)
        self.assertEqual(result, [1, 2], "Right child should move to left")

    def test_multi_level_tree(self):
        bst = BinarySearchTree()
        for num in [3, 1, 5, 2]:
            bst.r_insert(num)
        bst.invert()
        result = self.tree_to_list(bst.root)
        self.assertEqual(
            result, [3, 5, 1, None, None, 2], "Multi-level tree should be inverted"
        )


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)


"""
    EXPECTED OUTPUT:
    ----------------
    All inversion tests should pass
 """

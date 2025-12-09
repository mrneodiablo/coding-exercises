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

        current_node.left, current_node.right = (
            current_node.right, current_node.left
            )

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


def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        # Perform inversion (or second inversion for the specific case)
        bst.invert()
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")


test_invert_binary_search_tree()

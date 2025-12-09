import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # The 'is_balanced' and 'inorder_traversal' methods will
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):

        if left < 0 or right < 0 or right < left or len(nums) <= 0:
            return None

        middle = (left + right) // 2
        current_node = Node(nums[middle])

        current_node.left = self.__sorted_list_to_bst(
            nums, left=left, right=(middle - 1)
        )
        current_node.right = self.__sorted_list_to_bst(
            nums, left=middle + 1, right=right
        )

        return current_node

        #   +====================================================+
        #   |               WRITE YOUR CODE HERE                 |
        #   | Description:                                       |
        #   | - Private method to convert a sorted list to a     |
        #   |   binary search tree (BST).                        |
        #   | - The method uses the middle element of the list   |
        #   |   as the root to ensure balanced height.           |
        #   |                                                    |
        #   | Parameters:                                        |
        #   | - nums: Sorted list of integers.                   |
        #   | - left: Starting index of the list segment.        |
        #   | - right: Ending index of the list segment.         |
        #   |                                                    |
        #   | Return:                                            |
        #   | - The root node of the BST created from the        |
        #   |   specified list segment.                          |
        #   |                                                    |
        #   | Tips:                                              |
        #   | - The function is recursively called to construct  |
        #   |   the left and right subtrees.                     |
        #   | - A new Node is created at each recursive call     |
        #   |   with the mid element of the current list segment |
        #   |   as its value, ensuring the BST property is       |
        #   |   maintained.                                      |
        #   +====================================================+


class TestFunctions(unittest.TestCase):

    def test_empty_list(self):
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([])
        self.assertEqual(bst.is_balanced(), True, "Empty tree should be balanced")
        self.assertEqual(bst.inorder_traversal(), [], "Empty tree traversal should be empty")

    def test_single_element(self):
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([10])
        self.assertEqual(bst.is_balanced(), True, "Single element tree should be balanced")
        self.assertEqual(bst.inorder_traversal(), [10], "Single element traversal")

    def test_odd_number_elements(self):
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([1, 2, 3, 4, 5])
        self.assertEqual(bst.is_balanced(), True, "Tree should be balanced")
        self.assertEqual(bst.inorder_traversal(), [1, 2, 3, 4, 5], "Inorder traversal should match")

    def test_even_number_elements(self):
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
        self.assertEqual(bst.is_balanced(), True, "Tree should be balanced")
        self.assertEqual(bst.inorder_traversal(), [1, 2, 3, 4, 5, 6], "Inorder traversal should match")

    def test_large_sorted_list(self):
        bst = BinarySearchTree()
        large_sorted_list = list(range(1, 16))
        bst.sorted_list_to_bst(large_sorted_list)
        self.assertEqual(bst.is_balanced(), True, "Large tree should be balanced")
        self.assertEqual(bst.inorder_traversal(), large_sorted_list, "Inorder traversal should match")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctions)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)


"""
    EXPECTED OUTPUT:
    ----------------
    All tests should pass with balanced BST created from sorted lists
 """

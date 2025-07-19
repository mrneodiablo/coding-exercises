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


#  +====================================================+
#  |  Test code below will print output to "User logs"  |
#  +====================================================+


def check_balanced_and_correct_traversal(bst_parameter, expected_traversal):
    is_balanced = bst_parameter.is_balanced()
    inorder = bst_parameter.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print(
            "FAIL: Tree is balanced or inorder traversal is incorrect.\n"
            )


# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = BinarySearchTree()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)

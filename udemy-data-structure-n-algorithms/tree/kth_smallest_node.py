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

    def kth_smallest(self, kth) -> int:
        # # solution 1
        # # create a stack to hold nodes
        # stack = []
        # # start at the root of the tree
        # temp = self.root
        # while stack or temp:
        #     # get to left node
        #     while temp:
        #         stack.append(temp)
        #         temp = temp.left

        #     # pop the last node added to the stack
        #     temp = stack.pop()
        #     kth -= 1

        #     # return data
        #     if kth == 0:
        #         return temp.value

        #     # move to the right child of the node
        #     temp = temp.right
        # # if k is greater than the number of nodes in the tree, return None
        # return None

        # solution 2
        values = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            values.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)

        if self.root is None:
            return None

        traversal(self.root)

        if kth <= 0 or kth > len(values):
            return None

        return values[kth - 1]


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


if __name__ == "__main__":
    print("\n----- Test: Basic Kth Smallest -----\n")
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # Tree structure:
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   2  4 6  8
    # In-order: [2, 3, 4, 5, 6, 7, 8]

    result = bst.kth_smallest(1)
    check(2, result, "1st smallest (should be 2):")

    result = bst.kth_smallest(3)
    check(4, result, "3rd smallest (should be 4):")

    result = bst.kth_smallest(5)
    check(6, result, "5th smallest (should be 6):")

    result = bst.kth_smallest(7)
    check(8, result, "7th smallest (should be 8):")

    print("\n----- Test: Edge Cases - Invalid K -----\n")

    result = bst.kth_smallest(0)
    check(None, result, "k = 0 (invalid, should return None):")

    result = bst.kth_smallest(-1)
    check(None, result, "k = -1 (invalid, should return None):")

    result = bst.kth_smallest(8)
    check(None, result, "k = 8 (out of bounds, tree has 7 nodes):")

    result = bst.kth_smallest(10)
    check(None, result, "k = 10 (way out of bounds):")

    print("\n----- Test: Empty Tree -----\n")
    empty_bst = BinarySearchTree()
    result = empty_bst.kth_smallest(1)
    check(None, result, "1st smallest in empty tree:")

    print("\n----- Test: Single Node Tree -----\n")
    single_bst = BinarySearchTree()
    single_bst.insert(42)

    result = single_bst.kth_smallest(1)
    check(42, result, "1st smallest in single node tree:")

    result = single_bst.kth_smallest(2)
    check(None, result, "2nd smallest in single node tree (should be None):")

    print("\n----- Test: Two Node Tree -----\n")
    two_bst = BinarySearchTree()
    two_bst.insert(10)
    two_bst.insert(5)

    result = two_bst.kth_smallest(1)
    check(5, result, "1st smallest in two node tree:")

    result = two_bst.kth_smallest(2)
    check(10, result, "2nd smallest in two node tree:")

    result = two_bst.kth_smallest(3)
    check(None, result, "3rd smallest in two node tree (should be None):")

    print("\n----- Test: Skewed Tree (Only Right Children) -----\n")
    right_skewed_bst = BinarySearchTree()
    right_skewed_bst.insert(1)
    right_skewed_bst.insert(2)
    right_skewed_bst.insert(3)
    right_skewed_bst.insert(4)
    right_skewed_bst.insert(5)

    # Tree: 1 -> 2 -> 3 -> 4 -> 5 (all right children)
    # In-order: [1, 2, 3, 4, 5]

    result = right_skewed_bst.kth_smallest(1)
    check(1, result, "1st smallest in right-skewed tree:")

    result = right_skewed_bst.kth_smallest(3)
    check(3, result, "3rd smallest in right-skewed tree:")

    result = right_skewed_bst.kth_smallest(5)
    check(5, result, "5th smallest in right-skewed tree:")

    print("\n----- Test: Skewed Tree (Only Left Children) -----\n")
    left_skewed_bst = BinarySearchTree()
    left_skewed_bst.insert(5)
    left_skewed_bst.insert(4)
    left_skewed_bst.insert(3)
    left_skewed_bst.insert(2)
    left_skewed_bst.insert(1)

    # Tree: 5 <- 4 <- 3 <- 2 <- 1 (all left children)
    # In-order: [1, 2, 3, 4, 5]

    result = left_skewed_bst.kth_smallest(1)
    check(1, result, "1st smallest in left-skewed tree:")

    result = left_skewed_bst.kth_smallest(4)
    check(4, result, "4th smallest in left-skewed tree:")

    result = left_skewed_bst.kth_smallest(5)
    check(5, result, "5th smallest in left-skewed tree:")

    print("\n----- Test: Duplicate Values (Should Not Insert) -----\n")
    dup_bst = BinarySearchTree()
    dup_bst.insert(5)
    dup_bst.insert(3)
    dup_bst.insert(7)
    dup_bst.insert(5)  # Duplicate, should not be inserted
    dup_bst.insert(3)  # Duplicate, should not be inserted

    # Tree should still be: [3, 5, 7]
    result = dup_bst.kth_smallest(1)
    check(3, result, "1st smallest with duplicates (should be 3):")

    result = dup_bst.kth_smallest(3)
    check(7, result, "3rd smallest with duplicates (should be 7):")

    result = dup_bst.kth_smallest(4)
    check(
        None,
        result,
        "4th smallest with duplicates (should be None, only 3 unique values):",
    )

    print("\n----- Test: Large Numbers -----\n")
    large_bst = BinarySearchTree()
    large_bst.insert(1000)
    large_bst.insert(500)
    large_bst.insert(1500)
    large_bst.insert(250)
    large_bst.insert(750)
    large_bst.insert(1250)
    large_bst.insert(1750)

    # In-order: [250, 500, 750, 1000, 1250, 1500, 1750]
    result = large_bst.kth_smallest(1)
    check(250, result, "1st smallest with large numbers:")

    result = large_bst.kth_smallest(4)
    check(1000, result, "4th smallest with large numbers (root):")

    result = large_bst.kth_smallest(7)
    check(1750, result, "7th smallest with large numbers:")

    print("\n----- Original Test Cases -----\n")
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("1st smallest:", bst.kth_smallest(1))  # Expected output: 2
    print("3rd smallest:", bst.kth_smallest(3))  # Expected output: 4
    print("6th smallest:", bst.kth_smallest(6))  # Expected output: 7
    print("10th smallest:", bst.kth_smallest(10))  # Expected output: None

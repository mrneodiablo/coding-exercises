"""
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored in
a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

Clarification: The input/output format is the same as
how LeetCode serializes a binary tree.
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
"""

import json


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper_serialize(root):
            data = {"left": "#", "right": "#", "val": None}

            if not root:
                return

            data["left"] = helper_serialize(root.left)
            data["right"] = helper_serialize(root.right)
            data["val"] = root.val

            return data

        return json.dumps(helper_serialize(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def deserialize_helper(serialized_data):

            if not serialized_data:
                return None

            node = TreeNode(serialized_data["val"])
            node.left = deserialize_helper(serialized_data["left"])
            node.right = deserialize_helper(serialized_data["right"])

            return node

        return deserialize_helper(json.loads(data))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Helper function to check if two trees are equal
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# Test cases
if __name__ == "__main__":
    codec = Codec()

    # Test case 1: Balanced tree [1,2,3,null,null,4,5]
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)

    serialized1 = codec.serialize(root1)
    print(f"Test 1 - Serialized: {serialized1}")

    # Verify it's a JSON string
    assert isinstance(serialized1, str), "Should return a string"
    assert "1" in serialized1, "Should contain root value"

    # Verify round-trip deserialization
    deserialized1 = codec.deserialize(serialized1)
    assert is_same_tree(root1, deserialized1), "Round-trip failed"
    assert deserialized1.val == 1, "Root should be 1"
    assert deserialized1.left.val == 2, "Left should be 2"
    assert deserialized1.right.right.val == 5, "Right-right should be 5"
    print("✓ Test case 1 passed: Balanced tree")

    # Test case 2: Empty tree
    root2 = None
    serialized2 = codec.serialize(root2)
    print(f"\nTest 2 - Serialized empty: {serialized2}")

    assert serialized2 == "null", "Empty tree should serialize to 'null'"

    deserialized2 = codec.deserialize(serialized2)
    assert deserialized2 is None, "Empty tree should deserialize to None"
    print("✓ Test case 2 passed: Empty tree")

    # Test case 3: Left-skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    # /
    # 4
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)

    serialized3 = codec.serialize(root3)
    print(f"\nTest 3 - Serialized skewed: {serialized3}")

    # Verify round-trip
    deserialized3 = codec.deserialize(serialized3)
    assert is_same_tree(root3, deserialized3), "Round-trip failed"
    assert deserialized3.val == 1, "Root should be 1"
    assert deserialized3.right is None, "Right should be None"
    assert deserialized3.left.left.left.val == 4, "Deep left should be 4"
    print("✓ Test case 3 passed: Skewed tree")

    print("\n🎉 All test cases passed!")

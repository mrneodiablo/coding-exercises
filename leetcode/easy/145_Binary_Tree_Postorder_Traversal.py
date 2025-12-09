# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorder_dfs(root, [])

    def postorder_dfs(self, root, arr):
        if root is None:
            return

        self.postorder_dfs(root.left, arr)
        self.postorder_dfs(root.right, arr)
        arr.append(root.val)
        return arr

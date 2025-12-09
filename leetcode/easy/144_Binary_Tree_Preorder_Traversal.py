class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.preorder_dfs(root, [])

    def preorder_dfs(self, root, arr):
        if root is None:
            return

        arr.append(root.val)
        self.preorder_dfs(root.left, arr)
        self.preorder_dfs(root.right, arr)
        return arr

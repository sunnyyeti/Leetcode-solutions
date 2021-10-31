# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()
        def dfs(node):
            if node is None:
                return 
            if node.right in seen:
                return 
            seen.add(node)
            node.right = dfs(node.right)
            node.left = dfs(node.left)
            return node
        return dfs(root)
        
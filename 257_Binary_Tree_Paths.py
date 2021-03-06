# Given a binary tree, return all root-to-leaf paths.

# Note: A leaf is a node with no children.

# Example:

# Input:

#    1
#  /   \
# 2     3
#  \
#   5

# Output: ["1->2->5", "1->3"]

# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        self.ans = []
        path = []
        self.helper(root,path)
        return self.ans
        
    def helper(self,node,path):
        #print(node.val,path)
        path.append(str(node.val))
        if not node.left and not node.right:
            self.ans.append("->".join(path))
        if node.left:
            self.helper(node.left,path)
        if node.right:
            self.helper(node.right,path)
        path.pop()
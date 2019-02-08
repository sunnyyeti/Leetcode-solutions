# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        inorder_traversal = []
        self.inorder(root,inorder_traversal)
        #print([x.val for x in inorder_traversal])
        for i in range(len(inorder_traversal)-2,-1,-1):
            inorder_traversal[i].val+=inorder_traversal[i+1].val
        return root
        
    def inorder(self,root,inorder_traversal):
        if not root:
            return
        self.inorder(root.left,inorder_traversal)
        inorder_traversal.append(root)
        self.inorder(root.right, inorder_traversal)
        
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

 

# Note: 

# 1 <= preorder.length <= 100
# The values of preorder are distinct.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        ans = self.helper(preorder, 0, len(preorder) - 1)
        return ans

    def helper(self, preorder, begin, end):
        if end < begin:
            return None
        if end == begin:
            return TreeNode(preorder[begin])
        tmproot = TreeNode(preorder[begin])
        break_flag = False
        for i in range(begin + 1, end + 1):
            if preorder[i] > tmproot.val:
                break_flag=True
                break
        if break_flag:
            tmproot.left = self.helper(preorder, begin + 1, i - 1)
            tmproot.right = self.helper(preorder, i, end)
        else:
            tmproot.left = self.helper(preorder,begin+1,end)
        return tmproot
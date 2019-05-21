# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

     # 3
    # / \
   # 4   5
  # / \
 # 1   2
# Given tree t:
   # 4 
  # / \
 # 1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

     # 3
    # / \
   # 4   5
  # / \
 # 1   2
    # /
   # 0
# Given tree t:
   # 4
  # / \
 # 1   2
# Return false.
# Accepted
# 86,980
# Submissions
# 210,887
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        stack = [s]
        while stack:
            node = stack.pop()
            if node.val==t.val:
                if self.isSameTree(node,t):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    def isSameTree(self,t1,t2):
        if not t1 and not t2:
            return True
        elif not t1:
            return False
        elif not t2:
            return False
        if t1.val!=t2.val:
            return False
        return self.isSameTree(t1.left,t2.left) and self.isSameTree(t1.right,t2.right)
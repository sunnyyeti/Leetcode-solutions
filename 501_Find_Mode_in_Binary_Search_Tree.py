# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# For example:
# Given BST [1,null,2,2],

   # 1
    # \
     # 2
    # /
   # 2
 

# return [2].

# Note: If a tree has more than one mode, you can return them in any order.

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        self.last = None
        self.max_cnt = 0
        self.cur_cnt = 0
        self.ans = []
        self.helper(root)
        if self.cur_cnt>self.max_cnt:
            self.ans = [self.last]
        elif self.cur_cnt==self.max_cnt:
            self.ans.append(self.last)
        return self.ans
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if node.val == self.last:
            self.cur_cnt += 1
        else:
            if self.cur_cnt > self.max_cnt:
                self.max_cnt = self.cur_cnt
                self.ans = [self.last]
            elif self.cur_cnt == self.max_cnt:
                self.ans.append(self.last)
            self.last = node.val
            self.cur_cnt = 1
        self.helper(node.right)
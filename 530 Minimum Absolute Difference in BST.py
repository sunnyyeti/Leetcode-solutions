# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

# Example:

# Input:

#    1
#     \
#      3
#     /
#    2

# Output:
# 1

# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        last = float("inf")
        min_abs_dif = float("inf")
        def inorder_traverse(node):
            nonlocal min_abs_dif,last
            if node is None:
                return 
            inorder_traverse(node.left)
            min_abs_dif=min(min_abs_dif,abs(node.val-last))
            last = node.val
            inorder_traverse(node.right)
        inorder_traverse(root)
        return min_abs_dif
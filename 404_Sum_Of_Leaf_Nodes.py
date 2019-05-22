# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        if root is None:
            return self.sum
        self.traverse(root, False)
        return self.sum

    def traverse(self, root, left):
        if not root.left and not root.right and left:
            self.sum += root.val
            return
        if root.left:
            self.traverse(root.left, True)
        if root.right:
            self.traverse(root.right, False)

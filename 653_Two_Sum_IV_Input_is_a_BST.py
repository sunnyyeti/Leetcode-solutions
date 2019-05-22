# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        self.inorder_traverse(root, res)
        i, j = 0, len(res) - 1
        while i < j:
            tmp_sum = res[i] + res[j]
            if tmp_sum == k:
                return True
            elif tmp_sum < k:
                i += 1
            else:
                j -= 1
        return False

    def inorder_traverse(self, root, res):
        if root is None:
            return
        self.inorder_traverse(root.left, res)
        res.append(root.val)
        self.inorder_traverse(root.right, res)
# Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

 

# Example 1:


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Example 2:


# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
 

# Constraints:

# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum_ = 0
        def help(root):
            nonlocal sum_
            if root is None:
                return
            if low<=root.val<=high:
                sum_ += root.val
                help(root.left)
                help(root.right)
            elif root.val<low:
                help(root.right)
            else:
                help(root.left)
        help(root)
        return sum_
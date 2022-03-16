# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = True
        def help(node):
            """
            return the mininum and maximum value of this subtree
            """
            nonlocal ans
            if not node.left and not node.right:
                return node.val, node.val
            elif not node.left:
                rmin,rmax = help(node.right)
                if rmin<=node.val:
                    ans = False
                return min(node.val,rmin),max(rmax,node.val)
            elif not node.right:
                lmin,lmax = help(node.left)
                if lmax >= node.val:
                    ans = False
                return min(node.val,lmin),max(node.val,lmax)
            else:
                lmin,lmax = help(node.left)
                rmin,rmax = help(node.right)
                if not lmax<node.val<rmin:
                    ans = False
                return min(lmin,rmin,node.val),max(lmax,rmax,node.val)
        help(root)
        return ans
                
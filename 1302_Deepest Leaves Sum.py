# Given a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:



# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _deepestLeavesSum(self, root: TreeNode) -> int:
        stats = {}
        def help(root,d):
            if root is None:
                return
            if not root.left and not root.right:
                stats.setdefault(d,[]).append(root.val)
            help(root.left,d+1)
            help(root.right,d+1)
        help(root,0)
        return sum(stats[max(stats.keys())])
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def help(root,d):
            if root is None:
                return 0,d
            if not root.left and not root.right:
                return root.val,d
            ls,ld = help(root.left,d+1)
            rs,rd = help(root.right,d+1)
            if ld>rd:
                return ls,ld
            if ld<rd:
                return rs,rd
            return ls+rs,ld
        return help(root,0)[0]
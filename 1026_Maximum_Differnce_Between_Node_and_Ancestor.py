# Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

# (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

# Example 1:



# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: 
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

# Note:

# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float("-inf")
        self.helper(root)
        return self.max
        
    def helper(self,node):
        """
        return the maximum and minimun node value of all descendants of parameter `node`
        """
        if node is None:
            return float("-inf"),float("inf") ## max and min
        left_max, left_min = self.helper(node.left)
        right_max,right_min = self.helper(node.right)
        descent_max = max(left_max,right_max)
        descent_min = min(left_min,right_min)
        if descent_max != float("-inf"):
            self.max = max(abs(node.val-descent_max),self.max)
        if descent_min != float("inf"):
            self.max = max(abs(node.val-descent_min),self.max)
        return max(descent_max,node.val),min(descent_min,node.val)
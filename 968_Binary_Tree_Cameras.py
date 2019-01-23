# Given a binary tree, we install cameras on the nodes of the tree. 

# Each camera at a node can monitor its parent, itself, and its immediate children.

# Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

# Example 1:


# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# Example 2:


# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

# Note:

# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cnt = 0
        cover, put = self.helper(root)
        return self.cnt+(not cover)
        
    def helper(self,root):
        if root is None:
            return True, False
        left_cover, left_put = self.helper(root.left)
        right_cover, right_put = self.helper(root.right)
        if (not left_cover) or (not right_cover):
            self.cnt+=1
            return True,True
        if (not left_put and not right_put):
            return False,False
        return True, False

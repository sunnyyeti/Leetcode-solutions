# Given a binary tree, determine if it is a complete binary tree.

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

# Example 1:



# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:



# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
 
# Note:

# The tree will have between 1 and 100 nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        level = [root]
        next_stopped = False
        while level:
            next_level = []
            cur_stopped = next_stopped
            next_stopped = False
            for node in level:
                if next_stopped or cur_stopped:
                    if node.left or node.right:
                        return False
                else:
                    if not node.left and node.right:
                        return False
                    elif node.left:
                        next_level.append(node.left)
                        if node.right:
                            next_level.append(node.right)
                        else:
                            next_stopped=True
                    else:
                        next_stopped = True
            level = next_level
        return True
                
            
                        
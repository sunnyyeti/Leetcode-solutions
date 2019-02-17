# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

 

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:



# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Note:

# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if root.val == x or root.val ==y :
            return False
        self.x_level = None
        self.x_p = None
        self.y_level = None
        self.y_p = None
        self.x = x
        self.y = y
        self.helper(root,0,None)
        return self.x_level==self.y_level and self.x_p!=self.y_p        
    def helper(self,root,level,parent):
        if not root:
            return 
        if root.val==self.x:
            self.x_level = level
            self.x_p = parent
        if root.val == self.y:
            self.y_level = level
            self.y_p = parent
        self.helper(root.left,level+1,root.val)
        self.helper(root.right,level+1,root.val)
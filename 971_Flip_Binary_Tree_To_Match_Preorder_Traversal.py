# Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

# A node in this binary tree can be flipped by swapping the left child and the right child of that node.

# Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

# (Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

# Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

# If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

# If we cannot do so, then return the list [-1].

 

# Example 1:



# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Example 2:



# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# Example 3:



# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
 

# Note:

# 1 <= N <= 100
# Accepted
# 3,742
# Submissions
# 8,900

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if not voyage and not root:
            return []
        if root and not voyage:
            return [-1]
        if voyage and not root:
            return [-1]
        if voyage[0] != root.val:
            return [-1]
        self.voyage = voyage
        #self.ind = 0
        self.res = []
        success = self.helper(root,0)
        if success[0]:
            return self.res
        return [-1]
    def helper(self,node,ind):
        if ind==len(self.voyage)-1:
            return not node.left and not node.right,ind+1
        next_val = self.voyage[ind+1]
        if node.left:
            if node.left.val==next_val:
                pass
            elif (node.right and node.right.val==next_val):
                node.left,node.right = node.right, node.left
                self.res.append(node.val)
            else:
                return False,ind+1
            ind+=1
            success_left,next_ind = self.helper(node.left,ind)
            if success_left:
                ind = next_ind
                if ind>=len(self.voyage):
                      return node.right is None,ind
                else:
                    next_right_val = self.voyage[ind]
                    if not node.right :
                        return True,ind
                    if node.right.val!=next_right_val:
                        return False,ind
                    else:
                        return self.helper(node.right,ind)
            else:
                return False,next_ind

        else:
            if not node.right:
                return True,ind+1
            if node.right.val!=next_val:
                return False,ind+1
            ind+=1
            success_right = self.helper(node.right,ind)
            return success_right
            
                
                            
            
                
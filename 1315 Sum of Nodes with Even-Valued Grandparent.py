# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

 

# Example 1:



# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

# Constraints:

# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def acc(node):
            nonlocal sum_
            if node.left:
                if node.left.left:
                    sum_ += node.left.left.val
                if node.left.right:
                    sum_+=node.left.right.val
            if node.right:
                if node.right.left:
                    sum_ += node.right.left.val
                if node.right.right:
                    sum_ += node.right.right.val
        sum_ = 0
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.val&1==0:
                acc(cur_node)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return sum_
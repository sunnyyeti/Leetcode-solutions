# We run a preorder depth-first search (DFS) on the root of a binary tree.

# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

# If a node has only one child, that child is guaranteed to be the left child.

# Given the output traversal of this traversal, recover the tree and return its root.

 

# Example 1:


# Input: traversal = "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# Example 2:


# Input: traversal = "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# Example 3:


# Input: traversal = "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
 

# Constraints:

# The number of nodes in the original tree is in the range [1, 1000].
# 1 <= Node.val <= 109
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        level = {}
        first_dash = traversal.find('-')
        if first_dash == -1:
            return TreeNode(int(traversal))
        root = TreeNode(int(traversal[:first_dash]))
        level[0] = root
        dashs = 0
        num = 0
        i = first_dash
        flag = False
        while i<len(traversal):
            if traversal[i] == '-':
                if not flag:
                    dashs += 1
                else:
                    flag = False
                    parent = level[dashs-1]
                    if parent.left is None:
                        parent.left = TreeNode(num)
                        level[dashs] = parent.left
                    else:
                        parent.right = TreeNode(num)
                        level[dashs] = parent.right
                    dashs = 1
                    num = 0
            else:
                num = num*10+int(traversal[i])
                flag = True
            i+=1
        parent = level[dashs-1]
        if parent.left is None:
            parent.left = TreeNode(num)
        else:
            parent.right = TreeNode(num)   
        return level[0]
            
                
        
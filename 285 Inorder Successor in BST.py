# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

# The successor of a node p is the node with the smallest key greater than p.val.

 

# Example 1:


# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
# All Nodes will have unique values.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        prev = None
        ans = None
        def intr(node):
            nonlocal ans,prev
            if node is None:
                return
            intr(node.left)
            if prev is p:
                if ans:
                    return
                ans = node
                return
            else:
                prev = node
            intr(node.right)
        intr(root)
        return ans
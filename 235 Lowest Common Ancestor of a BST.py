# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

# Note:

# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowest(node):
            if node is None:
                return None,None,None
            la,lp,lq= lowest(node.left)
            ra,rp,rq = lowest(node.right)
            if not la and not ra :
                if (lp or lq) and (rp or rq):
                    return node, lp or lq, rp or rq
                if (lp or lq) or (rp or rq):
                    if node.val== p.val or node.val == q.val:
                        return node,node,rp or rq or lp or lq
                    else:
                        return None,None,rp or rq or lp or lq
                if node.val== p.val or node.val == q.val:
                        return None,None,node
                else:
                        return None,None,None
                    
            if la:
                return la,lp,lq
            if ra:
                return ra,rp,rq
        ans =  lowest(root)
        #print(ans)
        return ans[0]
            
            
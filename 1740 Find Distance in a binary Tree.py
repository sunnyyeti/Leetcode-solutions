# Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

# The distance between two nodes is the number of edges on the path from one to the other.

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
# Output: 3
# Explanation: There are 3 edges between 5 and 0: 5-3-1-0.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
# Output: 2
# Explanation: There are 2 edges between 5 and 7: 5-2-7.
# Example 3:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
# Output: 0
# Explanation: The distance between a node and itself is 0.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# All Node.val are unique.
# p and q are values in the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p==q:
            return 0
        min_dis = None
        def distance(node):
            if node is None:
                return None
            nonlocal min_dis
            right = distance(node.right)
            left = distance(node.left)
            if right is not None and left is not None:
                min_dis = right+left+2
            elif right is not None:
                if node.val in [p,q]:
                    min_dis = right+1
                    return 0
                else:
                    return right+1
            elif left is not None:
                if node.val in [p,q]:
                    min_dis = left+1
                    return 0
                else:
                    return left + 1
            else:
                if node.val in [p,q]:
                    return 0
                else:
                    return None
        distance(root)
        return min_dis
            
                
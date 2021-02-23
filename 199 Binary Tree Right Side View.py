# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        d = deque([(root,0)])
        ans = []
        while d:
            curnode,curlevel = d.popleft()
            if not d or curlevel < d[0][1]:
                ans.append(curnode.val)
            if curnode.left:
                d.append((curnode.left,curlevel+1))
            if curnode.right:
                d.append((curnode.right,curlevel+1))
        return ans
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        level = [root]
        max_length = 0
        while level:
            next_level = []
            i = 0
            while i<len(level) and level[i] is None:
                i+=1
            if i==len(level):
                break
            j = len(level)-1
            while level[j] is None:
                j-=1
            level_length = j-i+1
            max_length = max(max_length,level_length)
            for ind in range(i,j+1):
                node = level[ind]
                if node is None:
                    next_level.extend([None,None])
                else:
                    if node.left:
                        next_level.append(node.left)
                    else:
                        next_level.append(None)
                    if node.right:
                        next_level.append(node.right)
                    else:
                        next_level.append(None)
            level = next_level
        return max_length
        
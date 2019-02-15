# Given a binary tree, find the leftmost value in the last row of the tree.

# Example 1:
# Input:

    # 2
   # / \
  # 1   3

# Output:
# 1
# Example 2: 
# Input:

        # 1
       # / \
      # 2   3
     # /   / \
    # 4   5   6
       # /
      # 7

# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        queue = deque()
        queue.append((root,0))
        level = -1
        while queue:
            node,l= queue.popleft()
            if l>level:
                level = l
                ans = node.val
            if node.left:
                queue.append((node.left,l+1))
            if node.right:
                queue.append((node.right,l+1))
        return ans
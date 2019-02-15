# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

          # 1
         # / \
        # 3   2
       # / \   \  
      # 5   3   9 

# Output: [1, 3, 9]
from collections import deque
class Solution:
    def largestValues(self, root: 'TreeNode') -> 'List[int]':
        ans = []
        if not root:
            return ans
        deque_ = deque()
        deque_.append((root,0))
        level = -1
        max_v = float("-inf")
        while deque_:
            node,l= deque_.popleft()
            if l!=level:
                level = l
                if max_v!=float("-inf"):
                    ans.append(max_v)
                    max_v = float("-inf")
            max_v = max(max_v,node.val)
            if node.left:
                deque_.append((node.left,l+1))
            if node.right:
                deque_.append((node.right,l+1))
        ans.append(max_v)
        return ans
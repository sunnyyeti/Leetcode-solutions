# Given a binary tree, return the vertical order traversal of its nodes values.

# For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

# Example 1:



# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
# Example 2:



# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

# Note:

# The tree will have between 1 and 1000 nodes.
# Each node's value will be between 0 and 1000.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = {}
        q = deque([(0,0,root)])
        tmp = {}
        lasty = -1
        min_x = float("inf")
        max_x = float("-inf")
        while q:
            x,y,node = q.popleft()
            min_x = min(min_x,x)
            max_x = max(max_x,x)
            if y!=lasty:
                lasty = y
                for k,v in tmp.items():
                    if k not in res:
                        res[k] = []
                    res[k] += sorted(v)
                tmp = {}
                tmp.setdefault(x,[]).append(node.val)
            else:
                tmp.setdefault(x,[]).append(node.val)
            if node.left:
                q.append((x-1,y-1,node.left))
            if node.right:
                q.append((x+1,y-1,node.right))
        for k,v in tmp.items():
            res[k] = res.get(k,[])+sorted(v)
        ans = []
        for x in range(int(min_x),int(max_x)+1):
            if x in res:
                ans.append(res[x])
        return ans
            
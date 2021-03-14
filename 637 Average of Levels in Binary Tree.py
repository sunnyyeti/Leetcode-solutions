# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return ans
        d = deque([(root,0)])
        sum_ = 0
        last_level = 0
        cnt = 0
        ans = []
        while d:
            cur_node,cur_level = d.popleft()
            if cur_level == last_level:
                sum_ += cur_node.val
                cnt +=1
            else:
                ans.append(sum_/cnt)
                sum_ = cur_node.val
                cnt = 1
                last_level = cur_level
            if cur_node.left:
                d.append((cur_node.left,cur_level+1))
            if cur_node.right:
                d.append((cur_node.right,cur_level+1))
        ans.append(sum_/cnt)
        return ans
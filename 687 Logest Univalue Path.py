# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [5,4,5,1,1,5]
# Output: 2
# Example 2:


# Input: root = [1,4,5,4,4,5]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def helper(node):
            nonlocal ans
            if node is None:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            length = 1
            return_value = 1
            if node.left and node.val == node.left.val:
                length += left
                return_value = max(return_value,left+1)
            if node.right and node.val == node.right.val:
                length += right
                return_value = max(return_value,right+1)
            ans = max(ans,length)
            #print(node.val,left,right,ans,return_value)
            #print(left,right)
            return return_value
        helper(root)
        return ans-1
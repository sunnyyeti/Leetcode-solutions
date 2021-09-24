# Given the root of a binary tree, return the length of the longest consecutive path in the tree.

# This path can be either increasing or decreasing.

# For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
# On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# Example 2:


# Input: root = [2,1,3]
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -3 * 104 <= Node.val <= 3 * 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node.left and not node.right:
                ans = max(ans,1)
                return  1,1
            elif node.left and not node.right:
                left_i,left_d = helper(node.left)
                if node.val -1 == node.left.val:
                    cur_i = 1
                    cur_d = left_d+1
                elif node.val+1 == node.left.val:
                    cur_i = left_i+1
                    cur_d = 1
                else:
                    cur_i,cur_d = 1,1
                ans = max(ans,cur_i,cur_d)
                return cur_i,cur_d
            elif node.right and not node.left:
                right_i,right_d = helper(node.right)
                if node.val -1 == node.right.val:
                    cur_i = 1
                    cur_d = right_d+1
                elif node.val+1 == node.right.val:
                    cur_i = right_i+1
                    cur_d = 1
                else:
                    cur_i,cur_d = 1,1
                ans = max(ans,cur_i,cur_d)
                return cur_i,cur_d   
            else:
                left_i,left_d = helper(node.left)
                right_i,right_d = helper(node.right)
                if node.left.val+1 == node.val==node.right.val-1:
                    ans = max(ans,left_d+right_i+1)
                elif node.left.val-1==node.val==node.right.val+1:
                    ans = max(ans,left_i+right_d+1)
                if node.val -1 == node.left.val:
                    cur_i = 1
                    cur_d = left_d+1
                elif node.val+1 == node.left.val:
                    cur_i = left_i+1
                    cur_d = 1
                else:
                    cur_i,cur_d = 1,1
                ans = max(ans,cur_i,cur_d)
                if node.val -1 == node.right.val:
                    cur_ir = 1
                    cur_dr = right_d+1
                elif node.val+1 == node.right.val:
                    cur_ir = right_i+1
                    cur_dr = 1
                else:
                    cur_ir,cur_dr = 1,1
                ans = max(ans,cur_ir,cur_dr)
                return max(cur_i,cur_ir),max(cur_d,cur_dr)
        helper(root)
        return ans
                    
                
            
            
            
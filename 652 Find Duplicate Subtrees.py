# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

 

# Example 1:


# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
# Example 2:


# Input: root = [2,1,1]
# Output: [[1]]
# Example 3:


# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
 

# Constraints:

# The number of the nodes in the tree will be in the range [1, 10^4]
# -200 <= Node.val <= 200
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = {}
        def get_signature(node:TreeNode):
            if node is None:
                return ''
            left_sig = get_signature(node.left)
            right_sig = get_signature(node.right)
            cur_sig = f"{node.val}({left_sig})({right_sig})"
            #print(left_sig,right_sig,cur_sig)
            ans.setdefault(cur_sig,[]).append(node)
            return cur_sig
        get_signature(root)
        #print(ans)
        return [v.pop()  for k,v in ans.items() if len(v)>1]
            
        
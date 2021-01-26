# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight without alerting the police.

# Example 1:

# Input: [3,2,3,null,3,null,1]

#      3
#     / \
#    2   3
#     \   \ 
#      3   1

# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:

# Input: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.cache = {}
        return max(self.help(root,False),self.help(root,True))
    
    def help(self,root,robbed) -> int :
        if (root,robbed) in self.cache:
            return self.cache[(root,robbed)]
        if robbed:
            ans = root.val
            if root.left:
                ans += self.help(root.left,False)
            if root.right:
                ans += self.help(root.right,False)
            self.cache[(root,robbed)] = ans
            return ans 
        else:
            ans = 0
            if root.left:
                ans += max(self.help(root.left,True),self.help(root.left,False))
            if root.right:
                ans += max(self.help(root.right,True),self.help(root.right,False))
            self.cache[(root,robbed)] = ans
            return ans
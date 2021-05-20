# You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:


# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def help(root):
            if root is None:
                return
            help(root.left)
            ans.append(root)
            help(root.right)
        help(root)
        ans.append(TreeNode(float("inf")))
        #print(list(map(lambda x:x.val,ans)))
        ind = None
        for i in range(len(ans)):
            if  ind is None and ans[i].val>ans[i+1].val :
                ind = i
            #print(ind)
            if ind is not None:
                if ans[ind].val < ans[i].val:
                    
                    ans[ind].val,ans[i-1].val = ans[i-1].val,ans[ind].val
                    break
        
# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:

# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# Example 3:

# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# Example 4:

# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# Example 5:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 

# Constraints:

# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root,ans):
            if root is None:
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        res1 = []
        inorder(root1,res1)
        res2 = []
        inorder(root2,res2)
        i=j=0
        res = []
        while i<len(res1) and j<len(res2):
            if res1[i]<res2[j]:
                res.append(res1[i])
                i+=1
            else:
                res.append(res2[j])
                j+=1
        while i<len(res1):
            res.append(res1[i])
            i+=1
        while j<len(res2):
            res.append(res2[j])
            j+=1
        return res
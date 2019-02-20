# We are given a binary tree (with root node root), a target node, and an integer value K.

# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

# Output: [7,4,1]

# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.



# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
 

# Note:

# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# Accepted
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.ans = []
        self.target = target
        self.K = K
        self.pre_order(root)
        return self.ans
    def pre_order(self,root):
        if not root:
            return None
        if root is self.target:
            if self.K==0:
                self.ans.append(root.val)
                return 0
            else:
                self.find(root.left,self.K-1)
                self.find(root.right,self.K-1)
                return 0
        else:
            distance = self.pre_order(root.left)
            if distance is not None:
                distance+=1
                remain = self.K-distance
                if remain==0:
                    self.ans.append(root.val)
                elif remain>0:
                    self.find(root.right,remain-1)
                return distance
            distance = self.pre_order(root.right)
            if distance is not None:
                distance+=1
                remain = self.K-distance
                if remain==0:
                    self.ans.append(root.val)
                elif remain>0:
                    self.find(root.left,remain-1)
                return distance

    def find(self,root,distance):
        if not root:
            return
        if root and distance==0:
            self.ans.append(root.val)
        self.find(root.left,distance-1)
        self.find(root.right,distance-1)

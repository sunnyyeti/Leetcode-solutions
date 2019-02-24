# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:

      # 6
    # /   \
   # 3     5
    # \    / 
     # 2  0   
       # \
        # 1
# Note:
# The size of the given array will be in the range [1,1000].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class SegTreeNode:
    def __init__(self,max_val=None,max_ind=None,start=None,end=None,left=None,right=None):
        self.max_val=max_val
        self.max_ind = max_ind
        self.start = start
        self.end = end
        self.left = left
        self.right = right
    def query(self,start,end):
        if start<=self.start and end>=self.end:
            return self.max_val,self.max_ind
        if end<self.start or start>self.end:
            return float("-inf"),-1
        else:
            lv,lind = self.left.query(start,end)
            rv,rind = self.right.query(start,end)
            if lv>rv:
                return lv,lind
            else:
                return rv,rind

class MaxRangeSegTree:
    def __init__(self,arr):
        self.tree = self.construct_tree(arr,0,len(arr)-1)

    def query(self,start,end):
        return self.tree.query(start,end)

    def construct_tree(self,arr,begin,end):
        if begin==end:
            return SegTreeNode(arr[begin],begin,begin,end)
        mid = (begin+end)//2
        left_tree = self.construct_tree(arr,begin,mid)
        right_tree = self.construct_tree(arr,mid+1,end)
        curnode = SegTreeNode()
        curnode.left = left_tree
        curnode.right = right_tree
        curnode.start = begin
        curnode.end = end
        if left_tree.max_val>right_tree.max_val:
            curnode.max_val = left_tree.max_val
            curnode.max_ind = left_tree.max_ind
        else:
            curnode.max_ind = right_tree.max_ind
            curnode.max_val = right_tree.max_val
        return curnode


class Solution:
    def constructMaximumBinaryTree(self, nums):
        self.max_seg_tree = MaxRangeSegTree(nums)
        return self.helper(nums,0,len(nums)-1)
        
    
    def helper(self,nums,begin,end):
        if begin>end:
            return None
        max_v,max_ind = self.max_seg_tree.query(begin,end)
        curnode = TreeNode(max_v)
        curnode.left = self.helper(nums,begin,max_ind-1)
        curnode.right = self.helper(nums,max_ind+1,end)
        return curnode
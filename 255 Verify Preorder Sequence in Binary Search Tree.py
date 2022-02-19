# Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

 

# Example 1:


# Input: preorder = [5,2,1,3,6]
# Output: true
# Example 2:

# Input: preorder = [5,2,6,1,3]
# Output: false
 

# Constraints:

# 1 <= preorder.length <= 104
# 1 <= preorder[i] <= 104
# All the elements of preorder are unique.
 

# Follow up: Could you do it using only constant space complexity?
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def find_bst(index,l,u):
            if index >= len(preorder):
                return index

            if l<preorder[index]<u:
                end = find_bst(index+1,l,preorder[index])
                end = find_bst(end+1,preorder[index],u)
                return end
            else:
                return index-1
        return find_bst(0,float("-inf"),float('inf'))>=len(preorder)
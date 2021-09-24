# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
# Example 3:

# Input: root = [2,3,9,10,7,8,6,5,4,11,1]
# Output: 1025
# Example 4:

# Input: root = [1,1]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        treesums = {}
        max_product = float("-inf")
        def calculate_sum(node:TreeNode):
            if not node:
                return 0
            left_sum = calculate_sum(node.left)
            right_sum = calculate_sum(node.right)
            cur_sum = left_sum + right_sum + node.val
            treesums[node] = cur_sum
            return cur_sum
        def find_max_products(node:TreeNode):
            nonlocal max_product
            if node.left:
                tree1 = treesums[node.left]
                tree2 = total_sum-tree1
                max_product = max(max_product,tree1*tree2)
                find_max_products(node.left)
            if node.right:
                tree1 = treesums[node.right]
                tree2 = total_sum - tree1
                max_product = max(max_product,tree1*tree2)
                find_max_products(node.right)
                
        calculate_sum(root)
        total_sum = treesums[root]
        find_max_products(root)
        return max_product%(10**9+7)
        
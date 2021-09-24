# Given the root of a binary tree, return true if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree.

 

# Example 1:


# Input: root = [5,10,10,null,null,2,3]
# Output: true
# Example 2:


# Input: root = [1,2,10,null,null,2,20]
# Output: false
# Explanation: You cannot split the tree into two trees with equal sums after removing exactly one edge on the tree.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        #total_sum = 0
        def total_sum_helper(node: TreeNode) -> int:
            if node is None:
                return 0
            return total_sum_helper(node.left) + total_sum_helper(node.right) + node.val
        total_sum = total_sum_helper(root)

        def is_equal_partition(node: TreeNode) -> Tuple[int, bool]:
            if node is None:
                return 0, False
            left_sum, left_partitions = is_equal_partition(node.left)
            right_sum, right_partitions = is_equal_partition(node.right)
            return left_sum+right_sum+node.val, (left_partitions or right_partitions or (node.left and left_sum*2 == total_sum) or (node.right and right_sum*2 == total_sum))
        return is_equal_partition(root)[1]

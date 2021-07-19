# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(node1, node2):
            if node1 == node2 == None:
                return True
            elif (node1 and not node2) or (node2 and not node1):
                return False
            else:
                return node1.val == node2.val and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
        return is_mirror(root.left, root.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        level = [root]
        while level:
            i, j = 0, len(level)-1
            while i <= j:
                if level[i] == level[j] == None or (level[i] and level[j] and level[i].val == level[j].val):
                    i += 1
                    j -= 1
                else:
                    return False
            next_level = []
            for node in level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            level = next_level
        return True

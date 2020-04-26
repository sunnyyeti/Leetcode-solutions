# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

# Constraints:

# Both of the given trees will have between 1 and 200 nodes.
# Both of the given trees will have values between 0 and 200
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaf(root):
            if root is None:
                return []
            stack = [root]
            ans = []
            while stack:
                cur_node = stack.pop()
                if cur_node.left is None and cur_node.right is None:
                    ans.append(cur_node.val)
                if cur_node.right is not None:
                    stack.append(cur_node.right)
                if cur_node.left is not None:
                    stack.append(cur_node.left)
            return ans
        leaf1 =  leaf(root1)
        leaf2 = leaf(root2)
        return leaf1==leaf2
# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
# Example 2:

# Input: root = [1]
# Output: [[1]]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        out_degree = {}
        parents = {}
        out0 = []
        def helper(node, parent):
            parents[node] = parent
            if node.left:
                out_degree[node] = out_degree.get(node, 0)+1
                helper(node.left, node)
            if node.right:
                out_degree[node] = out_degree.get(node, 0)+1
                helper(node.right, node)
            if out_degree.get(node, 0) == 0:
                out0.append(node)
        helper(root, None)
        ans = []
        while out0:
            tmp = [n.val for n in out0]
            new_out0 = []
            ans.append(tmp)
            for n in out0:
                p = parents[n]
                if p:
                    out_degree[p] -= 1
                    if out_degree[p] == 0:
                        new_out0.append(p)
            out0 = new_out0
        return ans

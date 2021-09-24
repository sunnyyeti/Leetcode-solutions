# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

# The left boundary is the set of nodes defined by the following:

# The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
# If a node in the left boundary and has a left child, then the left child is in the left boundary.
# If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
# The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

# The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

# Given the root of a binary tree, return the values of its boundary.

 

# Example 1:


# Input: root = [1,null,2,3,4]
# Output: [1,3,4,2]
# Explanation:
# - The left boundary is empty because the root does not have a left child.
# - The right boundary follows the path starting from the root's right child 2 -> 4.
#   4 is a leaf, so the right boundary is [2].
# - The leaves from left to right are [3,4].
# Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
# Example 2:


# Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
# Output: [1,2,4,7,8,9,10,6,3]
# Explanation:
# - The left boundary follows the path starting from the root's left child 2 -> 4.
#   4 is a leaf, so the left boundary is [2].
# - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
#   10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
# - The leaves from left to right are [4,7,8,9,10].
# Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -1000 <= Node.val <= 1000
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def get_left_boundary(root):
            left_boundary = []
            node = root.left
            while node:
                left_boundary.append(node)
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
                else:
                    left_boundary.pop()
                    node = None
            return left_boundary

        def get_right_boundary(root):
            right_boundary = []
            node = root.right
            while node:
                right_boundary.append(node)
                if node.right:
                    node = node.right
                elif node.left:
                    node = node.left
                else:
                    right_boundary.pop()
                    node = None
            return right_boundary

        def get_leaves(root):
            stack = [root]
            leaves = []
            while stack:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if not node.left and not node.right and node is not root:
                    leaves.append(node)
            return leaves
        boundary = [
            root]+get_left_boundary(root)+get_leaves(root)+get_right_boundary(root)[::-1]
        return list(map(lambda x: x.val, boundary))

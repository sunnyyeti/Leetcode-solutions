# A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions.

# We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

# For example, below are two quad trees A and B:

# A:
# +-------+-------+   T: true
# |       |       |   F: false
# |   T   |   T   |
# |       |       |
# +-------+-------+
# |       |       |
# |   F   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight: T
# bottomLeft: F
# bottomRight: F

# B:               
# +-------+---+---+
# |       | F | F |
# |   T   +---+---+
# |       | T | T |
# +-------+---+---+
# |       |       |
# |   T   |   F   |
# |       |       |
# +-------+-------+
# topLeft: T
# topRight:
     # topLeft: F
     # topRight: F
     # bottomLeft: T
     # bottomRight: T
# bottomLeft: T
# bottomRight: F
 

# Your task is to implement a function that will take two quadtrees and return a quadtree that represents the logical OR (or union) of the two trees.

# A:                 B:                 C (A or B):
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       | F | F |  |       |       |
# |   T   |   T   |  |   T   +---+---+  |   T   |   T   |
# |       |       |  |       | T | T |  |       |       |
# +-------+-------+  +-------+---+---+  +-------+-------+
# |       |       |  |       |       |  |       |       |
# |   F   |   F   |  |   T   |   F   |  |   T   |   F   |
# |       |       |  |       |       |  |       |       |
# +-------+-------+  +-------+-------+  +-------+-------+
# Note:

# Both A and B represent grids of size N * N.
# N is guaranteed to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.
# The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        tree = self.merge_trees(quadTree1,quadTree2)
        self.shrink_tree(tree)
        return tree
        
    def merge_trees(self,t1,t2):
        if t1.isLeaf and t2.isLeaf:
            t1.val = t1.val or t2.val
            return t1
        elif t1.isLeaf:
            return self.merge_trees_and_values(t2,t1.val)
        elif t2.isLeaf:
            return self.merge_trees_and_values(t1,t2.val)
        else:
            t1.topLeft = self.merge_trees(t1.topLeft,t2.topLeft)
            t1.topRight = self.merge_trees(t1.topRight,t2.topRight)
            t1.bottomLeft =self.merge_trees(t1.bottomLeft,t2.bottomLeft)
            t1.bottomRight = self.merge_trees(t1.bottomRight,t2.bottomRight)
            return t1
            
    def merge_trees_and_values(self,tree,value):
        if tree.isLeaf:
            tree.val = tree.val or value
            return tree
        tree.topLeft = self.merge_trees_and_values(tree.topLeft,value)
        tree.topRight = self.merge_trees_and_values(tree.topRight,value)
        tree.bottomLeft = self.merge_trees_and_values(tree.bottomLeft,value)
        tree.bottomRight = self.merge_trees_and_values(tree.bottomRight,value)
        return tree
    
    def shrink_tree(self,t):
        if t.isLeaf:
            return 
        self.shrink_tree(t.topLeft)
        self.shrink_tree(t.topRight)
        self.shrink_tree(t.bottomLeft)
        self.shrink_tree(t.bottomRight)
        if t.topLeft.isLeaf and t.topRight.isLeaf and t.bottomLeft.isLeaf and t.bottomRight.isLeaf and (t.topLeft.val==t.topRight.val==t.bottomLeft.val==t.bottomRight.val):
            t.isLeaf = True
            t.val = t.topLeft.val
            t.topLeft = t.topRight=t.bottomLeft=t.bottomRight=None
            
            
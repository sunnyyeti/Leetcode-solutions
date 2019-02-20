# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

# Each node of each tree in the answer must have node.val = 0.

# You may return the final list of trees in any order.

 

# Example 1:

# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:

 

# Note:

# 1 <= N <= 20


class Solution:
    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        if N % 2 == 0:
            return []
        return self.helper(N)
 

    def helper(self,n):
        root = TreeNode(0)
        remain = n-1
        if remain==0:
            return [root]
        ans = []
        for left in range(1,remain,2):
            left_subtrees = self.helper(left)
            right_subtrees = self.helper(remain-left)
            for left in left_subtrees:
                for right in right_subtrees:
                    root.left = left
                    root.right = right
                    ans.append(self.get_copy(root))
        return ans
            

    def get_copy(self,root):
        tmproot = TreeNode(0)
        def helper(node1,node2):
            if node2.left:
                tmpleft = TreeNode(0)
                node1.left = tmpleft
                helper(tmpleft,node2.left)
            if node2.right:
                tmpright = TreeNode(0)
                node1.right = tmpright
                helper(tmpright,node2.right)
        helper(tmproot,root)
        return tmproot

        
        
class Solution:
    def allPossibleFBT(self, N: 'int') -> 'List[TreeNode]':
        if N % 2 == 0:
            return []
        self.cache = {}
        return self.helper(N)


    def helper(self,n):
        if n in self.cache:
            return self.cache[n]
        remain = n-1
        if remain==0:
            self.cache[n] = [TreeNode(0)]
            return self.cache[n]
        ans = []
        for left in range(1,remain,2):
            left_subtrees = self.helper(left)
            right_subtrees = self.helper(remain-left)
            for left in left_subtrees:
                for right in right_subtrees:
                    tmp = TreeNode(0)
                    tmp.left = left
                    tmp.right = right
                    ans.append(tmp)
        self.cache[n] = ans
        return ans



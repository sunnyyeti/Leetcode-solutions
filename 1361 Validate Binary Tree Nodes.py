# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

 

# Example 1:



# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# Example 2:



# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# Example 3:



# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
# Example 4:



# Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# Output: false
 

# Constraints:

# 1 <= n <= 10^4
# leftChild.length == rightChild.length == n
# -1 <= leftChild[i], rightChild[i] <= n - 1
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        #all_nodes = set(range(n))
        parents = [-1]*n
        for i,(l,r) in enumerate(zip(leftChild,rightChild)):
            if l!=-1 and parents[l]==-1:
                parents[l] = i
            elif l!=-1:
                return False
            if r!=-1 and parents[r]==-1:
                parents[r] = i
            elif r!=-1:
                return False
        #print(parents)
        roots = set()
        for i in range(n):
            visited = set([i])
            node = i
            while parents[node]!=-1:
                node = parents[node]
                if node in visited:
                    return False
                visited.add(node)
            roots.add(node)
        return len(roots)==1
            
            
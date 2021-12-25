# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

 

# Example 1:



# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation: 
# A longest path of the tree is the path 1 - 0 - 2.
# Example 2:



# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation: 
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

# Constraints:

# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# The given edges form an undirected tree.
import heapq
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        graph = {}
        for a,b in edges:
            graph.setdefault(a,[]).append(b)
            graph.setdefault(b,[]).append(a)
        max_length = 0
        def helper(node,parent):
            nonlocal max_length
            all_children = []
            for child in graph.get(node,[]):
                if child != parent:
                    heapq.heappush(all_children,helper(child,node))
                    if len(all_children) > 2:
                        heapq.heappop(all_children)
            if not all_children:
                return 0
            if len(all_children) == 1:
                max_length = max(max_length,all_children[0]+1)
                return all_children[0] + 1
            else:
                max_length = max(max_length,all_children[0]+all_children[1]+2)
                return all_children[1]+1
        helper(0,-1)
        return max_length
            
                    
            
                    
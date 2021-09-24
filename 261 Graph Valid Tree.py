# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
 

# Constraints:

# 1 <= 2000 <= n
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for n1,n2 in edges:
            graph.setdefault(n1,[]).append(n2)
            graph.setdefault(n2,[]).append(n1)
        #print(graph)
        state = [0]*n
        #0 white not visited
        #1 gray in visiting
        #2 black visited
        visited_edges = set()
        def dfs(node):
            if state[node] == 1:
                return False
            state[node] = 1
            #print("Neighbors of ", node)
            #print(graph.get(n,[]))
            for neighbor in graph.get(node,[]):
                if node > neighbor:
                    edge = (neighbor,node)
                else:
                    edge = (node,neighbor)
                if edge not in visited_edges:
                    #print(edge)
                    visited_edges.add(edge)
                    res = dfs(neighbor)
                    if not res:
                        return False
            #print(f"set {node} to 2")
            state[node] = 2
            return True
        res = dfs(0)
        #print(res)
        if not res:
            return False
        #print(state)
        return all(s==2  for s in state)
                    
                    
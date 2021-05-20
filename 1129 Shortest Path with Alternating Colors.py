# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

# Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

# Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

# Example 1:

# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
# Example 3:

# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
# Example 4:

# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
# Example 5:

# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
 

# Constraints:

# 1 <= n <= 100
# red_edges.length <= 400
# blue_edges.length <= 400
# red_edges[i].length == blue_edges[i].length == 2
# 0 <= red_edges[i][j], blue_edges[i][j] < n
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        total = n
        red_graph = {}
        for i,j in red_edges:
            if i+j>0:
                red_graph.setdefault(i,[]).append(j)
        blue_graph = {}
        for i,j in blue_edges:
            if i+j>0:
                blue_graph.setdefault(i,[]).append(j)
        q = deque()
        visited = set()
        ans = [-1]*total
        ans[0] = 0
        for n in red_graph.get(0,[]):
            q.append(('r',n,1))
            visited.add(('r',n))
        for n in blue_graph.get(0,[]):
            q.append(('b',n,1))
            visited.add(('b',n))
        updated = 1
        while q:
            cur_node = q.popleft()
            if ans[cur_node[1]] == -1:
                ans[cur_node[1]] = cur_node[2]
                updated +=1
                if updated==total:
                    break
            if cur_node[0]=='r':
                for n in blue_graph.get(cur_node[1],[]):
                    if ('b',n) not in visited:
                        visited.add(('b',n))
                        q.append(('b',n,cur_node[2]+1))
            if cur_node[0] == 'b':
                for n in red_graph.get(cur_node[1],[]):
                    if ('r',n) not in visited:
                        visited.add(('r',n))
                        q.append(('r',n,cur_node[2]+1))
        return ans 
            
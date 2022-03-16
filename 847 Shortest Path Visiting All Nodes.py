# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

# Example 1:


# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:


# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
 

# Constraints:

# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.
from functools import cache
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodes_cnt = len(graph)
        queue = deque()
        seen = set()
        for n in range(nodes_cnt):
            queue.append((n,0|(1<<n),0))
            seen.add((n,0|(1<<n)))
        while queue:
            node,mask,steps = queue.popleft()
            if mask == (1<<nodes_cnt) -1:
                return steps
            for nn in graph[node]:
                next_node = nn
                next_mask = mask|(1<<nn)
                if (next_node,next_mask) not in seen:
                    seen.add((next_node,next_mask))
                    queue.append((next_node,next_mask,steps+1))
       
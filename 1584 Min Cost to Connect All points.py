# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:



# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# Example 3:

# Input: points = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4
# Example 4:

# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000
# Example 5:

# Input: points = [[0,0]]
# Output: 0
 

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        visited = {0}
        n = len(points)
        dis_mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                dis_mat[i][j] = dis_mat[j][i] = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        node_pools =[(dis_mat[0][j],j) for j in range(1,n)]
        heapq.heapify(node_pools)
        cost = 0
        while len(visited)<len(points):
            c,p = heapq.heappop(node_pools)
            if p not in visited:
                visited.add(p)
                cost += c
                for i in range(n):
                    if i!=p and i not in visited:
                        heapq.heappush(node_pools,(dis_mat[p][i],i))
        return cost
                
    
                
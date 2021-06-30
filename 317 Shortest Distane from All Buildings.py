# You are given an m x n grid grid of values 0, 1, or 2, where:

# each 0 marks an empty land that you can pass by freely,
# each 1 marks a building that you cannot pass through, and
# each 2 marks an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

# Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

# Example 1:


# Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
# So return 7.
# Example 2:

# Input: grid = [[1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1]]
# Output: -1
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is either 0, 1, or 2.
# There will be at least one building in the grid.
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(r,c):
            queue = deque([(r,c,0)])
            visited = set([(r,c)])
            while queue:
                r,c,d = queue.popleft()
                dis[r][c] += d
                rea[r][c] += 1
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+dr,c+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0 and (nr,nc) not in visited:
                        queue.append((nr,nc,d+1))
                        visited.add((nr,nc))
        dis = [[0]*(len(grid[0])) for _ in grid]
        rea = [[0]*(len(grid[0])) for _ in grid]
        buildings = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    buildings += 1
                    bfs(i,j)
        #print(dis,rea)
        ans = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rea[i][j] == buildings and grid[i][j]==0:
                    ans = min(ans,dis[i][j])
        return ans if ans!=float('inf') else -1
        
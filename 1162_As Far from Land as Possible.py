# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

# If no land or water exists in the grid, return -1.

 

# Example 1:



# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:



# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
 

# Note:

# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        de = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    de.append((r,c,0))
                    visited.add((r,c))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        d = 0
        while de:
            r,c,d = de.popleft()
            for dr,dc in dirs:
                nr = r+dr
                nc = c+dc
                nd = d+1
                if (nr,nc) not in visited and 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
                    de.append((nr,nc,nd))
                    visited.add((nr,nc))
        return d if d else -1
                    
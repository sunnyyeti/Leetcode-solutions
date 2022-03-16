# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:

# Input: 
# grid = 
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

# Example 2:

# Input: 
# grid = 
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.
 

# Constraints:

# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([((0,0,k),0)])
        seen = {(0,0,k)}
        while queue:
            cs,steps = queue.popleft()
            if cs[:2] == (len(grid)-1,len(grid[0])-1):
                return steps
            r,c,k = cs
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    if grid[nr][nc] == 0:
                        if (nr,nc,k) not in seen:
                            seen.add((nr,nc,k))
                            queue.append(((nr,nc,k),steps+1))
                    else:
                        if k>=1:
                            if (nr,nc,k-1) not in seen:
                                seen.add((nr,nc,k-1))
                                queue.append(((nr,nc,k-1),steps+1))
        return -1
        
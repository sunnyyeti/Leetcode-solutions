# In a given 2D binary array grid, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
 

# Constraints:

# 2 <= grid.length == grid[0].length <= 100
# grid[i][j] == 0 or grid[i][j] == 1
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(r, c, seen):
            seen.add((r, c))
            grid[r][c] = 2
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                    dfs(nr, nc, seen)
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c, seen)
                    break
            else:
                continue
            break
        #print(grid)
        queue = deque()
        for r, c in seen:
            queue.append((r, c, 0))
        while queue:
            r, c, dis = queue.popleft()
            if grid[r][c] == 1:
                return dis-1
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 2:
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                    queue.append((nr, nc, dis+1))

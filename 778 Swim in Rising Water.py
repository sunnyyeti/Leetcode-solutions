# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

 

# Example 1:


# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# Example 2:


# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n2
# Each value grid[i][j] is unique.
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        t = -1
        queue = deque([(0,0)])
        while True:
            t+=1
            seen = set()
            new_queue = deque()
            while queue:
                cr,cc = queue.popleft()
                if (cr,cc) == (rows-1,cols-1):
                    return t
                if (cr,cc) not in seen:
                    seen.add((cr,cc))
                    new_queue.append((cr,cc))
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nr,nc = cr+dr,cc+dc
                        if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in seen and grid[nr][nc]<=t and grid[cr][cc]<=t:
                            queue.append((nr,nc))
            queue = new_queue
                        
            
            
        
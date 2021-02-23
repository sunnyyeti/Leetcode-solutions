# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def get_candidates(r,c,tr,tc,grid,visited):
            deltas = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
            for dr,dc in deltas:
                nr = r+dr
                nc = c+dc
                if 0<=nr<tr and 0<=nc<tc and grid[nr][nc]==0 and not (nr,nc) in visited:
                    yield nr,nc
        if len(grid)==0 or len(grid[0])==0 or grid[0][0]!=0:
            return -1
        d = deque([((0,0),1)])
        visited = set((0,0))
        tr,tc = len(grid),len(grid[0])
        while d:
            pos,dis = d.popleft()
            #print("cur:",pos)
            if pos==(tr-1,tc-1):
                return dis
            for nr,nc in get_candidates(pos[0],pos[1],tr,tc,grid,visited):
                #print("next:",nr,nc,dis+1)
                visited.add((nr,nc))
                d.append(((nr,nc),dis+1))
        return -1
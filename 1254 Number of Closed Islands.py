# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:



# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
# Example 2:



# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
# Example 3:

# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
 

# Constraints:

# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def traverse(r,c):
            closed=  True
            stack = [(r,c)]
            while stack:
                cr,cc = stack.pop()
                grid[cr][cc]=1
                if cr==0 or cr==rows-1 or cc==0 or cc==cols-1:
                    closed=False
                for dr,dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nr,nc = cr+dr,cc+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==0:
                        stack.append((nr,nc))
            return closed
        
        
        
        rows,cols = len(grid),len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    cnt+=traverse(i,j)
        return cnt
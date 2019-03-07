# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        row = len(grid)
        if row==0:
            return 0
        col = len(grid[0])
        if col==0:
            return 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    per = 0
                    for dr,dc in dirs:
                        nr = r+dr
                        nc = c+dc
                        if 0<=nr<row and 0<=nc<col:
                            if grid[nr][nc]==0:
                                per+=1
                        else:
                            per+=1
                    ans+=per
        return ans
        
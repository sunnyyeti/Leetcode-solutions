# On a 2-dimensional grid, there are 4 types of squares:

# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

# Example 1:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:

# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:

# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
 

# Note:

# 1 <= grid.length * grid[0].length <= 20


class Solution:
    def uniquePathsIII(self, grid):
        """
        Backtrack with DFS searching
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows = len(grid)
        if self.rows==0:
            return 0
        self.cols = len(grid[0])
        if self.cols==0:
            return 0
        self.empty_squares = 1 #regard start position as empty cell as well
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c]==1:
                    self.start = (r,c)
                if grid[r][c]==0:
                    self.empty_squares+=1
        self.cnt = 0
        self.grid = grid
        self.dfs(*self.start)
        return self.cnt

    def dfs(self,r,c):
        if self.grid[r][c]==2:
            if self.empty_squares==0:
                self.cnt+=1
            return
        self.grid[r][c]=3
        self.empty_squares-=1
        if (r+1)<self.rows and self.grid[r+1][c] in [0,2]:
            self.dfs(r+1,c)
        if (r-1)>-1 and self.grid[r-1][c] in [0,2]:
            self.dfs(r-1,c)
        if (c+1)<self.cols and self.grid[r][c+1] in [0,2]:
            self.dfs(r,c+1)
        if (c-1)>-1 and self.grid[r][c-1] in [0,2]:
            self.dfs(r,c-1)
        self.grid[r][c]=0
        self.empty_squares+=1
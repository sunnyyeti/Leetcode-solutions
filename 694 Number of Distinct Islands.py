# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

# Return the number of distinct islands.

 

# Example 1:


# Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# Output: 1
# Example 2:


# Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:        
        def dfs(r,c,islands):
            islands.append((r,c))
            grid[r][c] = 0
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]:
                    dfs(nr,nc,islands)
        def get_signature(islands):
            islands.sort()
            origin = islands[0]
            signature = []
            for cell in islands:
                signature.append((cell[0]-origin[0],cell[1]-origin[1]))
            return tuple(signature)
        all_islands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    cur_island = []
                    dfs(r,c,cur_island)
                    all_islands.add(get_signature(cur_island))
        return len(all_islands)
                    
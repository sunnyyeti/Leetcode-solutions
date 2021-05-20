# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def get(r,c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]):
                return grid[r][c]
            return float('inf')
        for r in range(len(grid)-1,-1,-1):
            for c in range(len(grid[0])-1,-1,-1):
                if not (r==len(grid)-1 and c==len(grid[0])-1):
                    grid[r][c]+=min(get(r,c+1),get(r+1,c))
        return grid[0][0]
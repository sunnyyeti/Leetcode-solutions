# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
import copy
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = copy.deepcopy(mat)
        rows,cols = len(mat),len(mat[0])
        def get(r,c):
            if 0<=r<rows and 0<=c<cols:
                return dp[r][c]
            return float('inf')
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    dp[r][c] = min(get(r-1,c)+1,get(r,c-1)+1)

        for r in reversed(range(rows)):
            for c in range(cols):
                if mat[r][c] != 0:
                    dp[r][c] = min(dp[r][c],get(r,c-1)+1,get(r+1,c)+1)

                 
        for r in range(rows):
            for c in reversed(range(cols)):
                if mat[r][c] != 0:
                    dp[r][c] = min(dp[r][c],get(r,c+1)+1,get(r-1,c)+1)
                    
        
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if mat[r][c] != 0:
                    dp[r][c] = min(dp[r][c],get(r,c+1)+1,get(r+1,c)+1)
                  
        return dp
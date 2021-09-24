# Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

# The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

# Example 1:


# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
# Example 2:


# Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
# Output: 4
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows,cols = len(mat),len(mat[0])
        prev_row_dp = [[0]*4  for _ in range(cols)] # h,v,d,ad
        ans = 0
        for r in range(rows):
            cur_row_dp = [[0]*4  for _ in range(cols)]
            for c in range(cols):
                ele = mat[r][c]
                if ele==1:
                    dp_cell = cur_row_dp[c]
                    dp_cell[0] = cur_row_dp[c-1][0]+1 if c else 1
                    dp_cell[1] = prev_row_dp[c][1]+1
                    dp_cell[2] = prev_row_dp[c-1][2]+1 if c else 1
                    dp_cell[3] = prev_row_dp[c+1][3]+1 if c+1<cols else 1
                    ans  = max(ans,max(dp_cell))
            prev_row_dp = cur_row_dp
        return ans
                    
                    
        
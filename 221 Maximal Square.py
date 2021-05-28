# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[None]*len(matrix[0]) for _ in matrix]
        ans = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]=='1':
                    if c==0 or matrix[r][c-1]=='0':
                        rdp = 1
                    else:
                        rdp = dp[r][c-1][0]+1
                    if r==0 or matrix[r-1][c]=='0':
                        cdp = 1
                    else:
                        cdp = dp[r-1][c][1]+1
                    dp[r][c] = [rdp,cdp]
                else:
                    #print(r,c)
                    #print(dp)
                    dp[r][c] = [0,0]
        square_dp = [[0]*len(matrix[0]) for _ in matrix]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '0':
                    square_dp[r][c] = 0
                else:
                    if r==0 or c==0:
                        square_dp[r][c] = 1
                        ans = max(ans,1)
                    else:
                        rdp,cdp = dp[r][c]
                        min_dp = min(rdp,cdp,square_dp[r-1][c-1]+1)
                        square_dp[r][c] = min_dp
                        ans = max(ans,min_dp)
        return ans**2
                    
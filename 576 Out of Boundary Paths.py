# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

 

# Example 1:

# Input: m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:

# Example 2:

# Input: m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:

 

# Note:

# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
class Solution:
    def findPaths(self, m: int, n: int, N: int, ii: int, jj: int) -> int:
        def neighbours(r,c):
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                yield r+dr,c+dc
        if N==0:
            return 0
        dp = [ [0]*N for _ in range(m*n)]
        for i in range(m*n):
            r = i//n
            c = i%n
            for nr,nc in neighbours(r,c):
                if nr<0 or nr>=m or nc<0 or nc>=n:
                    dp[i][0] +=1
        for d in range(1,N):
            for i in range(m*n):
                r = i//n
                c = i%n
                for nr,nc in neighbours(r,c):
                    if 0<=nr<m and 0<=nc<n:
                        dp[i][d] += dp[nr*n+nc][d-1]
                dp[i][d] %= (10**9+7) 
        d = ii*n+jj
        #print(d)
        return sum(dp[d])%(10**9+7)
            
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and space is marked as 1 and 0 respectively in the grid.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
# Accepted
# 385,742
# Submissions
# 1,074,535
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def get(r,c):
            if 0<=r<len(obstacleGrid) and 0<=c<len(obstacleGrid[0]):
                return obstacleGrid[r][c]
            return 0
        for r in range(len(obstacleGrid)-1,-1,-1):
            for c in range(len(obstacleGrid[0])-1,-1,-1):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                elif r==len(obstacleGrid)-1 and c==len(obstacleGrid[0])-1:
                    obstacleGrid[r][c] = 1
                else:
                    obstacleGrid[r][c] = get(r,c+1)+get(r+1,c)
        return obstacleGrid[0][0]
            
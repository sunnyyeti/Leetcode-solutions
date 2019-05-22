# Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
#
# A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
#
# Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.
#
#
#
# Example 1:
#
# Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation:
# There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
# Example 2:
#
# Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation:
# All 1s are either on the boundary or can reach the boundary.
#
#
# Note:
#
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# All rows have the same size.

from collections import deque
class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.A = A
        self.rows = len(A)
        self.cols = len(A[0])
        for r in range(self.rows):
            if self.A[r][0]==1:
                self.erode(r,0)
            if self.A[r][self.cols-1]==1:
                self.erode(r,self.cols-1)
        for c in range(self.cols):
            if self.A[0][c]==1:
                self.erode(0,c)
            if self.A[self.rows-1][c]==1:
                self.erode(self.rows-1,c)
        ans = 0
        for r in range(self.rows):
            for c in range(self.cols):
                ans+= self.A[r][c]==1
        return ans


    def erode(self,r,c):
        self.A[r][c] = 0
        d = deque()
        d.append((r,c))
        while d:
            r,c = d.popleft()
            if c+1<self.cols and self.A[r][c+1]==1:
                self.A[r][c+1]=0
                d.append((r,c+1))
            if c-1>-1 and self.A[r][c-1]==1:
                self.A[r][c-1]=0
                d.append((r,c-1))
            if r+1<self.rows and self.A[r+1][c]==1:
                self.A[r+1][c]=0
                d.append((r+1,c))
            if r-1>-1 and self.A[r-1][c]==1:
                self.A[r-1][c]=0
                d.append((r-1,c))

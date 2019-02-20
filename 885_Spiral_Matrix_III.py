# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

# Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

# Now, we walk in a clockwise spiral shape to visit every position in this grid. 

# Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 

# Eventually, we reach all R * C spaces of the grid.

# Return a list of coordinates representing the positions of the grid in the order they were visited.

 

# Example 1:

# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]


 

# Example 2:

# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


 

# Note:

# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
class Solution:
    def spiralMatrixIII(self, R: 'int', C: 'int', r0: 'int', c0: 'int') -> 'List[List[int]]':
        self.ans = [[r0,c0]]
        self.R = R
        self.C = C
        self.cur_length = 1
        self.total = R*C
        r = r0
        c = c0
        while True:
            r,c = self.up_right(r,c)
            r,c = self.bottom_left(r,c)
            if len(self.ans)==self.total:
                break

        return self.ans
    def up_right(self,r,c):
        for i in range(1,self.cur_length+1):
            c+=1
            if 0<=r<self.R and 0<=c<self.C:
                self.ans.append([r,c])
        for i in range(1,self.cur_length+1):
            r+=1
            if 0<=r<self.R and 0<=c<self.C:
                self.ans.append([r,c])
        self.cur_length+=1
        return r,c

    def bottom_left(self,r,c):
        for i in range(1,self.cur_length+1):
            c-=1
            if 0<=r<self.R and 0<=c<self.C:
                self.ans.append([r,c])
        for i in range(1,self.cur_length+1):
            r-=1
            if 0<=r<self.R and 0<=c<self.C:
                self.ans.append([r,c])
        self.cur_length+=1
        return r,c

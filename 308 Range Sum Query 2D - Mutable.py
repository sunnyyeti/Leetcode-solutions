# Given a 2D matrix matrix, handle multiple queries of the following types:

# Update the value of a cell in matrix.
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

# Example 1:


# Input
# ["NumMatrix", "sumRegion", "update", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
# Output
# [null, 8, null, 10]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e. sum of the left red rectangle)
# numMatrix.update(3, 2, 2);       // matrix changes from left image to right image
# numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e. sum of the right red rectangle)
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -105 <= matrix[i][j] <= 105
# 0 <= row < m
# 0 <= col < n
# -105 <= val <= 105
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion and update.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows,self.cols = len(matrix),len(matrix[0])
        self.bit = [[0]*(self.cols+1)  for _ in range(self.rows+1)]
        self.num = [[0]*self.cols for _ in matrix]
        self.matrix = matrix
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r,c,matrix[r][c])
        

    def update(self, row: int, col: int, val: int) -> None:
        #print(f"update {row},{col}->{val}")
        old = self.num[row][col]
        delta = val-old
        self.num[row][col] = val
        r = row+1
        #c += col+1
        while r <=self.rows:
            c = col + 1
            while c <= self.cols:
                self.bit[r][c] += delta
                c += c&(-c)
            r += r&(-r)
            
    def get_sum(self,row:int,col:int)->int:
        r = row+1
        ans = 0
        while r>0:
            c = col+1
            while c>0:
                ans += self.bit[r][c]
                c -= c&(-c)
            r -= r&(-r)
        return ans
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2,col2)-\
               self.get_sum(row1-1,col2)-\
               self.get_sum(row2,col1-1) + \
               self.get_sum(row1-1,col1-1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
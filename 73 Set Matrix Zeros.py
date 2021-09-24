# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def set_zero_row(r):
            for c in range(cols):
                matrix[r][c] = 0

        def set_zero_col(c):
            for r in range(rows):
                matrix[r][c] = 0
        rows, cols = len(matrix), len(matrix[0])
        first_row, first_col = False, False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = matrix[0][c] = 0
                    if r == 0:
                        first_row = True
                    if c == 0:
                        first_col = True
        for c in range(1, cols):
            if matrix[0][c] == 0:
                #print(f"set col {c}")
                set_zero_col(c)
        for r in range(1, rows):
            if matrix[r][0] == 0:
                #print(f"set row {r}")
                set_zero_row(r)
        if first_row:
            set_zero_row(0)
        if first_col:
            set_zero_col(0)

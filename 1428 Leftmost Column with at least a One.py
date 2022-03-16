# (This problem is an interactive problem.)

# A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

# You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
# BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

# For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

 

# Example 1:



# Input: mat = [[0,0],[1,1]]
# Output: 0
# Example 2:



# Input: mat = [[0,0],[0,1]]
# Output: 1
# Example 3:



# Input: mat = [[0,0],[0,0]]
# Output: -1
# Example 4:



# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
 

# Constraints:

# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] is either 0 or 1.
# mat[i] is sorted in non-decreasing order.
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        zeros_ups = [float('-inf')]*rows
        cl,cr = 0,cols-1
        while cl<=cr:
            cmid = (cl+cr)//2
            #has_one = False
            for row in range(rows):
                if cmid<=zeros_ups[row]:
                    continue
                cell = binaryMatrix.get(row,cmid)
                if cell == 0:
                    zeros_ups[row] = max(cmid,zeros_ups[row])
                else:
                    #has_one = 1
                    cr = cmid-1
                    break
            else:
                cl = cmid+1
        return cl if cl<cols else -1
                
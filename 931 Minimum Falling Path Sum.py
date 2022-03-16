# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:

# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum underlined below:
# [[2,1,3],      [[2,1,3],
#  [6,5,4],       [6,5,4],
#  [7,8,9]]       [7,8,9]]
# Example 2:

# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is underlined below:
# [[-19,57],
#  [-40,-5]]
# Example 3:

# Input: matrix = [[-48]]
# Output: -48
 

# Constraints:

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(len(matrix)-2,-1,-1):
            cur_r = matrix[r]
            for c,ele in enumerate(cur_r):
                nr = r+1
                min_path = float("inf")
                for nc in [c-1,c,c+1]:
                    if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]):
                        min_path = min(min_path,matrix[nr][nc])
                matrix[r][c] = ele+min_path
        return min(matrix[0])
            
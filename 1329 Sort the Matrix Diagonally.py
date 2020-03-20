# Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

# Example 1:


# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort_d(r,c):
            sr,sc = r,c
            all_eles = []
            while 0<=r<rows and 0<=c<cols:
                all_eles.append(mat[r][c])
                r+=1
                c+=1
            all_eles.sort()
            r,c = sr,sc
            i = 0
            while 0<=r<rows and 0<=c<cols:
                mat[r][c] = all_eles[i]
                r+=1
                c+=1
                i+=1
            
        rows,cols = len(mat),len(mat[0])
        for c in reversed(range(cols)):
            sort_d(0,c)
        for r in range(1,rows):
            sort_d(r,0)
        return mat
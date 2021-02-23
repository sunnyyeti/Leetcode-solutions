# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.

# Accepted
# 273.7K
# Submissions
# 644K
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        import bisect
        row = bisect.bisect_left(list(next(zip(*matrix))),target)
        if row<len(matrix) and matrix[row][0]==target:
            return True
        for r in range(row):
            col = bisect.bisect_left(matrix[r],target)
            if col<len(matrix[0]) and matrix[r][col]==target:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr1,nr2,nc1,nc2,flag = self.search(matrix,0,len(matrix)-1,0,len(matrix[0])-1,target)
        while flag is None:
            nr1,nr2,nc1,nc2,flag = self.search(matrix,nr1,nr2,nc1,nc2,target)
        return flag
        
    
    
    def search(self,matrix,r1,r2,c1,c2,target):
        rs,re = r1,r2
        while rs<=re:
            mid = (rs+re)//2
            if matrix[mid][c2]<target:
                rs = mid+1
            elif matrix[mid][c2]>target:
                re = mid-1
            else:
                return r1,r2,c1,c2,True
        new_r1 = rs
        rs,re = r1,r2
        while rs<=re:
            mid = (rs+re)//2
            if matrix[mid][c1]<target:
                rs = mid+1
            elif matrix[mid][c1]>target:
                re = mid-1
            else:
                return r1,r2,c1,c2,True
        new_r2 = re
        cs,ce = c1,c2
        while cs<=ce:
            mid = (cs+ce)//2
            if matrix[r1][mid]<target:
                cs = mid+1
            elif matrix[r1][mid]>target:
                ce = mid-1
            else:
                return r1,r2,c1,c2,True
        new_c2 = ce
        cs,ce = c1,c2
        while cs<=ce:
            mid = (cs+ce)//2
            if matrix[r2][mid]<target:
                cs = mid+1
            elif matrix[r2][mid]>target:
                ce = mid-1
            else:
                return r1,r2,c1,c2,True
        new_c1 = cs
        if new_r1>new_r2 or new_c1>new_c2:
            return new_r1,new_r2,new_c1,new_c2,False
        else:
            return new_r1,new_r2,new_c1,new_c2,None
        
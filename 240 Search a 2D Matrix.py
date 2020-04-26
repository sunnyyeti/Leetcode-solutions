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
# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

# Return the maximum number of rows that have all values equal after some number of flips.

 

# Example 1:

# Input: [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# Example 2:

# Input: [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal values.
# Example 3:

# Input: [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

# Note:

# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = {}
        inds =set(range(len(matrix[0])))
        for row in matrix:
            ind_1 = set()
            for i,col in enumerate(row):
                if col==1:
                    ind_1.add(i)
            cnt[tuple(ind_1)] = cnt.setdefault(tuple(ind_1),0)+1
            ind_0 = inds-ind_1
            cnt[tuple(ind_0)] = cnt.setdefault(tuple(ind_0),0)+1
        max_rows = float("-inf")
        for k in cnt:
            max_rows = max(max_rows,cnt[k])
        return max_rows
                
# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

# Example 1:


# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0
 

# Constraints:

# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0]*(cols+1) for _ in range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                prefix_sum[r+1][c+1] = prefix_sum[r][c+1] + \
                    prefix_sum[r+1][c]-prefix_sum[r][c]+matrix[r][c]
        #print(prefix_sum)
        ans = 0
        for r1 in range(rows):
            for r2 in range(r1, rows):
                counts = {0: 1}
                for c in range(cols):
                    #print(r1,r2,c)
                    sum_matrix = prefix_sum[r2+1][c+1]-prefix_sum[r1][c+1] - \
                        prefix_sum[r2+1][0]+prefix_sum[r1][0]
                    #print(sum_matrix)
                    remaing = sum_matrix-target
                    #print(counts.get(remaing,0))
                    ans += counts.get(remaing, 0)
                    counts[sum_matrix] = counts.get(sum_matrix, 0)+1
        return ans

# Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

# Example 1:

# Input: mat = [[1,0,1],
#               [1,1,0],
#               [1,1,0]]
# Output: 13
# Explanation:
# There are 6 rectangles of side 1x1.
# There are 2 rectangles of side 1x2.
# There are 3 rectangles of side 2x1.
# There is 1 rectangle of side 2x2. 
# There is 1 rectangle of side 3x1.
# Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
# Example 2:

# Input: mat = [[0,1,1,0],
#               [0,1,1,1],
#               [1,1,1,0]]
# Output: 24
# Explanation:
# There are 8 rectangles of side 1x1.
# There are 5 rectangles of side 1x2.
# There are 2 rectangles of side 1x3. 
# There are 4 rectangles of side 2x1.
# There are 2 rectangles of side 2x2. 
# There are 2 rectangles of side 3x1. 
# There is 1 rectangle of side 3x2. 
# Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
# Example 3:

# Input: mat = [[1,1,1,1,1,1]]
# Output: 21
# Example 4:

# Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
# Output: 5
 

# Constraints:

# 1 <= rows <= 150
# 1 <= columns <= 150
# 0 <= mat[i][j] <= 1
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows,cols = len(mat),len(mat[0])
        prefix_rows = []
        for row in mat:
            cur_pre_fixsum_row = [0]
            for num in row:
                cur_pre_fixsum_row.append(cur_pre_fixsum_row[-1]+num)
            prefix_rows.append(cur_pre_fixsum_row)
        ans = 0
        for c1 in range(cols):
            for c2 in range(c1,cols):
                inter_sums = []
                for sum_row in prefix_rows:
                    inter_sums.append(sum_row[c2+1]-sum_row[c1])
                target = c2-c1+1
                dp = [0]*len(inter_sums)
                for i,itsum in enumerate(inter_sums):
                    if itsum < target:
                        dp[i] = 0
                    else:
                        dp[i] = dp[i-1]+1
                    ans += dp[i]
        return ans
                
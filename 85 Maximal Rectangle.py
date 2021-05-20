# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = []
# Output: 0
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
# Example 4:

# Input: matrix = [["1"]]
# Output: 1
# Example 5:

# Input: matrix = [["0","0"]]
# Output: 0
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dp = [[0]*len(matrix[0]) for _ in matrix]
        max_area = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]=="1":
                    if c==0 or matrix[r][c-1]==0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = dp[r][c-1]+1
                    tmp_max = dp[r][c]
                    width = tmp_max
                    pr = r-1
                    while pr>=0 and dp[pr][c]:
                        width = min(width,dp[pr][c])
                        tmp_max = max(tmp_max,width*(r-pr+1))
                        pr-=1
                    #print(r,c,tmp_max)
                    max_area = max(max_area,tmp_max)
        return max_area
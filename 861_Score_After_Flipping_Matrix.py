# 861. Score After Flipping Matrix
# Medium

# 333

# 88

# Favorite

# Share
# We have a two dimensional matrix A where each value is 0 or 1.

# A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

# After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

# Return the highest possible score.

 

# Example 1:

# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 

# Note:

# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        cols = {}
        for row in A:
            if row[0]!=1:
                apply = lambda x:1-x
            else:
                apply = lambda x:x
            for c in range(len(row)):
                row[c]=apply(row[c])
                if row[c]:
                    cols[c] = cols.get(c,0)+1

        row_cnt = len(A)
        col_cnt = len(A[0])
        ans = 0
        for c in range(col_cnt):
            v = cols.get(c,0)
            ans+=2**(col_cnt-c-1)*max(v,row_cnt-v)
        return ans
        
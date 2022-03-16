# Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

# i - k <= r <= i + k,
# j - k <= c <= j + k, and
# (r, c) is a valid position in the matrix.


# Example 1:

# Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1
# Output: [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
# Example 2:

# Input: mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 2
# Output: [[45, 45, 45], [45, 45, 45], [45, 45, 45]]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n, k <= 100
# 1 <= mat[i][j] <= 100
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def get_from(arr, r, c):
            #print(arr)
            if 0 <= r < len(arr) and 0 <= c < len(arr[0]):
                return arr[r][c]
            return 0
        prefix_sum = [[0]*len(mat[0]) for _ in mat]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                prefix_sum[r][c] = get_from(
                    prefix_sum, r-1, c)+get_from(prefix_sum, r, c-1)-get_from(prefix_sum, r-1, c-1)+mat[r][c]
        #print(prefix_sum)
        answer = [[0]*len(mat[0]) for _ in mat]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                min_r = max(0, r-k)
                max_r = min(len(mat)-1, r+k)
                min_c = max(0, c-k)
                max_c = min(len(mat[0])-1, c+k)
                answer[r][c] = get_from(prefix_sum, max_r, max_c)-get_from(prefix_sum, min_r-1, max_c)-get_from(
                    prefix_sum, max_r, min_c-1)+get_from(prefix_sum, min_r-1, min_c-1)
        return answer

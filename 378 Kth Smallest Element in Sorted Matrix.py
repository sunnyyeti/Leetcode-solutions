# Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5
 

# Constraints:

# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -109 <= matrix[i][j] <= 109
# All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
# 1 <= k <= n2
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(matrix[0][0],0,0)]
        cnt = 0
        seen = {(0,0)}
        while True:
            value,r,c = heapq.heappop(heap)
            cnt+=1
            if cnt==k:
                return value
            if c<len(matrix[0])-1 and (r,c+1) not in seen:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
                seen.add((r,c+1))
            if r<len(matrix)-1 and (r+1,c) not in seen:
                heapq.heappush(heap,(matrix[r+1][c],r+1,c))
                seen.add((r+1,c))
        
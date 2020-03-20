# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

# Return the number of cells with odd values in the matrix after applying the increment to all indices.

 

# Example 1:


# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:


# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

# Constraints:

# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        odd_rows = set()
        odd_cols = set()
        for r,c in indices:
            if r not in odd_rows:
                odd_rows.add(r)
            else:
                odd_rows.remove(r)
            if c not in odd_cols:
                odd_cols.add(c)
            else:
                odd_cols.remove(c)
        ans = len(odd_rows)*m+(n-2*len(odd_rows))*len(odd_cols) #先确定奇数行，那些行上面的数都是奇数，然后确定奇数列，那一列上对应的奇数行变偶数，偶数行变奇数
        return ans
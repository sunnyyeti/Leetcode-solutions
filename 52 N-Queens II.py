# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 9
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag = set()
        diag2 = set()
        cnt = 0
        def bt(row):
            nonlocal cnt
            if row==n:
                cnt += 1
                return
            for c in range(n):
                if c not in cols and (c-row) not in diag and (row+c) not in diag2:
                    cols.add(c)
                    diag.add(c-row)
                    diag2.add(row+c)
                    bt(row+1)
                    cols.remove(c)
                    diag.remove(c-row)
                    diag2.remove(row+c)
        bt(0)
        return cnt
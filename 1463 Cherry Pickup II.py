# Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

# You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

# Return the maximum number of cherries collection using both robots  by following the rules below:

# From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
# When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
# When both robots stay on the same cell, only one of them takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in the grid.
 

# Example 1:



# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.
# Example 2:



# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
# Example 3:

# Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
# Output: 22
# Example 4:

# Input: grid = [[1,1],[1,1]]
# Output: 4
 

# Constraints:

# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100 
class Solution:
    def cherryPickup(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        cur_row = rows - 1
        reached_cols = min(cur_row + 1, cols)
        dp1 = [[0] * reached_cols for _ in range(reached_cols)]
        for i in range(reached_cols):
            for j in range(reached_cols):
                aj = cols - 1 - j
                if i != aj:
                    dp1[i][j] = grid[cur_row][i] + grid[cur_row][aj]
                else:
                    dp1[i][j] = grid[cur_row][i]
        while cur_row > 0:
            cur_row -= 1
            reached_cols = min(cur_row + 1, cols)
            dp2 = [[0] * reached_cols for _ in range(reached_cols)]
            #print("cur_row:", cur_row)
            #print("reached cols:", reached_cols)
            for i in range(reached_cols):
                for j in range(reached_cols):
                    aj = cols - 1 - j
                    #print(i, j)
                    if i != aj:
                        dp2[i][j] = grid[cur_row][i] + grid[cur_row][aj]
                    else:
                        dp2[i][j] = grid[cur_row][i]
                    next_row_max = float("-inf")
                    for delta_col_i in [-1, 0, 1]:
                        next_col_i = i + delta_col_i
                        if 0 <= next_col_i < cols:
                            for delta_col_j in [-1, 0, 1]:
                                next_col_aj = aj + delta_col_j
                                # next_col_j = j-delta_col_j
                                if 0 <= next_col_aj < cols:
                                    # print("next")
                                    # print(next_col_i,next_col_j)
                                    next_col_j = cols - 1 - next_col_aj
                                    tmp = dp1[next_col_i][next_col_j]
                                    next_row_max = max(next_row_max, tmp)
                    dp2[i][j] += next_row_max
            dp1 = dp2
        return dp1[0][0]


        
from functools import cache
from itertools import product
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        @cache
        def max_fruits(row,col1,col2):
            f1 = grid[row][col1]
            f2 = grid[row][col2]
            f = f1+f2 if col1!=col2 else f1
            next_row = row+1
            if next_row >= rows:
                return f
            next_col1s = [col1,col1-1,col1+1]
            next_col2s = [col2,col2-1,col2+1]
            next_f = float("-inf")
            for nc1,nc2 in product(next_col1s,next_col2s):
                if 0<=nc1<cols and 0<=nc2<cols:
                    next_f = max(next_f,max_fruits(next_row,nc1,nc2))
            return f+next_f
        return max_fruits(0,0,cols-1)
            
        
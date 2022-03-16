# You are given an n x n integer matrix grid where grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

# In the end, the skyline when viewed from all four directions of the grid (i.e., top, bottom, left, and right) must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.

# Return the maximum total sum that the height of the buildings can be increased.

# Note that all buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

 

# Example 1:


# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: 
# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]
# The grid after increasing the height of buildings without affecting skylines is:
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
# Example 2:

# Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
# Output: 0
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 2 <= n <= 50
# 0 <= grid[i][j] <= 100
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(r) for r in grid]
        col_max = [max(t) for t in zip(*grid)]
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans += min(row_max[r], col_max[c])-grid[r][c]
        return ans

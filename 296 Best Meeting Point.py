# Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

# The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

# Example 1:


# Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 6
# Explanation: Given three friends living at (0,0), (0,4), and (2,2).
# The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
# So return 6.
# Example 2:

# Input: grid = [[1,1]]
# Output: 1
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is either 0 or 1.
# There will be at least two friends in the grid.
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # extend the solution in 1 dimensional to 2 dims
        #topleft
        dis1 = [[0]*len(_) for _ in grid]
        for r in range(len(grid)):
            cur_row_ones = 0
            cur_row_dis = 0
            for c in range(len(grid[0])):
                cur_ele = grid[r][c]
                cur_row_dis += cur_row_ones
                cur_row_ones += cur_ele == 1
                if r > 0:
                    topleft_dis, topleft_ones = dis1[r-1][c]
                else:
                    topleft_dis, topleft_ones = 0, 0
                dis = topleft_dis+topleft_ones+cur_row_dis
                ones = topleft_ones + cur_row_ones
                dis1[r][c] = (dis, ones)
        #print(dis1)
        #bottom right
        dis2 = [[0]*len(_) for _ in grid]
        for r in reversed(range(len(grid))):
            cur_row_ones = 0
            cur_row_dis = 0
            for c in reversed(range(len(grid[0]))):
                cur_ele = grid[r][c]
                cur_row_dis += cur_row_ones
                cur_row_ones += cur_ele == 1
                if r < len(grid) - 1:
                    br_dis, br_ones = dis2[r+1][c]
                else:
                    br_dis, br_ones = 0, 0
                dis = br_dis+br_ones+cur_row_dis
                ones = br_ones+cur_row_ones
                dis2[r][c] = (dis, ones)
        #print(dis2)
        #topright
        dis3 = [[0]*len(_) for _ in grid]
        for r in range(len(grid)):
            cur_row_ones = 0
            cur_row_dis = 0
            for c in reversed(range(len(grid[0]))):
                cur_ele = grid[r][c]
                cur_row_dis += cur_row_ones
                cur_row_ones += cur_ele == 1
                if r > 0:
                    tr_dis, tr_ones = dis3[r-1][c]
                else:
                    tr_dis, tr_ones = 0, 0
                dis = tr_dis+tr_ones+cur_row_dis
                ones = tr_ones+cur_row_ones
                dis3[r][c] = (dis, ones)
        #print(dis3)
        #bottom left
        dis4 = [[0]*len(_) for _ in grid]
        for r in reversed(range(len(grid))):
            cur_row_ones = 0
            cur_row_dis = 0
            for c in range(len(grid[0])):
                cur_ele = grid[r][c]
                cur_row_dis += cur_row_ones
                cur_row_ones += cur_ele == 1
                if r < len(grid)-1:
                    bl_dis, bl_ones = dis4[r+1][c]
                else:
                    bl_dis, bl_ones = 0, 0
                dis = bl_dis+bl_ones+cur_row_dis
                ones = bl_ones+cur_row_ones
                dis4[r][c] = (dis, ones)
        #print(dis4)
        ans = float('inf')
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                cur_dis = dis1[r][c][0]+dis2[r][c][0]
                if r > 0 and c < len(grid[0])-1:
                    cur_dis += dis3[r-1][c+1][0]+dis3[r-1][c+1][1]*2
                if r < len(grid)-1 and c > 0:
                    cur_dis += dis4[r+1][c-1][0]+dis4[r+1][c-1][1]*2
                ans = min(ans, cur_dis)
                #print(r,c,cur_dis)
        return ans

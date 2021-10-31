# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

# Return the maximum number of points you can achieve.

# abs(x) is defined as:

# x for x >= 0.
# -x for x < 0.
 

# Example 1:


# Input: points = [[1,2,3],[1,5,1],[3,1,1]]
# Output: 9
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
# You add 3 + 5 + 3 = 11 to your score.
# However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
# Your final score is 11 - 2 = 9.
# Example 2:


# Input: points = [[1,5],[2,3],[4,2]]
# Output: 11
# Explanation:
# The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
# You add 5 + 3 + 4 = 12 to your score.
# However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
# Your final score is 12 - 1 = 11.
 

# Constraints:

# m == points.length
# n == points[r].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 0 <= points[r][c] <= 105
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return max(points[0])
        rows,cols = len(points),len(points[0])
        left = [float("-inf")]*cols
        right= [float("-inf")]*cols
        first_row = points[0]
        prev = float("-inf")
        for i,cell in enumerate(first_row):
            left[i] = max(cell+i,prev)
            prev = left[i]
        prev = float("-inf")
        for i in range(cols-1,-1,-1):
            right[i] = max(first_row[i]-i,prev)
            prev = right[i]
        for r in range(1,len(points)):
            new_left = [0]*cols
            new_right= [0]*cols
            max_score= [0]*cols
            prev = float("-inf")
            for c in range(cols):
                leftc = left[c]
                rightc = right[c]
                max_score[c] = max(leftc+points[r][c]-c,rightc+points[r][c]+c)
                new_left[c] = max(prev,max_score[c]+c)
                prev = new_left[c]
            prev = float("-inf")
            for c in range(cols-1,-1,-1):
                new_right[c] = max(prev,max_score[c]-c)
                prev = new_right[c]
            left,right = new_left,new_right
        return max(max_score)
                
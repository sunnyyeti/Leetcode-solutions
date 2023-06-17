# You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

# The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

# Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# You must write an algorithm with less than O(mn) runtime complexity

 

# Example 1:


# Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
# Output: 6
# Example 2:

# Input: image = [["1"]], x = 0, y = 0
# Output: 1
 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 100
# image[i][j] is either '0' or '1'.
# 1 <= x < m
# 1 <= y < n
# image[x][y] == '1'.
# The black pixels in the image only form one component.
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows,cols = len(image),len(image[0])
        left_y,right_y = y,cols-1
        while left_y <= right_y:
            mid_y = left_y+(right_y-left_y)//2
            if any(image[r][mid_y]=='1' for r in range(rows)):
                left_y = mid_y+1
            else:
                right_y = mid_y-1
        right_most_y = right_y
        left_y,right_y = 0,y
        while left_y <= right_y:
            mid_y = left_y+(right_y-left_y)//2
            if any(image[r][mid_y]=='1' for r in range(rows)):
                right_y = mid_y-1
            else:
                left_y = mid_y+1
        left_most_y = left_y
        lower_x,upper_x = 0,x
        while lower_x <= upper_x:
            mid_x = (lower_x+upper_x)//2
            if any(image[mid_x][c]=='1' for c in range(cols)):
                upper_x = mid_x -1
            else:
                lower_x = mid_x + 1
        lower_most_x = lower_x
        lower_x,upper_x = x,rows-1
        while lower_x <= upper_x:
            mid_x = (lower_x+upper_x)//2
            if any(image[mid_x][c]=='1' for c in range(cols)):
                lower_x = mid_x + 1
            else:
                upper_x = mid_x - 1
        upper_most_x = upper_x
        return (upper_most_x-lower_most_x+1)*(right_most_y-left_most_y+1)
            
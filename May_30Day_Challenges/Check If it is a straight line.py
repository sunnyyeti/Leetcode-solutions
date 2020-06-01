# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

# Example 1:



# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:



# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
 

# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def slope(p1,p2):
            delta_y = p2[1]-p1[1]
            delta_x = p2[0]-p1[0]
            if delta_x==0:
                return float("inf")
            return delta_y/delta_x
        coordinates.sort(key=lambda x:x[0])
        ini_slope = slope(coordinates[0],coordinates[1])
        return all(ini_slope==slope(coordinates[i-1],coordinates[i]) for i in range(2,len(coordinates)))
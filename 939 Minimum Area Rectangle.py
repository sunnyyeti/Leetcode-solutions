# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

# If there isn't any rectangle, return 0.

 

# Example 1:

# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:

# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
 

# Note:

# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x = {}
        y = {}
        for p in points:
            x.setdefault(p[0],set()).add(tuple(p))
            y.setdefault(p[1],set()).add(tuple(p))
        area = float("inf")
        for bl in points:
            for ul in x[bl[0]]:
                if ul[1] > bl[1]:
                    for br in y[bl[1]]:
                        if br[0]>bl[0]:
                            if (br[0],ul[1]) in x[br[0]]:
                                area = min(area,(br[0]-bl[0])*(ul[1]-bl[1]))
        return 0 if area==float('inf') else area
        
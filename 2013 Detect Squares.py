// You are given a stream of points on the X-Y plane. Design an algorithm that:

// Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
// Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
// An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

// Implement the DetectSquares class:

// DetectSquares() Initializes the object with an empty data structure.
// void add(int[] point) Adds a new point point = [x, y] to the data structure.
// int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
 

// Example 1:


// Input
// ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
// [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
// Output
// [null, null, null, null, 1, 0, null, 2]

// Explanation
// DetectSquares detectSquares = new DetectSquares();
// detectSquares.add([3, 10]);
// detectSquares.add([11, 2]);
// detectSquares.add([3, 2]);
// detectSquares.count([11, 10]); // return 1. You can choose:
//                                //   - The first, second, and third points
// detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
// detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
// detectSquares.count([11, 10]); // return 2. You can choose:
//                                //   - The first, second, and third points
//                                //   - The first, third, and fourth points

from collections import Counter
class DetectSquares:

    def __init__(self):
        self.cnter = Counter()
        self.xaxis = {}
        self.yaxis = {}

    def add(self, point: List[int]) -> None:
        tp = tuple(point)
        self.xaxis.setdefault(point[0],set()).add(tp)
        self.yaxis.setdefault(point[1],set()).add(tp)
        self.cnter[tp]+=1

    def count(self, point: List[int]) -> int:
        all_x = self.xaxis.get(point[0],set())
        all_y = self.yaxis.get(point[1],set())
        ans = 0
        for xp in all_x:
            cnt_xp = self.cnter[xp]
            for yp in all_y:
                cnt_yp = self.cnter[yp]
                des = (yp[0],xp[1])
                delta_x = abs(des[0]-point[0])
                delta_y = abs(des[1]-point[1])
                if delta_x == delta_y and delta_x:
                    cnt_des = self.cnter[des]
                    ans += cnt_xp*cnt_yp*cnt_des
        return ans
                
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
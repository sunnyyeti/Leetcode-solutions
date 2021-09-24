# You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

# Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

# It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 

# Example 1:

# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
# Example 2:

# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 

# Constraints:

# 2 <= points.length <= 105
# points[i].length == 2
# -108 <= xi, yi <= 108
# 0 <= k <= 2 * 108
# xi < xj for all 1 <= i < j <= points.length
# xi form a strictly increasing sequence.
import math, bisect
class SegTree:
    def __init__(self,arr):
        length = len(arr)
        height = math.log(length,2)
        height = int(math.ceil(height))
        self.tree = [0]*(2**(height+1)-1)
        self._construct(0,0,len(arr)-1,arr)
        self.length = length
        
    def _construct(self,tree_ind,scope_s,scope_e,arr):
        if scope_s == scope_e:
            self.tree[tree_ind] = arr[scope_s]
            return self.tree[tree_ind]
        mid = (scope_s+scope_e)//2
        left = self._construct(tree_ind*2+1,scope_s,mid,arr)
        right = self._construct(tree_ind*2+2,mid+1,scope_e,arr)
        self.tree[tree_ind] = max(left,right)
        return self.tree[tree_ind]
        
    def _query(self,tree_ind,scope_s,scope_e,query_s,query_e):
        if query_e < scope_s or query_s > scope_e:
            return float('-inf')
        elif query_e>=scope_e and query_s <= scope_s:
            return self.tree[tree_ind]
        else:
            mid = (scope_s+scope_e)//2
            left = self._query(tree_ind*2+1,scope_s,mid,query_s,query_e)
            right = self._query(tree_ind*2+2,mid+1,scope_e,query_s,query_e)
            return max(left,right)
        
    def query(self,start,end):
        return self._query(0,0,self.length-1,start,end)
        
        
            
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        x_y_sum = [p[0]+p[1] for p in points]
        x = [p[0] for p in points]
        seg_tree = SegTree(x_y_sum)
        ans = float("-inf")
        #y_i-x_i + y_j+x_j
        for i,p in enumerate(points):
            r = bisect.bisect_right(x,p[0]+k)
            if r > i+1:
                max_sum = seg_tree.query(i+1,r-1)
                ans = max(ans,max_sum+p[1]-p[0])
        return ans
                
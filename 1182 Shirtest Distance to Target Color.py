# You are given an array colors, in which there are three colors: 1, 2 and 3.

# You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

# Example 1:

# Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]
# Explanation: 
# The nearest 3 from index 1 is at index 4 (3 steps away).
# The nearest 2 from index 2 is at index 2 itself (0 steps away).
# The nearest 1 from index 6 is at index 3 (3 steps away).
# Example 2:

# Input: colors = [1,2], queries = [[0,3]]
# Output: [-1]
# Explanation: There is no 3 in the array.
 

# Constraints:

# 1 <= colors.length <= 5*10^4
# 1 <= colors[i] <= 3
# 1 <= queries.length <= 5*10^4
# queries[i].length == 2
# 0 <= queries[i][0] < colors.length
# 1 <= queries[i][1] <= 3
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        cloest = [[float("inf"),float("inf"),float("inf")] for _ in colors] #distance to 1,2,3
        ind1 = float('-inf')
        ind2 = float('-inf')
        ind3 = float('-inf')
        prevs = {1:ind1,2:ind2,3:ind3}
        for ind,color in enumerate(colors):
            cur_dis = cloest[ind]
            cur_dis[color-1] = 0
            prevs[color] = ind
            for c in [1,2,3]:
                if c!=color:
                    cur_dis[c-1] = min(cur_dis[c-1],ind-prevs[c])
        ind1 = float('inf')
        ind2 = float('inf')
        ind3 = float('inf')
        prevs = {1:ind1,2:ind2,3:ind3}
        for ind in reversed(range(len(colors))):
            color = colors[ind]
            cur_dis = cloest[ind]
            cur_dis[color-1] = 0
            prevs[color] = ind
            for c in [1,2,3]:
                if c!=color:
                    cur_dis[c-1] = min(cur_dis[c-1],prevs[c]-ind)
        #print(cloest)
        ans = []
        for q,color in queries:
            ans.append(cloest[q][color-1] if cloest[q][color-1]!=float("inf") else -1)
        return ans
# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

# What is the largest possible number of moves we can make?

 

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
 

# Note:

# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        x_points = {}
        y_points = {}
        self.nbs = {}
        for x,y in stones:
            x_points.setdefault(x,[]).append((x,y))
            y_points.setdefault(y,[]).append((x,y))
        for x,y in stones:## Find all connected points
            nbset = self.nbs.setdefault((x,y),set())
            for p in x_points[x]:
                if p!=(x,y):
                    nbset.add(p)
            for p in y_points[y]:
                if p!=(x,y):
                    nbset.add(p)
        self.visited = set()
        cnt = 0
        for x,y in stones:
            if (x,y) not in self.visited:
                loopcnt = self.dfs((x,y))
                cnt+=loopcnt-1
        return cnt
    def dfs(self,p):
        self.visited.add(p)
        point_cnt = 1
        for next_point in self.nbs[p]:
            if next_point not in self.visited:
                point_cnt+=self.dfs(next_point)
        return point_cnt
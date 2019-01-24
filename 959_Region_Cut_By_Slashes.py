# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

# (Note that backslash characters are escaped, so a \ is represented as "\\".)

# Return the number of regions.

 

# Example 1:

# Input:
# [
  # " /",
  # "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:

# Example 2:

# Input:
# [
  # " /",
  # "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:

# Example 3:

# Input:
# [
  # "\\/",
  # "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:

# Example 4:

# Input:
# [
  # "/\\",
  # "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:

# Example 5:

# Input:
# [
  # "//",
  # "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:

 

# Note:

# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] is either '/', '\', or ' '.

class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        self.N = len(grid)
        self.neighbours = {}
        self.visited = {}
        for i,slashes in enumerate(grid):
            for j,c in enumerate(slashes):  
                if c==" ":
                    continue
                if c=="/":
                    p1 = (j+1,i)
                    p2 = (j,i+1)
                if c=="\\":
                    p1 = (j,i)
                    p2 = (j+1,i+1)
                self.neighbours.setdefault(p1,[]).append(p2)
                self.neighbours.setdefault(p2,[]).append(p1)
                self.visited.setdefault(p1,False)
                self.visited.setdefault(p2,False)
        self.passed_path = set()
        self.cnt = 1
        for point in self.neighbours.keys():
            if not self.visited[point] and self.isboundry(point):
                self.dfs(point)
        for point in self.neighbours.keys():
            if not self.visited[point]:
                self.dfs(point)
        return self.cnt
    def isboundry(self,point):
        x,y = point
        return x==0 or x==self.N or y==0 or y==self.N
    
    def dfs(self,point):
        self.visited[point]=True
        for next_point in self.neighbours[point]:
            if (point,next_point) not in self.passed_path:
                self.passed_path.add((point,next_point))
                self.passed_path.add((next_point,point))
                if self.visited[next_point] or self.isboundry(next_point):
                    self.cnt+=1
                self.dfs(next_point)
                
# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

 

# Example 1:



# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# Example 2:



# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.
# Example 3:



# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        rpos = {}
        cpos = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rpos.setdefault(i,set()).add(j)
                    cpos.setdefault(j,set()).add(i)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rpos[i].remove(j)
                    cpos[j].remove(i)
                    if rpos[i] or cpos[j]:
                        cnt+=1
                    rpos[i].add(j)
                    cpos[j].add(i)
        return cnt
# Storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

# The game is represented by a grid of size m x n, where each element is a wall, floor, or a box.

# Your task is move the box 'B' to the target position 'T' under the following rules:

# Player is represented by character 'S' and can move up, down, left, right in the grid if it is a floor (empy cell).
# Floor is represented by character '.' that means free cell to walk.
# Wall is represented by character '#' that means obstacle  (impossible to walk there). 
# There is only one box 'B' and one target cell 'T' in the grid.
# The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
# The player cannot walk through the box.
# Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.

 

# Example 1:



# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#",".","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 3
# Explanation: We return only the number of times the box is pushed.
# Example 2:

# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T","#","#","#","#"],
#                ["#",".",".","B",".","#"],
#                ["#","#","#","#",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: -1
# Example 3:

# Input: grid = [["#","#","#","#","#","#"],
#                ["#","T",".",".","#","#"],
#                ["#",".","#","B",".","#"],
#                ["#",".",".",".",".","#"],
#                ["#",".",".",".","S","#"],
#                ["#","#","#","#","#","#"]]
# Output: 5
# Explanation:  push the box down, left, left, up and up.
# Example 4:

# Input: grid = [["#","#","#","#","#","#","#"],
#                ["#","S","#",".","B","T","#"],
#                ["#","#","#","#","#","#","#"]]
# Output: -1
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 20
# 1 <= n <= 20
# grid contains only characters '.', '#',  'S' , 'T', or 'B'.
# There is only one character 'S', 'B' and 'T' in the grid.
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def connected(i1,j1,i2,j2,bi,bj):
            if i2<0 or i2>=rows or j2<0 or j2>=cols or grid[i2][j2]=="#":
                return False
            grid[bi][bj] = 'B'
            grid[i1][j1] = 'S'
            stack = [(i1,j1)]
            visited = {(i1,j1)}
            while stack:
                i,j = stack.pop()
                if (i,j)==(i2,j2):
                    grid[bi][bj] = grid[i1][j1] = '.'
                    return True
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni,nj = i+di,j+dj
                    if 0<=ni<rows and 0<=nj<cols and grid[ni][nj] in [".","T"] and (ni,nj) not in visited:
                        stack.append((ni,nj))
                        visited.add((ni,nj))
            grid[bi][bj] = grid[i1][j1] = '.'
            return False
        from collections import deque
        import copy
        rows,cols = len(grid),len(grid[0])
        Ti,Tj = next(  (i,j) for i in range(rows) for j in range(cols) if grid[i][j]=="T"  )
        Bi,Bj = next(  (i,j) for i in range(rows) for j in range(cols) if grid[i][j]=="B"  )
        Si,Sj = next(  (i,j) for i in range(rows) for j in range(cols) if grid[i][j]=="S"  )
        grid[Bi][Bj] = grid[Si][Sj] = '.'
        visited = set([(Bi,Bj,Si,Sj)])
        q = deque([(Bi,Bj,Si,Sj,0)])
        while q:
            ci,cj,si,sj,step = q.popleft()
            if (ci,cj)==(Ti,Tj):
                return step
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = ci+di,cj+dj
                if 0<=ni<rows and 0<=nj<cols and grid[ni][nj]!="#" and (ni,nj,ci,cj) not in visited and connected(si,sj,ci-di,cj-dj,ci,cj):
                    q.append((ni,nj,ci,cj,step+1))
                    visited.add((ni,nj,ci,cj))
        return -1
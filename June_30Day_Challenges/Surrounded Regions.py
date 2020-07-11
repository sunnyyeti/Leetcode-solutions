# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not grid:
            return
        ns = set()
        visited = set()
        r,c = len(grid),len(grid[0])
        def stretch(i,j):
                ns.add((i,j))
                visited.add((i,j))
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni = i+di
                    nj = j+dj
                    if 0<=ni<r and 0<=nj<c and (ni,nj) not in visited and grid[ni][nj]=='O':
                        stretch(ni,nj)
        for i in range(r):
                if (i,0) not in visited and grid[i][0]=='O':
                    stretch(i,0)
                if (i,c-1) not in visited and grid[i][c-1]=='O':
                    stretch(i,c-1)
        for j in range(c):
                if (0,j) not in visited and grid[0][j]=='O':
                    stretch(0,j)
                if (r-1,j) not in visited and grid[r-1][j]=='O':
                    stretch(r-1,j)
        for i in range(r):
                for j in range(c):
                    if grid[i][j]=='O' and (i,j) not in ns:
                        grid[i][j]='X'
                    
        
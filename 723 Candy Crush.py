# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

# The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the stable board.

 

# Example 1:


# Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
# Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
# Example 2:

# Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 3 <= m, n <= 50
# 1 <= board[i][j] <= 2000
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        removed = self.detect_candies(board)
        while removed:
            #print(removed)
            board = self.refill_board(board,removed)
            #print(board)
            removed = self.detect_candies(board)
        return board
        
        
    def refill_board(self,board,removed):
        def next_valid(col):
            for i in reversed(range(len(board))):
                if (i,j) not in removed:
                    yield board[i][j]
            while True:
                yield 0
        for j in range(len(board[0])):
            col_generator = next_valid(j)
            for i in range(len(board)-1,-1,-1):
                board[i][j] = next(col_generator)
        return board
    def detect_candies(self,board):
        lefts = [[0  for _ in board[0]]  for _ in board]
        ups = [[0  for _ in board[0]] for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 0:
                    if i==0:
                        ups[i][j] = 1
                    else:
                        ups[i][j] = 1 if board[i][j]!=board[i-1][j] else ups[i-1][j]+1
                    if j==0:
                        lefts[i][j] = 1
                    else:
                        lefts[i][j] = 1 if board[i][j]!=board[i][j-1] else lefts[i][j-1]+1
        removed = set()
        for i in range(len(board)):
            j = len(board[0])-1
            while j>=2:
                if lefts[i][j] >= 3:
                    for k in range(j,j-lefts[i][j],-1):
                        removed.add((i,k))
                j -= max(lefts[i][j],1)
        for j in range(len(board[0])):
            i = len(board)-1
            while i>=2:
                if ups[i][j] >= 3:
                    for k in range(i,i-ups[i][j],-1):
                        removed.add((k,j))
                i-=max(1,ups[i][j])
        return removed
                    
                    
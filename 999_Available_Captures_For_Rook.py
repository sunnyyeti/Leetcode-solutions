# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

# Return the number of pawns the rook can capture in one move.

 

# Example 1:



# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# In this example the rook is able to capture all the pawns.
# Example 2:



# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: 
# Bishops are blocking the rook to capture any pawn.
# Example 3:



# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# The rook can capture the pawns at positions b5, d6 and f5.
 

# Note:

# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
class Solution:
    def numRookCaptures(self, board) -> int:
        for i in range(8):
            flag=False
            for j in range(8):
                if board[i][j] == "R":
                    flag=True
                    break
            if flag:
                break
        ni = i + 1
        ans = 0
        while ni < 8:
            if board[ni][j] == ".":
                ni += 1
            elif board[ni][j] == "B":
                break
            else:
                ans += 1
                break
        ni = i - 1
        while ni >= 0:
            if board[ni][j] == ".":
                ni -= 1
            elif board[ni][j] == "B":
                break
            else:
                ans += 1
                break
        nj = j + 1
        while nj < 8:
            if board[i][nj] == ".":
                nj += 1
            elif board[i][nj] == "B":
                break
            else:
                ans += 1
                break
        nj = j - 1
        while nj >= 0:
            if board[i][nj] == ".":
                nj -= 1
            elif board[i][nj] == "B":
                break
            else:
                ans += 1
                break
        return ans
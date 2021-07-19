# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square x, consists of the following:

# You choose a destination square S with a label in the range [x + 1, x + 6] where S <= n2.
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most size destinations, regardless of the size of the board.
# If S has a snake or ladder, you move to the destination of that snake or ladder. Otherwise, you move to S.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c].

# Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.

# For example, if the board is [[4,-1],[-1,3]] and on the first move, your destination square is 2, then you finish your first move at 3, because you do not continue moving to 4.
# Return the least number of moves required to reach the square n2. If it is not possible, return -1.

 

# Example 1:


# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 [at row 5, column 0].
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 (row 3, column 4) and take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
# Example 2:

# Input: board = [[-1,-1],[-1,3]]
# Output: 1
 

# Constraints:

# n == board.length
# n == board[i].length
# 2 <= n <= 20
# grid[i][j] is either -1 or in the range [1, n2].
# The squares labeled 1 and n2 does not have any ladders or snakes.
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def convert_to_rc(ind):
            rows = (ind-1)//n
            cols = (ind-1) % n
            if rows % 2 == 1:
                cols = n-1-cols
            rows = n-rows-1
            return rows, cols
        queue = deque([(1, 0)])
        seen = {1}
        while queue:
            cur, step = queue.popleft()
            if cur == n*n:
                return step
            for i in range(1, 7):
                next_ind = cur + i
                if next_ind <= n**2:
                    nr, nc = convert_to_rc(next_ind)
                    if board[nr][nc] != -1:
                        next_ind = board[nr][nc]
                    if next_ind not in seen:
                        seen.add(next_ind)
                        queue.append((next_ind, step+1))

        return-1

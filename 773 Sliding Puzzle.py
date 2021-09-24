# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

# Example 1:


# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Example 2:


# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Example 3:


# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Example 4:


# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
 

# Constraints:

# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# Each value board[i][j] is unique.
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target_state = ((1,2,3),(4,5,0))
        state = lambda board: tuple(map(tuple,board))
        queue = deque([(state(board),0)])
        seen = {state(board)}
        def next_states(board_state):
            zero_r,zero_c = next((r,c) for r in range(2) for c in range(3) if board_state[r][c]==0)
            next_board = list(map(list,board_state))
            next_states = []
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = zero_r+dr,zero_c+dc
                if 0<=nr<2 and 0<=nc<3:
                    next_board[zero_r][zero_c],next_board[nr][nc] = next_board[nr][nc],next_board[zero_r][zero_c]
                    next_states.append(state(next_board))
                    next_board[zero_r][zero_c],next_board[nr][nc] = next_board[nr][nc],next_board[zero_r][zero_c]
            return next_states
        
        while queue:
            cur_state,moves = queue.popleft()
            if cur_state == target_state:
                return moves
            for next_state in next_states(cur_state):
                if next_state not in seen:
                    queue.append((next_state,moves+1))
                    seen.add(next_state)
        return -1
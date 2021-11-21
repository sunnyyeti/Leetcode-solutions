# There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n, where pieces[i] describes the type (rook, queen, or bishop) of the ith piece. In addition, you are given a 2D integer array positions also of length n, where positions[i] = [ri, ci] indicates that the ith piece is currently at the 1-based coordinate (ri, ci) on the chessboard.

# When making a move for a piece, you choose a destination square that the piece will travel toward and stop on.

# A rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), or (r, c-1).
# A queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
# A bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
# You must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square.

# Return the number of valid move combinations​​​​​.

# Notes:

# No two pieces will start in the same square.
# You may choose the square a piece is already on as its destination.
# If two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second.
 

# Example 1:


# Input: pieces = ["rook"], positions = [[1,1]]
# Output: 15
# Explanation: The image above shows the possible squares the piece can move to.
# Example 2:


# Input: pieces = ["queen"], positions = [[1,1]]
# Output: 22
# Explanation: The image above shows the possible squares the piece can move to.
# Example 3:


# Input: pieces = ["bishop"], positions = [[4,3]]
# Output: 12
# Explanation: The image above shows the possible squares the piece can move to.
# Example 4:


# Input: pieces = ["rook","rook"], positions = [[1,1],[8,8]]
# Output: 223
# Explanation: There are 15 moves for each rook which results in 15 * 15 = 225 move combinations.
# However, there are two invalid move combinations:
# - Move both rooks to (8, 1), where they collide.
# - Move both rooks to (1, 8), where they collide.
# Thus there are 225 - 2 = 223 valid move combinations.
# Note that there are two valid move combinations that would result in one rook at (1, 8) and the other at (8, 1).
# Even though the board state is the same, these two move combinations are considered different since the moves themselves are different.
# Example 5:


# Input: pieces = ["queen","bishop"], positions = [[5,7],[3,4]]
# Output: 281
# Explanation: There are 12 * 24 = 288 move combinations.
# However, there are several invalid move combinations:
# - If the queen stops at (6, 7), it blocks the bishop from moving to (6, 7) or (7, 8).
# - If the queen stops at (5, 6), it blocks the bishop from moving to (5, 6), (6, 7), or (7, 8).
# - If the bishop stops at (5, 2), it blocks the queen from moving to (5, 2) or (5, 1).
# Of the 288 move combinations, 281 are valid.
 

# Constraints:

# n == pieces.length
# n == positions.length
# 1 <= n <= 4
# pieces only contains the strings "rook", "queen", and "bishop".
# There will be at most one queen on the chessboard.
# 1 <= xi, yi <= 8
# Each positions[i] is distinct.
from itertools import combinations,product
class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        directions = {
            "rook":[(1,0),(-1,0),(0,1),(0,-1)],
            "queen":[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)],
            "bishop":[(1,1),(1,-1),(-1,1),(-1,-1)]
        }
        total_moves = set()
        def bt(positions,dirs,stops):
            #print(positions,dirs,stops)
            nonlocal total_moves
            total_moves.add(tuple(positions))
            new_positions = []
            new_stops = []
            for (r,c),(dr,dc),ifstop in zip(positions,dirs,stops):
                nr,nc = r+dr,c+dc
                if ifstop:
                    new_positions.append((r,c))
                    new_stops.append(True)
                else:
                    if 1<=nr<=8 and 1<=nc<=8:
                        new_positions.append((nr,nc))
                        new_stops.append(False) 
                        #can choose to stop
                    else:
                        new_positions.append((r,c))
                        new_stops.append(True)
                        #force to stop
            non_stops = [i for i,s in enumerate(new_stops) if not s]
            if len(non_stops)==0:
                return
            #indices can continue walking, but can also choose to stop
            if len(set(new_positions)) == len(new_positions):
                bt(new_positions,dirs,new_stops)
                #do not stop cny piece
            for new_stop in range(1,len(non_stops)+1):
                new_stop_inds = combinations(non_stops,new_stop)
                for inds in new_stop_inds:
                    new_new_stops = new_stops[:]
                    new_new_positions = new_positions[:]
                    for ind in inds:
                        new_new_stops[ind] = True
                        new_new_positions[ind] = positions[ind]
                    if not all(new_new_stops) and len(set(new_new_positions)) == len(new_new_positions):
                        bt(new_new_positions,dirs,new_new_stops)
        possible_dirs = [directions[p] for p in pieces]
        all_dir_combinations = list(product(*possible_dirs))
        positions = [tuple(p)  for p in positions ]
        for dir_comb in all_dir_combinations:
            bt(positions,dir_comb,[False]*len(positions))
        return len(total_moves)
        
        
                    
                    
                    
                    
                
            
            
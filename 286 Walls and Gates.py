# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

# Example 1:


# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
# Example 2:

# Input: rooms = [[-1]]
# Output: [[-1]]
# Example 3:

# Input: rooms = [[2147483647]]
# Output: [[2147483647]]
# Example 4:

# Input: rooms = [[0]]
# Output: [[0]]
 

# Constraints:

# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(starts):
            seen = {(s, e) for s, e, d in starts}
            queue = deque(starts)
            while queue:
                cr, cc, dis = queue.popleft()
                rooms[cr][cc] = min(rooms[cr][cc], dis)
                for nr, nc in [(cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1)]:
                    if 0 <= nr < len(rooms) and 0 <= nc < len(rooms[0]) and rooms[nr][nc] != -1 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc, dis+1))
        bfs([(r, c, 0) for r in range(len(rooms))
            for c in range(len(rooms[0])) if rooms[r][c] == 0])
        return rooms

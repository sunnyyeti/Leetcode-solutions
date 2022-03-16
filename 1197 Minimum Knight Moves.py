# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

# Constraints:

# |x| + |y| <= 300
# Accepted
from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def get_nexts(x, y):
            for dy in [-2, -1, 1, 2]:
                cx = 3-abs(dy)
                for dx in [-cx, cx]:
                    yield x+dx, y+dy
        queue = deque([(0, 0, 0)])
        seen = {(0, 0)}
        while queue:
            cx, cy, dis = queue.popleft()
            if (cx, cy) == (x, y):
                return dis
            for nx, ny in get_nexts(cx, cy):
                if (nx, ny) not in seen:
                    queue.append((nx, ny, dis+1))
                    seen.add((nx, ny))

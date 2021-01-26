# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

# Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

# Example 1:

# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

# Note:

# 1 <= p <= 1000
# 0 <= q <= p
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        start = (0,0)
        ends = {(p,0),(p,p),(0,p)}
        dire = 1
        while start not in ends:
            next_x = p-start[0]
            next_y = start[1] + dire*q
            if next_y > p:
                next_y = 2*p-next_y
                dire = -1*dire
            if next_y < 0:
                next_y = -next_y
                dire = -1*dire
            start = (next_x,next_y)
        if start==(p,0):
            return 0
        if start==(p,p):
            return 1
        if start==(0,p):
            return 2
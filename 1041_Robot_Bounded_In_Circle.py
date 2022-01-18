# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinetely.
# Example 3:

# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

# Note:

# 1 <= instructions.length <= 100
# instructions[i] is in {'G', 'L', 'R'}
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_state = (0,0,0)
        for inst in instructions:
            cur_state = self.step(cur_state,inst)
        return cur_state[:2] == (0,0) or cur_state[2] != 0
        
    def step(self, state, inst):
        x,y,d = state
        deltas = {
            0:(0,1), #north
            1:(1,0), #east
            2:(0,-1), # south
            3:(-1,0) #west
        }
        if inst == 'G':
            dx,dy = deltas[d]
            return x+dx,y+dy,d
        elif inst == 'L':
            return x,y,(d-1)%4
        else:
            return x,y,(d+1)%4
        
        
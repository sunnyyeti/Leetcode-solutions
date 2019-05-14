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
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos = (0,0,"up")
        for ins in instructions:
            pos = self.step(pos,ins)
        if pos[0]==pos[1]==0:
            return True
        if pos[-1]!="up":
            return True
        return False
        
    def step(self,pos,ins):
        if ins=="G":
            if pos[-1]=="up":
                return (pos[0],pos[1]+1,pos[2])
            if pos[-1]=="left":
                return (pos[0]-1,pos[1],pos[2])
            if pos[-1]=="right":
                return (pos[0]+1,pos[1],pos[2])
            if pos[-1]=="down":
                return (pos[0],pos[1]-1,pos[2])
        if ins=="L":
            if pos[-1]=="up":
                return (pos[0],pos[1],"left")
            if pos[-1]=="left":
                return (pos[0],pos[1],"down")
            if pos[-1]=="right":
                return (pos[0],pos[1],"up")
            if pos[-1]=="down":
                return (pos[0],pos[1],"right")
        if ins=="R":
            if pos[-1]=="up":
                return (pos[0],pos[1],"right")
            if pos[-1]=="left":
                return (pos[0],pos[1],"up")
            if pos[-1]=="right":
                return (pos[0],pos[1],"down")
            if pos[-1]=="down":
                return (pos[0],pos[1],"left")
        
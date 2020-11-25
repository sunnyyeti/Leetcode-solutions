# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

# Example 1:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
# Example 2:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
# Example 3:

# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
 

# Constraints:

# p1.length == p2.length == p3.length == p4.length == 2
# -104 <= xi, yi <= 104
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.isvalid(p1,p2,p3,p4) or self.isvalid(p1,p3,p2,p4) or self.isvalid(p1,p4,p2,p3)
        
    def isvalid(self,p1,p2,p3,p4):
        return (self.dis(p1,p3)==self.dis(p3,p2)==self.dis(p4,p2)==self.dis(p4,p1)) and self.dis(p1,p3)!=0 and self.per(p1,p3,p3,p2) and self.per(p3,p2,p2,p4) and self.per(p2,p4,p4,p1) and self.per(p4,p1,p1,p3)
    
    def dis(self,p1,p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    
    def per(self,p1,p2,p3,p4):
        l1 = p1[0]-p2[0],p1[1]-p2[1]
        l2 = p3[0]-p4[0],p3[1]-p4[1]
        return l1[0]*l2[0]+l1[1]*l2[1]==0
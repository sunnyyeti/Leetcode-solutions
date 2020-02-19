# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

# Note:

# The number of stones is ≥ 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:

# [0,1,3,5,6,8,12,17]

# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.

# Return true. The frog can jump to the last stone by jumping 
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
# 2 units to the 4th stone, then 3 units to the 6th stone, 
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:

# [0,1,2,3,4,8,9,11]

# Return false. There is no way to jump to the last stone as 
# the gap between the 5th and 6th stone is too large.
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.stones = stones
        self.cache = {}
        return self.helper(0,0)
    def helper(self,last_jump,ind):
        if ind==len(self.stones)-1:
            return True
        if (last_jump,ind) in self.cache:
            return self.cache[(last_jump,ind)]
        for next_jump in [last_jump-1,last_jump,last_jump+1]:
            if next_jump:
                next_ind =  self.find(ind+1,len(self.stones)-1,self.stones[ind]+next_jump)
                if next_ind != -1 and self.helper(next_jump,next_ind):
                    self.cache[(last_jump,ind)] = True
                    return True
        self.cache[(last_jump,ind)] = False
        return False
    
    def find(self,start,end,target):
        while start<=end:
            mid = (start+end)//2
            if self.stones[mid]==target:
                return mid
            elif self.stones[mid]<target:
                start=mid+1
            else:
                end = mid-1
        return -1
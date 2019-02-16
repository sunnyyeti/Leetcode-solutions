# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

# Note:

# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
 

# Example 1:

# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

# Example 2:

# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
class Solution:
    def findRadius(self, houses: 'List[int]', heaters: 'List[int]') -> 'int':
        if not houses:
            return 0
        heaters.sort()
        min_radius = float("-inf")
        for h in houses:
            pos = self.get_lower_bound(heaters,h)
            if pos == -1:
                min_radius = max(min_radius,heaters[0]-h)
            elif pos == len(heaters)-1:
                min_radius = max(min_radius,h-heaters[-1])
            else:
                min_radius = max(min_radius,min(h-heaters[pos],heaters[pos+1]-h))
        return min_radius
    def get_lower_bound(self,arr,tar):
        begin = 0
        end = len(arr)-1
        while begin<=end:
            mid = (begin+end)//2
            if arr[mid]>tar:
                end = mid-1
            else:
                begin = mid+1
        return end
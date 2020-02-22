# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

# Example 1:
# Input: [1,1,2,2,2]
# Output: true

# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:
# Input: [3,3,3,3,4]
# Output: false

# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# Accepted
# 28.4K
# Submissions
# 77.6K
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target, rem = divmod(sum(nums), 4)
        if rem:
            return False

        def getSides(i, target):
            # return all the possible ways we can make a side
            if target == 0:
                return [[]]
            if i == len(nums) or target < 0:
                return []
            else:
                include = [[i] + c for c in getSides(i + 1, target - nums[i])]
                return include + getSides(i + 1, target)
        def getgroups(i,target):
            if target==0:
                return [[]]
            if i==len(nums) or target<0:
                return []
            subgroups = getgroups(i+1,target-nums[i])
            includes =  [[i]+g for g in subgroups]
            excludes = getgroups(i+1,target)
            return includes+excludes        
        #groups = getSides(0, target)
        #print(groups)
        #groups = []
        #for i in range(len(nums)):
            #groups.extend(getgroups(i,target))
        groups = getgroups(0,target)
        #print(groups)
        if len(groups) < 4:
            return False
        else:
            usage = {i:0 for i in range(len(nums))}
            for g in groups:
                for i in g:
                    usage[i] += 1
            for index in usage:
                if usage[index] == 0 or usage[index] + 3 > len(groups):
                    return False
        return True
    def makesquaret(self, nums: List[int]) -> bool:
        sides = [0,0,0,0]
        def help(ind):
            _id = (ind,tuple(sorted(sides)))
            if _id in cache:
                return cache[_id]
            if ind==len(nums):
                if sides[0]==sides[1]==sides[2]==sides[3]:
                    return True
                else:
                    return False
            for s in range(4):
                if s==1 and (sides[0]==sides[1]):
                    continue
                if s==2 and (sides[2] in (sides[0],sides[1])):
                    continue
                if s==3 and (sides[3] in (sides[0],sides[1],sides[2])):
                    continue
                sides[s]+=nums[ind]
                if sides[s]<=tar and help(ind+1):
                    #cache[_id] = True
                    return True
                else:
                    sides[s]-=nums[ind]
            cache[_id] = False    
            return False
        if len(nums)<4:
            return False
        nums.sort()
        _sum = sum(nums)
        if _sum%4!=0:
            return False
        tar = _sum//4
        cache = {}
        return help(0)
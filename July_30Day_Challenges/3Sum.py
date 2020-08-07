# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#    Hide Hint #1  
# So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!
#    Hide Hint #2  
# For the two-sum problem, if we fix one of the numbers, say
# x
# , we have to scan the entire array to find the next number
# y
# which is
# value - x
# where value is the input parameter. Can we change our array somehow so that this search becomes faster?
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def help(nums,start,end,target):
            while start<=end:
                mid = (start+end)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]<target:
                    start = mid+1
                else:
                    end = mid-1
            return False
        nums.sort()
        hash_map = {}
        for i,e in enumerate(nums):
            hash_map.setdefault(e,[]).append(i)
        #print(hash_map)
        ans = []
        first = None
        second = None
        for i in range(0,len(nums)-2):
            if nums[i]!=first:
                first = nums[i]
                for j in range(i+1,len(nums)-1):
                    if nums[j]!=second:
                        second = nums[j]
                        t = -first-second
                        if hash_map.get(t,[-100])[-1]>j:
                            ans.append([nums[i],nums[j],t])
        #print(ans)
        return ans
        rs = set(tuple(r) for r in ans)
        return [list(r) for r in rs]
        
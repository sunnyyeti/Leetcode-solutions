# Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
from collections import Counter
class Solution:
    def triangleNumber(self, nums: 'List[int]') -> 'int':
        #count = Counter(nums)
        #nums = list(set(nums))
        nums.sort()
        ans = 0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                lower_b = self.find_lowerbound(nums,j+1,len(nums)-1,nums[i]+nums[j])
                ans+=lower_b-j
        return ans
        
    
    def find_lowerbound(self,arr,begin,end,target):
        while begin<=end:
            mid = (begin+end)//2
            if arr[mid]>=target:
                end = mid-1
            else:
                begin = mid+1
        return end
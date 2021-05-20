# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one element.
 

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        less_than_before_inds = []
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                less_than_before_inds.append(i)
        #print(less_than_before_inds)
        if len(less_than_before_inds)==0:
            return True
        elif len(less_than_before_inds)>1:
            return False
        else:
            i = less_than_before_inds[0]
            if i==1 or i==len(nums)-1:
                return True
            else:
                if nums[i]>=nums[i-2] or nums[i+1]>=nums[i-1]:
                    return True
                else:
                    return False
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                ind = i
                break
        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        
        if ind == 0:
            reverse(nums,0,len(nums)-1)
        else:
            target = nums[ind-1]
            min_v = float("inf")
            min_ind = -1
            for j in range(ind,len(nums)):
                if nums[j]>target and nums[j]<=min_v:
                    min_v = nums[j]
                    min_ind = j
            nums[min_ind],nums[ind-1] = nums[ind-1],nums[min_ind]
            reverse(nums,ind,len(nums)-1)
            
                    
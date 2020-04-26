# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_ind = 0
        cur_ind = 0
        while cur_ind<len(nums):
            if nums[cur_ind]:
                nums[insert_ind] = nums[cur_ind]
                insert_ind+=1
            cur_ind+=1
        while insert_ind<len(nums):
            nums[insert_ind]=0
            insert_ind+=1
            
        
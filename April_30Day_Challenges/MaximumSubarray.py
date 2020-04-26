# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_conquer(nums,start,end):
            if start==end:
                return nums[start]
            mid = (start+end)//2
            left_max = divide_conquer(nums,start,mid)
            right_max = divide_conquer(nums,mid+1,end)
            tmp_max = right_half_max = nums[mid+1]
            for j in range(mid+2,end+1):
                tmp_max = tmp_max+nums[j]
                if tmp_max>right_half_max:
                    right_half_max = tmp_max
            tmp_max = left_half_max = nums[mid]
            for j in range(mid-1,start-1,-1):
                tmp_max = tmp_max+nums[j]
                if tmp_max>left_half_max:
                    left_half_max = tmp_max
            return max(left_max,right_max,left_half_max+right_half_max)
                    
        def dynamic_programming(nums):
            max_sum = previous_sum = nums[0]
            for i in range(1,len(nums)):
                previous_sum = max(previous_sum+nums[i],nums[i])
                max_sum = max(max_sum,previous_sum)
            return max_sum
        return divide_conquer(nums,0,len(nums)-1)
            
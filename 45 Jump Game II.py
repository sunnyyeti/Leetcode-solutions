# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 105
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=len(nums)-1:
                min_steps = 1
            else:
                min_steps = min((steps[i+step] for step in range(1,nums[i]+1)),default=float("inf"))+1
            steps[i] = min_steps
        return steps[0]
                    
            
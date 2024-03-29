# Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

# Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

 

# Example 1:

# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: Change the array [5,3,2,4] to [2,2,2,2].
# The difference between the maximum and minimum is 2-2 = 0.
# Example 2:

# Input: nums = [1,5,0,10,14]
# Output: 1
# Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
# The difference between the maximum and minimum is 1-0 = 1.
# Example 3:

# Input: nums = [6,6,0,1,1,4,6]
# Output: 2
# Example 4:

# Input: nums = [1,5,6,14,15]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        min_dif = float('inf')
        for left in range(0, 4):
            right = 3-left
            min_v = min(nums[0+left:len(nums)-right])
            max_v = max(nums[0+left:len(nums)-right])
            dif = max_v-min_v
            min_dif = min(dif, min_dif)
        return min_dif

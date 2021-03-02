# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
 
 class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorts = sorted(nums)
        dif = False
        begin,end = -1,-1
        for i in range(len(nums)):
            if nums[i]!=sorts[i]:
                if not dif:
                    begin = i
                    dif = True
                else:
                    end = i
        return 0 if not dif else end-begin+1

class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        cur_max = float("-inf")
        begin,end = -1,-1
        for i, v in enumerate(nums):
            if v<cur_max:
                end = i
            else:
                cur_max = v
        cur_min = float("inf")
        for i in range(len(nums)-1,-1,-1):
            v = nums[i]
            if v>cur_min:
                begin = i
            else:
                cur_min = v
        return end-begin+1 if end!=begin else 0
            
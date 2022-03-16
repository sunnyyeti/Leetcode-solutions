# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)
from functools import cache


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1]+n)

        @cache
        def min_max_subarray_sum(ind, splits):
            if splits == 1:
                return prefix_sum[-1]-prefix_sum[ind]
            if splits == len(nums)-ind:
                return max(nums[ind:])
            min_max = float("inf")
            acc_sum = 0
            for end in range(ind, len(nums)-splits+1):
                acc_sum += nums[end]
                if acc_sum > min_max:
                    break
                next_min_max = min_max_subarray_sum(end+1, splits-1)
                cur_min_max = max(acc_sum, next_min_max)
                min_max = min(min_max, cur_min_max)
            return min_max
        return min_max_subarray_sum(0, m)

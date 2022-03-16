# You are given an integer array nums.

# You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

# Return true if it is possible to achieve that and false otherwise.

# Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7,8]
# Output: true
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
# Example 2:

# Input: nums = [3,1]
# Output: false
 

# Constraints:

# 1 <= nums.length <= 30
# 0 <= nums[i] <= 104
from functools import cache
from fractions import Fraction
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        total_cnt = len(nums)
        @cache
        def find(target,k,start_ind):
            if k==0:return target==0
            if target<0 or len(nums)-start_ind<k:return False
            return find(target-nums[start_ind],k-1,start_ind+1) or find(target,k,start_ind+1)
        return any(find(total_sum*k//total_cnt,k,0) for k in range(1,len(nums)//2+1) if total_sum*k%total_cnt==0)
        
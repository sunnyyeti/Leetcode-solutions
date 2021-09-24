# Given an integer array nums, return the number of all the arithmetic subsequences of nums.

# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.

 

# Example 1:

# Input: nums = [2,4,6,8,10]
# Output: 7
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
# Example 2:

# Input: nums = [7,7,7,7,7]
# Output: 16
# Explanation: Any subsequence of this array is arithmetic.
 

# Constraints:

# 1  <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(lambda : [1,0,0]) for _ in nums] 
        #[ #length1, #length2, #length>=3]
        ans = 0
        for i in range(1,len(nums)):
            n = nums[i]
            cur_dp = dp[i]
            for j in range(i-1,-1,-1):
                prev = nums[j]
                dif = n-prev
                last_dp = dp[j]
                cur_length_cnt = cur_dp[dif]
                prev_length_cnt = last_dp[dif]
                cur_length_cnt[1] += prev_length_cnt[0]
                cur_length_cnt[2] += prev_length_cnt[1]+prev_length_cnt[2]
        for d in dp:
            for k,v in d.items():
                ans += v[-1]
        return ans
                
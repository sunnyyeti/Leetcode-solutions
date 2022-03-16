# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

 

# Example 1:

# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:

# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
 

# Constraints:

# 1 <= nums.length <= 2 * 105
# -104 <= nums[i] <= 104
# -109 <= k <= 109
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: -1}
        ans = 0
        sum_ = 0
        for i, n in enumerate(nums):
            sum_ += n
            if sum_-k in prefix_sum:
                ans = max(ans, i-prefix_sum[sum_-k])
            if sum_ not in prefix_sum:
                prefix_sum[sum_] = i
        return ans

# Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

# Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

 

# Example 1:

# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
# Example 2:

# Input: nums = [0], lower = 0, upper = 0
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# -105 <= lower <= upper <= 105
# The answer is guaranteed to fit in a 32-bit integer.
from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList([0])
        prev_sum = 0
        upper_cnt = 0
        lower_cnt = 0
        for i,v in enumerate(nums):
            acc_sum = prev_sum + v
            th1 = acc_sum - upper
            th2 = acc_sum-lower+1
            insert1 = sl.bisect_left(th1)
            insert2 = sl.bisect_left(th2)
            upper_cnt += len(sl)-insert1
            lower_cnt += len(sl)-insert2
            prev_sum = acc_sum
            sl.add(prev_sum)
        return upper_cnt - lower_cnt
            

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

import bisect
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc_sum = [0]
        for n in nums:
            acc_sum.append(acc_sum[-1]+n)
        ans = 0
        cnt = {}
        for i, s in enumerate(acc_sum):
            cnt.setdefault(s,[]).append(i)
        for i in range(len(acc_sum)-1,0,-1):
            right_sum = acc_sum[i]
            left_sum = right_sum - k
            #print(i,right_sum)
            if left_sum in cnt:
                inds = cnt[left_sum]
                ans += bisect.bisect_left(inds,i)   
        return ans
                
            
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc_sum = [0]
        cnt = {0:1}
        for n in nums:
            cur_acc = acc_sum[-1]+n
            acc_sum.append(cur_acc)
            cnt[cur_acc] = cnt.setdefault(cur_acc,0)+1
        ans=0
        for i in range(len(nums)):
            cnt[acc_sum[i]]-=1
            ans+=cnt.get(acc_sum[i]+k,0)
        return ans
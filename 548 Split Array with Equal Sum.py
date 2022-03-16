# Given an integer array nums of length n, return true if there is a triplet (i, j, k) which satisfies the following conditions:

# 0 < i, i + 1 < j, j + 1 < k < n - 1
# The sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
# A subarray (l, r) represents a slice of the original array starting from the element indexed l to the element indexed r.
 

# Example 1:

# Input: nums = [1,2,1,2,1,2,1]
# Output: true
# Explanation:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# Example 2:

# Input: nums = [1,2,1,2,1,2,1,2]
# Output: false
 

# Constraints:

# n == nums.length
# 1 <= n <= 2000
# -106 <= nums[i] <= 106
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if len(nums) < 7:
            return False
        pre_sum = [0]*(len(nums)+1)
        for i, n in enumerate(nums):
            pre_sum[i+1] = pre_sum[i]+n
        #print(pre_sum)

        def get_sum_between(s, e):
            # s: start index
            # e: end_index
            # both are inclusive
            return pre_sum[e+1]-pre_sum[s]

        for j in range(3, len(nums)-3):
            first_half_split = set()
            for i in range(1, j-1):
                sum_1 = get_sum_between(0, i-1)
                sum_2 = get_sum_between(i+1, j-1)
                if sum_1 == sum_2:
                    first_half_split.add(sum_1)
            for k in range(j+2, len(nums)-1):
                sum_3 = get_sum_between(j+1, k-1)
                sum_4 = get_sum_between(k+1, len(nums)-1)
                if sum_3 == sum_4 and sum_3 in first_half_split:
                    return True
        return False

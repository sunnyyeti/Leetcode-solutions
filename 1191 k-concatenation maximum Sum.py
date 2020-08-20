# Given an integer array arr and an integer k, modify the array by repeating it k times.

# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

# As the answer can be very large, return the answer modulo 10^9 + 7.

 

# Example 1:

# Input: arr = [1,2], k = 3
# Output: 9
# Example 2:

# Input: arr = [1,-2,1], k = 5
# Output: 2
# Example 3:

# Input: arr = [-1,-2], k = 7
# Output: 0
 

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4
# Accepted
# 12,076
# Submissions
# 46,688
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_sum = arr[0]
        last_sum = arr[0]
        for i in range(1,len(arr)*2):
            cur = arr[i%len(arr)]
            last_sum = max(last_sum+cur,cur)
            max_sum = max(last_sum,max_sum)
        arr_sum = sum(arr)
        if arr_sum<=0:
            max_sum = max_sum%(10**9+7) if max_sum>0 else 0
        else:
            max_sum = (max_sum+(k-2)*arr_sum)
            max_sum = max_sum%(10**9+7) if max_sum>0 else 0
        return max_sum
        
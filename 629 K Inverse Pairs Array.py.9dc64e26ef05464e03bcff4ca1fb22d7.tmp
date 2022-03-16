# Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

# We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

# Since the answer may be very large, the answer should be modulo 109 + 7.

# Example 1:

# Input: n = 3, k = 0
# Output: 1
# Explanation: 
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
 

# Example 2:

# Input: n = 3, k = 1
# Output: 2
# Explanation: 
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

# Note:

# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp1 = [1]*(k+2) #n==1
        dp1[0] = 0
        for nn in range(2,n+1):
            dp2 = [0]*(k+2)
            for kk in range(0,k+1):
                end = kk
                start  = max(0,kk-nn+1)
                dp2[kk+1] = dp1[end+1]-dp1[start]
                dp2[kk+1] += dp2[kk]
            dp1 = dp2
        return (dp1[k+1]-dp1[k])%(10**9+7)
# Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning.

 

# Example 1:

# Input: A = [1,15,7,9,2,5,10], K = 3
# Output: 84
# Explanation: A becomes [15,15,15,9,10,10,10]
 

# Note:

# 1 <= K <= A.length <= 500
# 0 <= A[i] <= 10^6
class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ans = [0]
        for i,a in enumerate(A):
            max_v = a
            max_ans = float("-inf")
            for k in range(K):
                if i-k>=0:
                    max_v = max(max_v,A[i-k])
                else:
                    break
                max_ans = max(max_ans,(k+1)*max_v+ans[i-k])
            ans.append(max_ans)
        return ans[-1]

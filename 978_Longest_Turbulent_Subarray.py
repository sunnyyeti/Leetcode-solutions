# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

 

# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:

# Input: [4,8,12,16]
# Output: 2
# Example 3:

# Input: [100]
# Output: 1
 

# Note:

# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9

class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A)<=1:
            return len(A)
        max_length = 0
        predif = A[1]-A[0]
        if predif!=0:
            curl = 2
        else:
            curl = 1
        i = 2
        while i<len(A):
            if (A[i]-A[i-1])*predif<0:
                curl+=1
            else:
                max_length = max(max_length,curl)
                if A[i]==A[i-1]:
                    curl = 1
                else:
                    curl = 2                    
            predif = A[i]-A[i-1]
            i+=1
        return max(max_length,curl)
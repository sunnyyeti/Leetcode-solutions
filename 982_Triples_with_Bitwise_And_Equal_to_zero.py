# Given an array of integers A, find the number of triples of indices (i, j, k) such that:

# 0 <= i < A.length
# 0 <= j < A.length
# 0 <= k < A.length
# A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
 

# Example 1:

# Input: [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
 

# Note:

# 1 <= A.length <= 1000
# 0 <= A[i] < 2^16
# Accepted
# 1,674
# Submissions
# 3,300


class Solution:

    def countTriplets_(self, A: 'List[int]') -> 'int':
        N = 1<<16
        dp = [0]*N
        dp[N-1] = 1
        for i in range(3):
            tmp = [0]*N
            for k in range(N):
                for a in A:
                    tmp[a&k]+=dp[k]
            dp = tmp

        return dp[0]

    def countTriplets(self, A: 'List[int]') -> 'int':
        N = 1<<16
        cnt = [0]*N
        max_v = -1
        for a in A:
            if a>max_v:
                max_v = a
            for b in A:
                cnt[a&b]+=1
        res = 0
        for c in A:
            for key in range(max_v+1):
                if key & c == 0:
                    res+=cnt[key]

        return res
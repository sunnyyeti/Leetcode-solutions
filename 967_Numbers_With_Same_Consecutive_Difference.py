# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

# You may return the answer in any order.

 

# Example 1:

# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

# Note:

# 1 <= N <= 9
# 0 <= K <= 9

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = []
        for i in range(10):
            if N!=1 and i==0:
                continue
            res.extend(self.helper(N,K,str(i)))
        return list(map(int,res))
        
    def helper(self,N,K,start):
        res = []
        if N==1:
            return [start]
        tmp1 = []
        if int(start)+K<=9:
            tmp1 = self.helper(N-1,K,str(int(start)+K))
        tmp2 = []
        if int(start)-K>=0 and int(start)-K!=int(start)+K:
            tmp2 = self.helper(N-1,K,str(int(start)-K))
        for t in tmp1+tmp2:
            res.append(start+t)
        return res
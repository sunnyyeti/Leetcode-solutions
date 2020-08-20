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
from functools import lru_cache
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = self.help(N,K)
        if N>1:
            ans = [a for a in ans if a[0]!='0']
        return [int(a) for a in ans]
    @lru_cache(maxsize=None)
    def help(self,N,K):
        if N==1:
            return {'0','1','2','3','4','5','6','7','8','9'}
        n_1 = self.help(N-1,K)
        ans = set()
        for b in {'0','1','2','3','4','5','6','7','8','9'}:
            for ns in n_1:
                if abs(ord(ns[0])-ord(b))==K:
                    ans.add(b+ns)
        return ans
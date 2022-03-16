# Numbers can be regarded as the product of their factors.

# For example, 8 = 2 x 2 x 2 = 2 x 4.
# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range [2, n - 1].

 

# Example 1:

# Input: n = 1
# Output: []
# Example 2:

# Input: n = 12
# Output: [[2,6],[3,4],[2,2,3]]
# Example 3:

# Input: n = 37
# Output: []
 

# Constraints:

# 1 <= n <= 107
import math
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        tmp = []
        def bt(val):
            tmp.append(val)
            ans.append(tmp[:])
            tmp.pop()
            for i in range(2,int(math.sqrt(val))+1):
                if val%i==0 and (not tmp or i>=tmp[-1]):
                    tmp.append(i)
                    bt(val//i)
                    tmp.pop()
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                tmp.append(i)
                bt(n//i)
                tmp.pop()
        return ans
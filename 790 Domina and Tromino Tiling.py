# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000
from functools import cache
class Solution:
    # @cache
    # def numTilings(self, n: int) -> int:
    #     if n==0:
    #         return 1
    #     if n==1:
    #         return 1
    #     if n==2:
    #         return 2
    #     if n==3:
    #         return 5
    #     part1 = self.numTilings(n-1)+self.numTilings(n-2)
    #     part2 = 2*sum(self.numTilings(i) for i in range(0,n-2))
    #     return (part1+part2)%(10**9+7)
    
    def numTilings(self, n: int) -> int:
        if n<=2:
            return n
        MOD = 10**9+7
        pp,p = 1,2
        prev_sum = 1
        for i in range(3,n+1):
            cur = (pp+p+2*prev_sum)%MOD
            prev_sum = (prev_sum+pp)%MOD
            pp,p = p,cur
        return cur
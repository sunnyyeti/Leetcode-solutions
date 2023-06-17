# <!-- There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

# Example 1:


# Input: piles = [[1,100,3],[7,8,9]], k = 2
# Output: 101
# Explanation:
# The above diagram shows the different ways we can choose k coins.
# The maximum total we can obtain is 101.
# Example 2:

# Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
# Output: 706
# Explanation:
# The maximum total can be obtained if we choose all coins from the last pile.
 

# Constraints:

# n == piles.length
# 1 <= n <= 1000
# 1 <= piles[i][j] <= 105
# 1 <= k <= sum(piles[i].length) <= 2000 -->
from functools import cache
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        def get_prefix_sum(pile):
            prefix_sum = [0]
            for i in range(0,len(pile)):
                prefix_sum.append(prefix_sum[-1]+pile[i])
            return prefix_sum
        prefix_sum_piles = [get_prefix_sum(pile) for pile in piles]
        
        #print(prefix_sum_piles)
        prefix_sum_total = [0]*len(prefix_sum_piles)
        prev = 0
        for i in reversed(range(len(prefix_sum_piles))):
            prefix_sum_total[i] = prefix_sum_piles[i][-1] + prev
            prev = prefix_sum_total[i]
        #print(prefix_sum_total)
        length_to_end = [0]*len(piles)
        prev = 0
        for i in reversed(range(len(piles))):
            length_to_end[i] = len(piles[i])+prev
            prev = length_to_end[i]
        #print(length_to_end)
        @cache
        def max_coins_from_index(index,k):
            if index >= len(piles):
                return 0
            if k==0:
                return 0
            if length_to_end[index] <= k:
                return prefix_sum_total[index]
            max_coins = float("-inf")
            for cur_k in range(min(len(piles[index])+1,k+1)):
                chose_coins = prefix_sum_piles[index][cur_k]
                max_coins = max(max_coins,chose_coins+max_coins_from_index(index+1,k-cur_k))
            #print(index,k,max_coins)
            return max_coins
        return max_coins_from_index(0,k)
            
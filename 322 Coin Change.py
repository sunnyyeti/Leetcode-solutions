# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def help(amount):
            if amount==0:
                return 0
            if amount<0:
                return -1
            min_needs = float("inf")
            for i in range(len(coins)-1,-1,-1):
                remain_amount = amount-coins[i]
                remain_needs = help(remain_amount)
                if remain_needs<min_needs and remain_needs!=-1:
                    min_needs = remain_needs
            if min_needs<float("inf"):
                return min_needs+1
            else:
                return -1
        return help(amount)
        
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
# Example 4:

# Input: coins = [1], amount = 1
# Output: 1
# Example 5:

# Input: coins = [1], amount = 2
# Output: 2
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
import bisect
import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.cache
        def help(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            min_ = float("inf")
            right = bisect.bisect_right(coins,amount)-1
            for i in range(right,-1,-1):
                cur = coins[i]
                min_ = min(min_,help(amount-cur))
            return min_+1
        coins.sort()
        res =  help(amount)
        return res if res < float("inf") else -1
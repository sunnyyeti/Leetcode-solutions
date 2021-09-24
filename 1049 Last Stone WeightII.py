# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
# Example 2:

# Input: stones = [31,26,33,21,40]
# Output: 5
# Example 3:

# Input: stones = [1,2]
# Output: 1
 

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100
from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        stones.sort(reverse=True)
        @cache
        def max_stones(max_sum, ind):
            max_v = 0
            for i in range(ind, len(stones)):
                if stones[i] <= max_sum:
                    next_v = max_stones(max_sum-stones[i], i+1)
                    max_v = max(max_v, stones[i]+next_v)
            return max_v
        max_v = max_stones(total_sum//2, 0)
        #print(max_v)
        return total_sum-2*max_v

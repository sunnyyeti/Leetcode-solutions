# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

 

# Example 1:


# Input: inventory = [2,5], orders = 4
# Output: 14
# Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
# The maximum total value is 2 + 5 + 4 + 3 = 14.
# Example 2:

# Input: inventory = [3,5], orders = 6
# Output: 19
# Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
# The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
# Example 3:

# Input: inventory = [2,8,4,10,6], orders = 20
# Output: 110
# Example 4:

# Input: inventory = [1000000000], orders = 1000000000
# Output: 21
# Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.
 

# Constraints:

# 1 <= inventory.length <= 105
# 1 <= inventory[i] <= 109
# 1 <= orders <= min(sum(inventory[i]), 109)
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10**9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)
        last_sum = 0
        last_ops = 0
        last_len = 1
        last_ele = inventory[0]
        for i in range(1,len(inventory)):
            cur_ele = inventory[i]
            if cur_ele != last_ele:
                new_ops = last_ops + (last_ele - cur_ele)*last_len
                if new_ops <= orders:
                    last_ops = new_ops
                    last_sum = (last_sum + (last_ele+cur_ele+1)*(last_ele-cur_ele)//2*last_len)%mod
                    last_ele = cur_ele
                    last_len += 1
                else:
                    needed_ops = orders - last_ops
                    rounds = needed_ops // last_len
                    remain = needed_ops % last_len
                    last_sum = (last_sum + (last_ele+last_ele-rounds+1)*(rounds)//2*last_len)%mod
                    new_base = last_ele-rounds
                    last_sum = (last_sum + new_base*remain)%mod
                    return last_sum
            else:
                last_len += 1
        return last_sum
        
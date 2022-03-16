# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

# Return the minimum number of transactions required to settle the debt.

 

# Example 1:

# Input: transactions = [[0,1,10],[2,0,5]]
# Output: 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
# Example 2:

# Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
# Output: 1
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

# Constraints:

# 1 <= transactions.length <= 8
# transactions[i].length == 3
# 0 <= fromi, toi <= 20
# fromi != toi
# 1 <= amounti <= 100
from functools import cache


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        net = [0]*20
        for from_, to_, amount in transactions:
            net[from_] += amount
            net[to_] -= amount
            #因为要还钱
        outs = []
        ins = []
        for v in net:
            if v < 0:
                outs.append(-v)
            elif v > 0:
                ins.append(v)
        outs.sort()
        ins.sort()
        #print(outs,ins)

        @cache
        def min_trans(outs, ins):
            #print(outs,ins)
            if len(outs) == 0 and len(ins) == 0:
                return 0
            if len(outs) == 1:
                return len(ins)
            if len(ins) == 1:
                return len(outs)
            outs, ins = list(outs), list(ins)
            #print(outs,ins)
            min_out = outs[0]
            min_next_ = float('inf')
            for i in range(len(ins)):
                cur_in = ins[i]
                cur_max = min(min_out, cur_in)
                outs[0] -= cur_max
                ins[i] -= cur_max
                routs = tuple(sorted((o for o in outs if o)))
                rins = tuple(sorted((i_ for i_ in ins if i_)))
                next_ = min_trans(routs, rins)
                min_next_ = min(min_next_, next_)
                outs[0] += cur_max
                ins[i] += cur_max
            return min_next_ + 1
        return min_trans(tuple(outs), tuple(ins))

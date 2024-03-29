# You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after n days.

# You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

# Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

 

# Example 1:

# Input: bulbs = [1,3,2], k = 1
# Output: 2
# Explanation:
# On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
# On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
# On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
# We return 2 because on the second day, there were two on bulbs with one off bulb between them.
# Example 2:

# Input: bulbs = [1,2,3], k = 1
# Output: -1
 

# Constraints:

# n == bulbs.length
# 1 <= n <= 2 * 104
# 1 <= bulbs[i] <= n
# bulbs is a permutation of numbers from 1 to n.
# # 0 <= k <= 2 * 104
from sortedcontainers import SortedList
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        on_bulbs = SortedList()
        for b in bulbs:
            insert_ind = on_bulbs.bisect_left(b)
            if insert_ind-1 >=0 :
                if b-on_bulbs[insert_ind-1]==k+1:
                    return len(on_bulbs)+1
            if insert_ind < len(on_bulbs):
                if on_bulbs[insert_ind]-b==k+1:
                    return len(on_bulbs)+1
            on_bulbs.add(b)
        return -1
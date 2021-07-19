# In a deck of cards, each card has an integer written on it.

# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

# Each group has exactly X cards.
# All the cards in each group have the same integer.
 

# Example 1:

# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:

# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# Example 3:

# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
# Example 4:

# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
# Example 5:

# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
 

# Constraints:

# 1 <= deck.length <= 104
# 0 <= deck[i] < 104
from collections import Counter
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = Counter(deck)
        min_cnt = min(cnt.values())
        if min_cnt < 2:
            return False

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a
        counts = sorted(set(cnt.values()))
        gcd = reduce(lambda x, y: gcd(x, y), counts)
        if gcd >= 2:
            return True
        return False

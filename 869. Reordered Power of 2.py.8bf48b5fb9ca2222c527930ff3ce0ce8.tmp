# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
# Example 3:

# Input: n = 16
# Output: true
# Example 4:

# Input: n = 24
# Output: false
# Example 5:

# Input: n = 46
# Output: true
from collections import Counter
class Solution:
    cands = set(2**i for i in range(31))
    def reorderedPowerOf2(self, n: int) -> bool:
        store = {}
        for c in self.cands:
            sc = str(c)
            store.setdefault(len(sc),[]).append(Counter(sc))
        sn = str(n)
        return any(c==Counter(sn) for c in store[len(sn)])
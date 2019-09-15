# You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

# Example 1:

# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:

# Input: "AAABBC"
# Output: 188
 

# Note:

# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.cnt = 0
        self.helper(Counter(tiles))
        return self.cnt
    
    def helper(self,cnt):
        for key in cnt:
            if cnt[key]>0:
                cnt[key]-=1
                self.cnt+=1
                self.helper(cnt)
                cnt[key] = cnt.get(key,0)+1

        
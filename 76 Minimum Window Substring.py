# Given two strings s and t of lengths m and n respectively, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of English letters.
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntt = Counter(t)
        occuured = set()
        cnt = {}
        i,j = 0 ,0
        ans = None
        while j<len(s):
            c = s[j]
            if c in cntt:
                cnt[c] = cnt.get(c,0)+1
                if cnt[c] >= cntt[c]:
                    occuured.add(c)
            while len(occuured)==len(cntt):
                if ans is None or j-i+1 < len(ans):
                    ans = s[i:j+1]
                if s[i] in cntt:
                    cnt[s[i]]-=1
                    if cnt[s[i]] < cntt[s[i]]:
                        occuured.remove(s[i])
                i+=1

            j+=1
        return '' if ans is None else ans
                    
                
        
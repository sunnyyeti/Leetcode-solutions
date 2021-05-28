# Given a string s, return the maximum number of ocurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
 

# Example 1:

# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 ocurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
# Example 2:

# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
# Example 3:

# Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# Output: 3
# Example 4:

# Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# Output: 0
 

# Constraints:

# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s only contains lowercase English letters.
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter()
        ans = 0
        for size in range(minSize,minSize+1):
            window_cnt = Counter(s[:size])
            if len(window_cnt)<=maxLetters:
                cnt[s[:size]] += 1
                ans = max(ans,cnt[s[:size]])
            for j in range(size,len(s)):
                window_cnt[s[j-size]]-=1
                if window_cnt[s[j-size]]==0:
                    del window_cnt[s[j-size]]
                window_cnt[s[j]] = window_cnt.get(s[j],0)+1
                if len(window_cnt)<=maxLetters:
                    cnt[s[j-size+1:j+1]] += 1
                    ans = max(ans,cnt[s[j-size+1:j+1]])
        return ans
            
            
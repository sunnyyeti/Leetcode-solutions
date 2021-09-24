# Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters.
from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i,j = 0,0
        chars = Counter(s[0:1])
        ans = 0
        while True:
            while j<len(s) and len(chars) <= 2:
                j+=1
                if j==len(s):
                    ans = max(ans,j-i)
                    return ans
                chars[s[j]]+=1
            ans = max(ans,j-i)
            while len(chars) > 2:
                chars[s[i]]-=1
                if chars[s[i]]==0:
                    del chars[s[i]]
                i+=1
                
                
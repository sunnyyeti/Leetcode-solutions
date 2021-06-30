# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 0 <= k <= 50
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = float('-inf')
        i,j = 0,0
        chars_set = {}
        while j<len(s):
            cur_char = s[j]
            chars_set[cur_char] = chars_set.get(cur_char,0)+1
            #print(chars_set)
            if len(chars_set)<=k:
                ans = max(ans,j-i+1)
            else:
                while len(chars_set) > k:
                    removed_char = s[i]
                    chars_set[removed_char]-=1
                    if chars_set[removed_char] == 0:
                        del chars_set[removed_char]
                    i+=1
                ans = max(ans,j-i+1)
            j+=1
        return ans
                
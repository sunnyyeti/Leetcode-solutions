# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1
 

# Constraints:

# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def isvalid():
            return cnt["a"] and cnt["b"] and cnt["c"]
        cnt = {"a":0,"b":0,"c":0}
        ans = 0
        j = 0
        for i in range(len(s)-2):
            if i:
                cnt[s[i-1]]-=1
                if isvalid():
                    ans+=len(s)-j
                    continue
                else:
                    j+=1
            while j<len(s):
                cnt[s[j]]+=1
                if isvalid():
                    ans+=len(s)-j
                    break
                j+=1
            else:
                break
        return ans
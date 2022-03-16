
# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.
 

# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:

# Input: s = "a", t = ""
# Output: true
# Example 4:

# Input: s = "", t = "A"
# Output: true
 

# Constraints:

# 0 <= s.length <= 104
# 0 <= t.length <= 104
# s and t consist of lower-case letters, upper-case letters and/or digits.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            return sum(c1!=c2 for c1,c2 in zip(s,t)) == 1
        if abs(len(s)-len(t))==1:
            if len(s)<len(t):
                s,t = t,s
            i,j = 0,0
            while i<len(s) and j<len(t) and s[i]==t[j]:
                i+=1
                j+=1
            if j==len(t):
                return True
            i+=1
            while i<len(s) and j<len(t) and s[i]==t[j]:
                i+=1
                j+=1
            return i==len(s) and j==len(t)
        else:
            return False
            
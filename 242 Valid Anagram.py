# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)
        for k in set(s):
            if cs[k]!=ct[k]:
                return False
        for k in set(t):
            if cs[k]!=ct[k]:
                return False
        return True
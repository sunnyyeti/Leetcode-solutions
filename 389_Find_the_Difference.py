# Given two strings s and t which consist of only lowercase letters.

# String t is generated by random shuffling string s and then add one more letter at a random position.

# Find the letter that was added in t.

# Example:

# Input:
# s = "abcd"
# t = "abcde"

# Output:
# e

# Explanation:
# 'e' is the letter that was added.
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = {}
        for c in t:
            cnt[c] = cnt.get(c,0)+1
        for c in s:
            cnt[c]-=1
            if cnt[c]==0:
                cnt.pop(c)
        return list(cnt.keys())[0]
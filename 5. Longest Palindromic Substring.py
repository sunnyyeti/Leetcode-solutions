# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        ans = 0
        start = 0
        end = 0
        for l in range(1,length+1):
            for i in range(length-l+1):
                j = i+l-1
                if s[i]!=s[j]:
                    dp[i][j] = 0
                else:
                    ii = i+1
                    jj = j-1
                    dp[i][j] = ii>jj or dp[ii][jj]
                    if dp[i][j]:
                        if j-i+1 > ans:
                            ans = j-i+1
                            start =i
                            end = j
        return s[start:end+1]
                
        
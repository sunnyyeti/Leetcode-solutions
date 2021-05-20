# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input: s = "acdcb", p = "a*c?b"
# Output: false
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1)  for _ in range(len(s)+1)]
        flags = [False]*(len(p)+1)
        flags[0] = True
        dp[0][0] = True
        for j in range(1,len(p)+1):
            pc = p[j-1]
            if pc != '*':
                dp[0][j] = False
            else:
                dp[0][j] = dp[0][j-1]
            flags[j] = flags[j] or dp[0][j]

        for i in range(1,len(s)+1):
            sc = s[i-1]
            for j in range(1,len(p)+1):
                pc = p[j-1]
                if pc=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif pc=='*':
                    dp[i][j] = flags[j-1]
                else:
                    dp[i][j] = sc==pc and dp[i-1][j-1]
                flags[j] = flags[j] or dp[i][j]
        return dp[-1][-1]
                    
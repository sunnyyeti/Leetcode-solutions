# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
 

# Constraints:

# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(p)+1):
            pc = p[i-1]
            if pc != '*':
                dp[0][i] = False
            else:
                dp[0][i] = dp[0][i-2] or dp[0][i-1]
        #print(dp)
        for i in range(1,len(s)+1):
            dp[i][0] = False
            sc = s[i-1]
            for j in range(1,len(p)+1):
                pc = p[j-1]
                if pc=='.':
                    dp[i][j] = dp[i-1][j-1]
                elif pc=='*':
                    dp[i][j] = dp[i][j-2] or ((sc==p[j-2] or p[j-2]=='.') and dp[i-1][j])      
                else:
                    dp[i][j] = (sc==pc and dp[i-1][j-1])
            #print(dp)
        return dp[-1][-1]
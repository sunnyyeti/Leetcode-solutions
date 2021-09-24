# Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

# Example 1:

# Input: s = "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
# Example 2:

# Input: s = "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "abc".
# Example 3:

# Input: s = "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase English letters.
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        seen = {s[-1]}
        dp = [0]*len(s)
        dp[-1] = 1
        for i in range(len(s)-2,-1,-1):
            cur_char = s[i]
            cnt = 0
            for j in range(i+1,len(s)):
                if (cur_char,j) not in seen:
                    cnt += dp[j]
                    seen.add((cur_char,j))
            if cur_char not in seen:
                seen.add(cur_char)
                cnt += 1
            dp[i] = cnt
        return sum(dp)%(10**9+7)
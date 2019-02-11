# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
# Accepted
# 50,726
# Submissions
# 112,504
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        length = [[1]*len(s) for _ in s]
        for r in range(len(s)-2,-1,-1):
            for c in range(r+1,len(s)):
                if s[r]==s[c]:
                    if r+1==c:
                        length[r][c]=2
                    else:
                        length[r][c] = max(length[r+1][c-1]+2,length[r+1][c],length[r][c-1])
                else:
                    length[r][c] = max(length[r+1][c],length[r][c-1])
        return length[0][-1]
        
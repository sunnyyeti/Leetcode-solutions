# Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.

# If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

 

# Example 1:

# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of s2 in the window must occur in order.
# Example 2:

# Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
# Output: ""
 

# Constraints:

# 1 <= s1.length <= 2 * 104
# 1 <= s2.length <= 100
# s1 and s2 consist of lowercase English letters.
# Accepted
# 61,870
# Submissions
# 144,927
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        def is_sub_sequence(s2, s1):
            ti = 0
            t = s2[ti]
            j = 0
            while j < len(s1):
                if s1[j] == t:
                    ti += 1
                    if ti == len(s2):
                        return True
                    t = s2[ti]
                j += 1
            return False
        if not is_sub_sequence(s2, s1):
            return ""
        if len(s2) == 1:
            return s2
        dp = [-1]*(len(s1))
        c0 = s2[0]
        for i, t in enumerate(s1):
            if t == c0:
                dp[i] = i
            else:
                if i > 0:
                    dp[i] = dp[i-1]
        j = 1
        while j < len(s2):
            c = s2[j]
            new_dp = [-1]*(len(s1))
            i = j
            while i < len(s1):
                t = s1[i]
                if t == c:
                    new_dp[i] = dp[i-1]
                else:
                    new_dp[i] = new_dp[i-1]
                i += 1
            dp = new_dp
            j += 1
        tar = s2[-1]
        ans = []
        for i, c in enumerate(s1):
            if c == tar:
                start = dp[i]
                if start != -1:
                    ans.append((i-start+1, start))
        ans.sort()
        l, s = ans[0]
        return s1[s:s+l]

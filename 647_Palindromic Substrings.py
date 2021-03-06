# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Note:
#
# The input string length won't exceed 1000.
class Solution:
    def countSubstrings(self, s: str) -> int:
        str_len = len(s)
        dp = [[True] * str_len for _ in range(str_len)]
        res = str_len
        for i in range(str_len - 1, -1, -1):
            for j in range(str_len - 1, i, -1):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = (i + 1 > j - 1) or dp[i + 1][j - 1]
                    res += dp[i][j]

        return res

class Solution2:
    def countSubstrings(self, st: str) -> int:
        def get(s,e):
            if s>e:
                return True
            return store[(s,e)]
        store = {}
        ans = 0
        for l in range(1,len(st)+1):
            for s in range(len(st)-l+1):
                e = s+l-1
                if st[s]==st[e]:
                    store[(s,e)] = get(s+1,e-1)
                    ans += store[(s,e)]
                else:
                    store[(s,e)] = False
        #print(store)
        return ans
                    
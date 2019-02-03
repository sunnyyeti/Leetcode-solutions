# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4

# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2

# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

#import numpy as np
class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # self.strs = strs
        # self.cache = {}
        # return self.helper(0,m,n)
        cnts = []
        for s in range(len(strs)+1):
            tmp = [[0]*(n+1) for _ in range(m+1)]
            cnts.append(tmp)
        for i in range(len(strs)-1,-1,-1):
            str_ = strs[i]
            num0 = str_.count("0")
            num1 = len(str_) - num0
            for r in range(m+1):
                for c in range(n+1):
                    if r<num0 or c<num1:
                        cnts[i][r][c] = cnts[i+1][r][c]
                    else:
                        cnts[i][r][c] = max(cnts[i+1][r][c],1+cnts[i+1][r-num0][c-num1])
        return cnts[0][m][n]

    def helper(self,ind,m,n):
        if ind>=len(self.strs):
            return 0
        if (ind,m,n) in self.cache:
            return self.cache[(ind,m,n)]
        cnt1 = self.helper(ind+1,m,n)
        num0 = self.strs[ind].count("0")
        num1 = len(self.strs[ind])-num0
        cnt2 = 0
        if m>=num0 and n>=num1:
            cnt2 = 1+self.helper(ind+1,m-num0,n-num1)
        self.cache[(ind,m,n)] = max(cnt2,cnt1)
        return max(cnt1,cnt2)



#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
import re
class Solution:
    def isMatch(self,s,p):
        len_s = len(s)
        p = re.sub("\*+","*",p)
        len_p = len(p)
        res = [[False]*(len_s+1) for _ in range(len_p+1)]
        res[-1][-1]= True
        for r in range(len_p-1,-1,-1):
            if p[r]=="*" and res[r+1][-1]:
                res[r][-1]=True
            else:
                res[r][-1]=False
        for r in range(len_p-1,-1,-1):
            row_flag = res[r][-1]
            pc = p[r]
            for c in range(len_s-1,-1,-1):
                sc = s[c]
                if pc=="*":
                    for tmpc in range(c,len_s+1):
                        if res[r+1][tmpc]==True:
                            res[r][c]=True
                            break
                    else:
                        res[r][c]=False
                elif pc=="?":
                    res[r][c] = res[r+1][c+1]
                else:
                    if pc!=sc:
                        res[r][c]=False
                    else:
                        res[r][c] = res[r+1][c+1]
                row_flag = row_flag or res[r][c]
            if not row_flag:
                return False
        return res[0][0]


if __name__ == "__main__":
    print(Solution().isMatch("aa","*?"))
        
        
            


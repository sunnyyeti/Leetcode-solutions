# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

# Example 1:

# Input: n = 13
# Output: 6
# Example 2:

# Input: n = 0
# Output: 0
 

# Constraints:

# 0 <= n <= 2 * 109
class Solution:
    def countDigitOne(self, n: int) -> int:
        strn =  str(n)
        lenn = len(strn)
        res = 0
        for i,c in enumerate(strn):
            #print(i,c)
            res += int(c) * (lenn - 1) * 10 ** (lenn - 2)  #比如567 第一位5 lenn为3， 0-99有(lenn-1)*10**(lenn-2)个
                                                           #现在是5，有5个 0-99(0-99 100-199 200-299 300-399 400-499)所以前面乘以int(c)
            if c>'1':
                res += 10**(lenn-1) #如果大于1， 比如还是5的时候， 则100-199 百位上的1，一共100个，就是  10**(lenn-1)
            elif c=='1': #如果等于1比如167,那么就不是所有100-199百位上的，而是100-167 一共68 个
                res += int(strn[i+1:])+1 if i<len(strn)-1 else 1
            lenn -= 1
        return int(res)

# 0 -9 1
# 0 -99 20
# 0 -999 300
# 0 -9999 4000
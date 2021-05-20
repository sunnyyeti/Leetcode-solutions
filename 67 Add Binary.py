# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# Accepted
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a,b = b,a
        ans = ['']*(len(a)+1)
        i,j = len(a)-1,len(b)-1
        c = 0
        k = len(ans)-1
        while i>=0 and j>=0:
            total = int(a[i])+int(b[j])+c
            c,v = divmod(total,2)
            ans[k] = str(v)
            i-=1
            j-=1
            k-=1
        while i>=0:
            total = int(a[i])+c
            c,v = divmod(total,2)
            ans[k] = str(v)
            k-=1
            i-=1
        if c:
            ans[k] = str(c)
        ans = ''.join(ans).lstrip('0')
        return ans if ans else '0'
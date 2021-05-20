# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            n1 = ord(num1[i])-ord('0')
            for j in range(len(num2)-1,-1,-1):
                n2 = ord(num2[j])-ord('0')
                mul = n1*n2
                pos = len(num1)-1-i+len(num2)-1-j
                pos = len(ans)-1-pos
                c = 0
                c1,v1 = divmod(mul,10)
                c2,v2 = divmod(ans[pos]+v1,10)
                c = c1+c2
                ans[pos] = v2
                pos -= 1
                while c:
                    c,v = divmod(ans[pos]+c,10)
                    ans[pos] = v
                    pos-=1
        ans = ''.join(map(lambda x: str(x), ans)).lstrip('0')
        return ans if ans else '0'
        
    def multiply_help(self,num1:str,num2:str):
        #num2 length is 1
        ans = ['']*(len(num1)+1)
        c = 0
        k = len(ans)-1
        i = len(num1)-1
        num2 = int(num2)
        while i>=0:
            total = int(num1[i])*num2+c
            ans[k] = str(total%10)
            c = total//10
            i-=1
            k-=1
        if c:
            ans[k] = str(c)
        return ''.join(ans)
            
        
    def add(self, num1:str, num2:str) -> str:
        i,j = len(num1)-1,len(num2)-1
        c = 0
        ans = ['']*(max(len(num1),len(num2))+1)
        k = len(ans)-1
        while i>=0 and j>=0:
            total = int(num1[i])+int(num2[j])+c
            ans[k] = str(total%10)
            c = total//10
            i-=1
            j-=1
            k-=1
        while i>=0:
            total = int(num1[i])+c
            ans[k] = str(total%10)
            c = total//10
            i-=1
            k-=1
        while j>=0:
            total = int(num2[j])+c
            ans[k] = str(total%10)
            c = total//10
            j-=1
            k-=1
        if c:
            ans[k] = str(c)
        return ''.join(ans)
            
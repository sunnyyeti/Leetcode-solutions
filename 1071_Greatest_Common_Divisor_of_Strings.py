# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

# Return the largest string X such that X divides str1 and X divides str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Note:

# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        com = self.gcd(len1,len2)
        for i in range(com,0,-1):
            if  len1%i==0 and len2%i==0 and str1[:i]==str2[:i]:
                if self.divides(i,str1) and self.divides(i,str2):
                    return str1[:i]
        return ""
    
    def divides(self,i,s):
        ori = s[:i]
        for t in range(i,len(s),i):
            if s[t:t+i]!=ori:
                return False
        return True
        
        
    def gcd(self,a,b):
        if a<b:
            a,b = b,a
        while a%b!=0:
            a,b = b,a%b
        return b
        
        
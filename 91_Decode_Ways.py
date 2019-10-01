# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
class Solution:
    def numDecodings(self, s: str) -> int:
        self.cache = {}
        return self.helper(s)
    
    def helper(self,s:str) -> int:
            if s[0]=='0':
                return 0
            if len(s)==1:
                return 1
            if len(s)==2:
                if int(s)<=26:
                    if s[-1]!='0':
                        return 2
                    else:
                        return 1
                else:
                    if s[-1]!='0':
                        return 1
                    else:
                        return 0
            if s in self.cache:
                return self.cache[s]
            ans = self.helper(s[1:])+(self.helper(s[2:]) if int(s[:2])<=26 else 0)
            self.cache[s]=ans
            return ans
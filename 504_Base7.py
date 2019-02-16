# Given an integer, return its base 7 string representation.

# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
class Solution:
    def convertToBase7(self, num: 'int') -> 'str':
        if num>=0:
            return self.convert(num)
        return "-"+self.convert(-num)
    
    def convert(self,num):
        if num==0:
            return "0"
        ans = []
        while num>0:
            ans.append(num%7)
            num = num//7
        return "".join(map(str,reversed(ans)))
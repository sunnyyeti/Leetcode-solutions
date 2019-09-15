# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            tmp = 0
            while num>0:
                tmp+=num%10
                num//=10
            num = tmp
        return 
        
class Solution:
    def addDigits(self, num: int) -> int:
        # while num>=10:
        #     tmp = 0
        #     while num>0:
        #         tmp+=num%10
        #         num//=10
        #     num = tmp
        # return num
        return num if not num else (num-1)%9+1
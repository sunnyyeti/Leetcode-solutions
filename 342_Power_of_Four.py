# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        c = math.log(num,4)
        return int(c)==c
        
    import math
    
    
class Solution(object):
    def isPowerOfFour_(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        c = math.log(num,4)
        return int(c)==c
    
    def isPowerOfFour(self,num):
        if num<=0:
            return False
        bits = bin(num)[3:]
        return len(bits)%2==0 and (set(bits)=={"0"} or set(bits)==set())
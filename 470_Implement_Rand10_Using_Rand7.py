# Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

# Do NOT use system's Math.random().

 

# Example 1:

# Input: 1
# Output: [7]
# Example 2:

# Input: 2
# Output: [8,4]
# Example 3:

# Input: 3
# Output: [8,1,10]
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            n1 = rand7()
            n2 = rand7()
            n = (n1-1)*7+n2
            if n<=40:
                r = n%10
                return r if r else 10
            
        